from data import CITIES, BUSINESSES, USERS, REVIEWS, TIPS, CHECKINS
from IPython.display import display
import random
import numpy as np
import ast
import pandas as pd
from collections import defaultdict

#subcategorieën = ['ByAppointmentOnly', 'BusinessAcceptsCreditCards', 'GoodForKids', 'RestaurantsReservations', 'HasTV', 'RestaurantsTakeOut', 'OutdoorSeating', 'RestaurantsGoodForGroups', 'RestaurantsDelivery', 'BikeParking', 'Caters', 'LateNight',
#'BusinessAcceptsBitcoin', 'WheelchairAccessible', 'HappyHour', 'CoatCheck']

#dict_subcategorieën: ['Music', 'Ambience', 'BusinessParking', 'GoodForMeal']

lijst = []
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

def filter(categorie, subcategorie, subcategorie2, subcategorie3, subcategorie4, subcategorietje, subcategorietje2, subcategorietje3, subcategorietje4, subcategorietje5, subcategorietje6, subcategorietje7, subcategorietje8, subcategorietje9, subcategorietje10, subcategorietje11, subcategorietje12, subcategorietje13, subcategorietje14, subcategorietje15, subcategorietje16):
    data=dict()
    for i in lijst:
        try:
            test = i[categorie].get(subcategorie)
            test2 = i[categorie].get(subcategorie2)
            test3 = i[categorie].get(subcategorie3)
            test4 = i[categorie].get(subcategorie4)
            test = ast.literal_eval(test)
            test2 = ast.literal_eval(test2)
            test3 = ast.literal_eval(test3)
            test4 = ast.literal_eval(test4)
            test5 = {**test, **test2, **test3, **test4}
            data[i['business_id']] = []
            for k,v in test5.items():
                if v == True:
                    data[i['business_id']].append(k)
        except:
            continue
    return data
    filter('attributes','Music', 'Ambience', 'BusinessParking', 'GoodForMeal')

def filter2(categorie, subcategorie, subcategorie2, subcategorie3, subcategorie4, subcategorietje, subcategorietje2, subcategorietje3, subcategorietje4, subcategorietje5, subcategorietje6, subcategorietje7, subcategorietje8, subcategorietje9, subcategorietje10, subcategorietje11, subcategorietje12, subcategorietje13, subcategorietje14, subcategorietje15, subcategorietje16):
    subcategorietjeslijst = [subcategorietje, subcategorietje2, subcategorietje3, subcategorietje4, subcategorietje5, subcategorietje6, subcategorietje7, subcategorietje8, subcategorietje9, subcategorietje10, subcategorietje11, subcategorietje12, subcategorietje13, subcategorietje14, subcategorietje15, subcategorietje16]
    hoi = filter(categorie, subcategorie, subcategorie2, subcategorie3, subcategorie4, subcategorietje, subcategorietje2, subcategorietje3, subcategorietje4, subcategorietje5, subcategorietje6, subcategorietje7, subcategorietje8, subcategorietje9, subcategorietje10, subcategorietje11, subcategorietje12, subcategorietje13, subcategorietje14, subcategorietje15, subcategorietje16)
    for i in lijst:
        try:
            test = i[categorie].get(subcategorietje)
            test2 = i[categorie].get(subcategorietje2)
            test3 = i[categorie].get(subcategorietje3)
            test4 = i[categorie].get(subcategorietje4)
            test5 = i[categorie].get(subcategorietje5)
            test6 = i[categorie].get(subcategorietje6)
            test7 = i[categorie].get(subcategorietje7)
            test8 = i[categorie].get(subcategorietje8)
            test9 = i[categorie].get(subcategorietje9)
            test10 = i[categorie].get(subcategorietje10)
            test11 = i[categorie].get(subcategorietje11)
            test12 = i[categorie].get(subcategorietje12)
            test13 = i[categorie].get(subcategorietje13)
            test14 = i[categorie].get(subcategorietje14)
            test15 = i[categorie].get(subcategorietje15)
            test16 = i[categorie].get(subcategorietje16)
            # test17 = {**test, **test2, **test3, **test4, **test5, **test6, **test7, **test8, **test9, **test10, **test11, **test12, **test13, **test14, **test15, **test16}
            if test == None:
                test = False
            if test == 'True':
                hoi[i['business_id']].append(subcategorietje)
            if test2 == None:
                test2 = False
            if test2 == 'True':
                hoi[i['business_id']].append(subcategorietje2)
            if test3 == None:
                test3 = False
            if test3 == 'True':
                hoi[i['business_id']].append(subcategorietje3)
            if test4 == None:
                test4 = False
            if test4 == 'True':
                hoi[i['business_id']].append(subcategorietje4)
            if test5 == None:
                test5 = False
            if test5 == 'True':
                hoi[i['business_id']].append(subcategorietje5)
            if test6 == None:
                test6 = False
            if test6 == 'True':
                hoi[i['business_id']].append(subcategorietje6)
            if test7 == None:
                test7 = False
            if test7 == 'True':
                hoi[i['business_id']].append(subcategorietje7)
            if test8 == None:
                test8 = False
            if test8 == 'True':
                hoi[i['business_id']].append(subcategorietje8)
            if test9 == None:
                test9 = False
            if test9 == 'True':
                hoi[i['business_id']].append(subcategorietje9)
            if test10 == None:
                test10 = False
            if test10 == 'True':
                hoi[i['business_id']].append(subcategorietje10)
            if test11 == None:
                test11 = False
            if test11 == 'True':
                hoi[i['business_id']].append(subcategorietje11)
            if test12 == None:
                test12 = False
            if test12 == 'True':
                hoi[i['business_id']].append(subcategorietje12)
            if test13 == None:
                test13 = False
            if test13 == 'True':
                hoi[i['business_id']].append(subcategorietje13)
            if test14 == None:
                test14 = False
            if test14 == 'True':
                hoi[i['business_id']].append(subcategorietje14)
            if test15 == None:
                test15 = False
            if test15 == 'True':
                hoi[i['business_id']].append(subcategorietje15)
            if test16 == None:
                test16 = False
            if test16 == 'True':
                hoi[i['business_id']].append(subcategorietje16)
        except:
            continue
    print(hoi)
    return hoi
    filter2('attributes','Music', 'Ambience', 'BusinessParking', 'GoodForMeal', 'ByAppointmentOnly', 'BusinessAcceptsCreditCards', 'GoodForKids', 'RestaurantsReservations', 'HasTV', 'RestaurantsTakeOut', 'OutdoorSeating', 'RestaurantsGoodForGroups', 'RestaurantsDelivery', 'BikeParking', 'Caters', 'LateNight',
    'BusinessAcceptsBitcoin', 'WheelchairAccessible', 'HappyHour', 'CoatCheck')


