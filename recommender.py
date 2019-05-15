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

# filter subcategorieen uit lijst
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
    # maak dataframe gefilterd op subcategorie
def create_filter_dataframe(categorie, subcategorie):
    data = filter(categorie, subcategorie)
    data2 = pd.Series(data)
    drie = data2.to_frame(subcategorie).reset_index()
    drie = drie.rename(columns = {'index' : 'business_id'})
    return(drie)

create_filter_dataframe('attributes', 'Ambience')

def extract_subcategories(categorie):
    """Creates a utility matrix for subcategories
    Arguments:
    df -- a dataFrame containing at least the columns 'business_id' and 'subcategorie'
    Output:
    a matrix containing a rating in each cell
    """
    categorie_m = categorie.apply(lambda row: pd.Series([row['business_id']] + row['Ambience']), axis=1)
    stack_categorie = categorie_m.set_index(0).stack()
    df_stack_categorie = stack_categorie.to_frame()
    df_stack_categorie['business_id'] = stack_categorie.index.droplevel(1)
    df_stack_categorie.columns = ['Ambience', 'business_id']
    return df_stack_categorie.reset_index()[['business_id', 'Ambience']]

def pivot_categories(df):
    """Creates a adjusted(/soft) cosine similarity matrix.
    Arguments:
    matrix -- a utility matrix
    Notes:
    Missing values are set to 0. This is technically not a 100% correct, but is more convenient
    for computation and does not have a big effect on the outcome.
    """
    return df.pivot_table(index = 'business_id', columns = 'Ambience', aggfunc = 'size', fill_value=0)

df_categories = extract_subcategories(create_filter_dataframe('attributes', 'Ambience'))
df_utility_matrix = pivot_categories(df_categories)

def create_similarity_matrix_categories(matrix):
    """Create a  """
    npu = matrix.values
    m1 = npu @ npu.T
    diag = np.diag(m1)
    m2 = m1 / diag
    m3 = np.minimum(m2, m2.T)
    return pd.DataFrame(m3, index = matrix.index, columns = matrix.index)
df_similarity_categories = create_similarity_matrix_categories(df_utility_matrix)
def recommendations(business_id):
    hallo = dict()
    for i in df_similarity_categories:
        hallo[i] = df_similarity_categories[business_id][i]
    test = sorted(hallo, key=hallo.get, reverse=True)
    lijstje = []
    for i in test:
        for x in BUSINESSES['westlake']:
            if i == x['business_id']:
                lijstje.append(x)
    return lijstje

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
    return(recommendations('wTNWq7jrCZD1q2hSjUtTXg'))

recommend(None, 'wTNWq7jrCZD1q2hSjUtTXg')
