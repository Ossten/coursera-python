
from collections import OrderedDict
import os


here = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(here, 'restaurants.txt')
testifile = os.path.join(here, 'restaurants_test.txt')

# reading the file and building the  data structures
class Restaurant :
    ''' Restaurant
    '''
    def __init__(self, name, rating, price, cuisine):
        self.name = name
        self.rating = rating
        self.price = price
        self.cuisine = cuisine

    def __repr__(self):
        return "Restaurant()"

    def __str__(self):
        ''' (Restaurant) -> str
        >>> r1 = Restaurant('Chopsticks', '75%', '$$', ['Japanese', 'Thai', 'Chinese'])
        >>> r1.__str__()
        "Name: Chopsticks, rating: 75%, price: $$, cuisine: ['Japanese', 'Thai', 'Chinese']"
        '''
        return 'Name: {0}, rating: {1}, price: {2}, cuisine: {3}'.format(self.name, self.rating, self.price, self.cuisine)

def make_restaurant(name, rating, price, cuisine):
    r = Restaurant(name, rating, price, cuisine)
    return r

def read_file(file):
    """ (text file) -> Restaurant
    Readig the text file and populating a list of objects of a class Restaurant with the data that is parsed
    """
    data = []
    restaurant_list = []
    with open(file, 'r+') as f:  
        data = f.readlines()
        for i in range (0,len(data)):
            if ((i%5) == 0):
                name = data[i].rstrip()
                rating = data[i+1].rstrip()
                price = data[i+2].rstrip()
                cuisine = list(map(str.strip,(data[i+3].split(','))))
                # print (restaurant_list)
                restaurant_list.append(make_restaurant(name, rating, price, cuisine))
    return restaurant_list

def query_restaurant ():
    """
    Geting the restaurant name and rating by selecting the price range and the food type preffered from the console.
    """
    price = input('Select the requested price by typing in $, $$, $$$ or $$$$ :  ')
    restaurant_list = read_file(FILENAME)
    restaurant_list = sorted(restaurant_list, key = lambda Restaurant: Restaurant.rating, reverse = True)
    cuisine_list = []
    for i in range (0, len(restaurant_list)):
        # print(restaurant_list[i].name, restaurant_list[i].rating)
        if restaurant_list[i].price == price:
            for j in restaurant_list[i].cuisine:
                if j not in cuisine_list:
                    cuisine_list.append(j)
    # print (cuisine_list)
    print('Select the desired cuisine, in the selected pricerange, by typing it in ',cuisine_list,' :  ' )
    cuisine = input(' :  ' )
    for i in range (0, len(restaurant_list)):
        if restaurant_list[i].price == price and cuisine in cuisine_list and cuisine in restaurant_list[i].cuisine:
            print (restaurant_list[i].name, restaurant_list[i].rating)
            return(restaurant_list[i].name, restaurant_list[i].rating)

query_restaurant ()

if __name__ =='__main__':
    import doctest
    doctest.testmod()