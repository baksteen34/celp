from data import CITIES, BUSINESSES, USERS, REVIEWS, TIPS, CHECKINS

import random
henk = 'Restaurants'
piet = BUSINESSES['westlake']
for x in piet:
<<<<<<< HEAD
    henk = x['categories']
    for y in henk:
        print(y)
=======
    hallo = x['categories']
    test = hallo.split(',')
    for j in test:
        print(j)

>>>>>>> ebdf7a71ccd7dc4461a3f2fdcf51f32411c009d2




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