def create_filter_dataframe(categorie, subcategorie, subcategorie2, subcategorie3, subcategorie4, subcategorietje, subcategorietje2, subcategorietje3, subcategorietje4, subcategorietje5, subcategorietje6, subcategorietje7, subcategorietje8, subcategorietje9, subcategorietje10, subcategorietje11, subcategorietje12, subcategorietje13, subcategorietje14, subcategorietje15, subcategorietje16):
    data = filter2(categorie, subcategorie, subcategorie2, subcategorie3, subcategorie4, subcategorietje, subcategorietje2, subcategorietje3, subcategorietje4, subcategorietje5, subcategorietje6, subcategorietje7, subcategorietje8, subcategorietje9, subcategorietje10, subcategorietje11, subcategorietje12, subcategorietje13, subcategorietje14, subcategorietje15, subcategorietje16)
    data2 = pd.Series(data)
    drie = data2.to_frame(subcategorie).reset_index()
    drie = drie.rename(columns = {'index' : 'business_id'})
    return(drie)

hallo = create_filter_dataframe('attributes','Music', 'Ambience', 'BusinessParking', 'GoodForMeal', 'ByAppointmentOnly', 'BusinessAcceptsCreditCards', 'GoodForKids', 'RestaurantsReservations', 'HasTV', 'RestaurantsTakeOut', 'OutdoorSeating', 'RestaurantsGoodForGroups', 'RestaurantsDelivery', 'BikeParking', 'Caters', 'LateNight',
'BusinessAcceptsBitcoin', 'WheelchairAccessible', 'HappyHour', 'CoatCheck')

def extract_subcategories(categorie):
    """Creates a utility matrix for subcategories
    Arguments:
    df -- a dataFrame containing at least the columns 'business_id' and 'subcategorie'
    Output:
    a matrix containing a rating in each cell
    """
    categorie_m = categorie.apply(lambda row: pd.Series([row['business_id']] + row['Music']), axis=1)
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

df_categories = extract_subcategories(create_filter_dataframe('attributes','Music', 'Ambience', 'BusinessParking', 'GoodForMeal','ByAppointmentOnly', 'BusinessAcceptsCreditCards', 'GoodForKids', 'RestaurantsReservations', 'HasTV', 'RestaurantsTakeOut', 'OutdoorSeating', 'RestaurantsGoodForGroups', 'RestaurantsDelivery', 'BikeParking', 'Caters', 'LateNight',
'BusinessAcceptsBitcoin', 'WheelchairAccessible', 'HappyHour', 'CoatCheck'))
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
print(df_utility_matrix)
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

def test(user_id, business_id):
    for i in REVIEWS['cleveland']:
        if i['user_id'] == user_id:
            if i['business_id'] == business_id:
                aangeklikt = int(i['stars'])
                print("Aangeklikt =", aangeklikt)

    gemiddeld_10 = 0
    teller = 0
    for i in recommend(business_id=business_id):
        for j in REVIEWS['cleveland']:
            if j['business_id'] == i['business_id']:
                if j['user_id'] == user_id:
                    gemiddeld_10 += int(j['stars'])
                    teller += 1

    if teller == 0:
        print("Geen ratings van de top10 gevonden door deze user")
    else:
        afwijking = round(aangeklikt - (gemiddeld_10/teller), 2)
        print("Aantal gereviewde restaurants uit de top10 door deze user=", teller)
        print("De gemiddelde afwijking van de aangeklikte vergeleken met ratings van dezelfde user =", afwijking)

    willekeurig = 0
    for i in range(10):
        willekeurig += int(random.choice(lijst)['stars'])
    afwijking2 = round(aangeklikt - (willekeurig/10), 2)
    print("De gemiddelde afwijking van de aangeklikte vergeleken met willekeurige ratings =", afwijking2)

reviews_lijst = []
reviews = dict()

for review in REVIEWS['cleveland']:
     business_id = review['business_id']
     for bedrijf in lijst:
         if bedrijf['business_id'] == business_id:
             try:
                 business_id = bedrijf['business_id']
                 user_id = review['user_id']
                 test(user_id, business_id)
             except:
                 continue 


#test('XsKL7KGNXL1r_YTxXuUWkA', '9IJ-TE4HEcAJQkUtc1A_Vw')
