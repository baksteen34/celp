from data import CITIES, BUSINESSES, USERS, REVIEWS, TIPS, CHECKINS

import random
henk = 'Restaurants'
piet = BUSINESSES['westlake']
for x in piet:
    henk = x['categories']
    for y in henk:
        print(y)




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
