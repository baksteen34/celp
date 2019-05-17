from data import CITIES, BUSINESSES, USERS, REVIEWS, TIPS, CHECKINS
from IPython.display import display
import random
import numpy as np
import ast
import pandas as pd
from collections import defaultdict

lijst = []

# filter door de BUSINESSES, haal geopende Restaurants eruit
for x in BUSINESSES['cleveland']:
    try:
        for j in x['categories'].split(','):
            if j == 'Restaurants':
                lijst.append(x)
    except:
        continue

    for j in lijst:
        if j['is_open'] == 0:
            lijst.remove(x)

# filter subcategorieen uit lijst
def filter(categorie, subcategorie, subcategorie2):
    data=dict()
    for i in lijst:
        try:
            test = i[categorie].get(subcategorie)
            test2 = i[categorie].get(subcategorie2)
            test = ast.literal_eval(test)
            test2 = ast.literal_eval(test2)
            #print(type(test))
            test4 = {**test, **test2}
            data[i['business_id']] = []
            for k,v in test4.items():
                if v == True:
                    data[i['business_id']].append(k)
        except:
            continue
    return data
filter("attributes", "Ambience", "GoodForMeal")
def filter2(categorie, subcategorie, subcategorie2, subcategorietje):
    hoi = filter(categorie, subcategorie, subcategorie2)
    for i in lijst:
        try:
            test = i[categorie].get(subcategorietje)
            if test == None:
                test = False
            if test == 'True':
                hoi[i['business_id']].append(subcategorietje)

        except:
            continue
    return hoi
    # maak dataframe gefilterd op subcategorie
def create_filter_dataframe(categorie, subcategorie, subcategorie2, subcategorietje):
    data = filter2(categorie,subcategorie, subcategorie2, subcategorietje)
    data2 = pd.Series(data)
    drie = data2.to_frame(subcategorie).reset_index()
    drie = drie.rename(columns = {'index' : 'business_id'})
    return(drie)

hallo = create_filter_dataframe('attributes', 'Ambience', 'GoodForMeal', 'HasTV')
print(hallo)
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

df_categories = extract_subcategories(create_filter_dataframe('attributes', 'Ambience', 'GoodForMeal', 'HasTV'))
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
    lijst3 = []
    for j in lijst:
        for i in df_similarity_categories:
            if j['business_id'] == i:
                lijst3.append(j)

    if business_id == None:
        return random.sample(lijst3, 10)

# input van random sample moet een lijst van restaurants zijn

    hallo = dict()
    for i in df_similarity_categories:
        if i == business_id:
            continue
        else:
            hallo[i] = df_similarity_categories[business_id][i]
    test = sorted(hallo, key=hallo.get, reverse=True)
    lijstje = []
    for i in test:
        for x in BUSINESSES['cleveland']:
            if i == x['business_id']:
                lijstje.append(x)

    for x in lijst:
        if x['business_id'] == business_id:
            for y, z in x['attributes'].items():
                if y == 'RestaurantsPriceRange2':
                    prijs = int(z)

    final = []
    for x in lijstje:
        for y, z in x['attributes'].items():
            if y == 'RestaurantsPriceRange2':
                if int(z) == prijs or int(z) == (prijs + 1) or int(z) == (prijs - 1):
                    final.append(x)

    final = final[0:10]

    return final

recommend(business_id='9IJ-TE4HEcAJQkUtc1A_Vw')

stars_dict = dict()
review_dict = dict()
def test(user_id):
    #for i in REVIEWS['cleveland']:
    #    stars_dict.append(i['stars'])
    #return stars_dict
#     for i in REVIEWS['brooklyn']:
#         review_dict[i['review_id']] = i['stars']
#
# #   for j in REVIEWS['brooklyn']:
# #        stars_dict[i['business_id']] = review_dict"
#     return review_dict
    for i in REVIEWS['cleveland']:
        if i['user_id'] == user_id:
            print(i['business_id'], i['stars'])
