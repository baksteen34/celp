from data import CITIES, BUSINESSES, USERS, REVIEWS, TIPS, CHECKINS
from IPython.display import display
import random
import numpy as np
import ast
import pandas as pd

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
def filter(categorie, subcategorie):
    data=dict()
    for i in lijst:
        test = i[categorie].get(subcategorie)
        test = ast.literal_eval(test)
        print(test)
    while test == True:
        data[i['business_id']] = test
    return data
filter('attributes','HasTV')


#lK-wuiq8b1TuU7bfbQZgsg
