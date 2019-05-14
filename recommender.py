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
display(drie)

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
