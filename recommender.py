from data import CITIES, BUSINESSES, USERS, REVIEWS, TIPS, CHECKINS

import random

piet = BUSINESSES['westlake']
for x in piet:
    print(x['name'])






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
<<<<<<< HEAD

    #poep



for i in BUSINESSES['sun city']:
    print(i['name']
=======
>>>>>>> 3e5e018fa590add07a9e8fd2c22db8b458a7dd1b
