from data import CITIES, BUSINESSES, USERS, REVIEWS, TIPS, CHECKINS
from IPython.display import display
import random
import numpy as np
import ast
import pandas as pd

lijst = []
# filter door de BUSINESSES, haal geopende Restaurants eruit
for x in BUSINESSES['westlake']:
    for j in x['categories'].split(','):
        if j == 'Restaurants':
            lijst.append(x)

    for j in lijst:
        if j['is_open'] == 0:
            lijst.remove(x)
print(lijst)

# filter ambiances uit lijst
def filter(categorie, subcategorie):
    data=dict()
    for i in lijst:
        try:
            test = i[categorie].get(subcategorie)
            test = ast.literal_eval(test)
            data[i['business_id']] = []
            for k,v in test.items():
                if v == True:
                    data[i['business_id']].append(k)
        except:
            continue
    return data
data = filter('attributes', "Ambience")
data2 = pd.Series(data)
drie = data2.to_frame('Ambience').reset_index()
drie = drie.rename(columns = {'index' : 'business_id'})
display(drie)
def extract_subcategories(categorie):

    categorie_m = categorie.apply(lambda row: pd.Series([row['business_id']] + row['Ambience']), axis=1)
    stack_categorie = categorie_m.set_index(0).stack()
    df_stack_categorie = stack_categorie.to_frame()
    df_stack_categorie['business_id'] = stack_categorie.index.droplevel(1)
    df_stack_categorie.columns = ['Ambience', 'business_id']
    return df_stack_categorie.reset_index()[['business_id', 'Ambience']]

def pivot_categories(df):
    return df.pivot_table(index = 'business_id', columns = 'Ambience', aggfunc = 'size', fill_value=0)

df_categories = extract_subcategories(drie)
display(df_categories)
df_utility_matrix = pivot_categories(df_categories)
display(df_utility_matrix)

def create_similarity_matrix_categories(matrix):
    """Create a  """
    npu = matrix.values
    m1 = npu @ npu.T
    diag = np.diag(m1)
    m2 = m1 / diag
    m3 = np.minimum(m2, m2.T)
    return pd.DataFrame(m3, index = matrix.index, columns = matrix.index)
df_similarity_categories = create_similarity_matrix_categories(df_utility_matrix)
display(df_similarity_categories.head())

def recommend(user_id=None, business_id=None, city=None, n=10):
    """
    Returns n recommendations as a list of dicts.
    Optionally takes in a user_id, business_id and/or city.
    A recommendation is a dictionary in the form of:
        {
            business_id:str
            stars:str
            name:str
            city:str
            adress:str
        }
    """

    if not city:
        city = random.choice(CITIES)
    return random.sample(BUSINESSES[city], n)
