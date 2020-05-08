# file -> (dict,dict,dict)

import ast
import re
from collections import OrderedDict
import os

here = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(here, 'restaurants_small.txt')

# reading the file and building the  data structures

def read_restaurant(file):
    """(file) -> (dict,dict,dict)
        Return a tuple of dictionaries based on the information in the file
        name_to_rating = {}
        price_to_names = {'$':[], '$$':[],'$$$':[], '$$$$':[]}
        cuisine_to_names = {}
    """
    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}
    cuisine_name = []
    data = []
    cn = []
    d1=d2={}
    with open(file, 'r+') as f:                                         # reading the file
        data = f.readlines()
        for i in range(0, len(data)):
            if ((i % 5) == 0):                                          # gets every fifth line of the file not counting empty lines
                name_rating = {data[i].rstrip(): data[i+1].rstrip()}    # every 4th and 5th line is put in to key-value pair
                name_to_rating.update(name_rating)                      # every key-value pair is updated in the dictionary
                if ',' in data[i+3]:
                    s = data[i+3].split(', ')
                    s = list(map(str.strip,s))
                    for j,el in enumerate(s):
                        cn = {s[j]:[data[i].rstrip()]}
                        d1 = {k:list(set().union(d1.get(k, []),cn.get(k, [])))  for k in  (d1.keys()|cn.keys())}
                else:                                           
                    cuisine_name = {data[i+3].rstrip(): [data[i].rstrip()]}
                    d2.update(cuisine_name)
                for key in price_to_names:
                    if key == data[i+2].rstrip():
                        price_to_names[key].append(data[i].rstrip())
    d1={k: v if isinstance(v , list) else [v] for k,v in d1.items()}
    d2={k: v if isinstance(v , list) else [v] for k,v in d2.items()}           
    cuisine_to_names = {k:list(set().union(d1.get(k, []),d2.get(k, [])))  for k in  (d1.keys()|d2.keys())}
    return name_to_rating, price_to_names, cuisine_to_names

name_to_rating, price_to_names, cuisine_to_names = read_restaurant(FILENAME)

    #print("name_to_rating = ",name_to_rating)
    #print("price_to_names = ",price_to_names)
    #print("cuisine_to_names = ",cuisine_to_names)
#---------------------------------------------------------------------------------
def by_price():
    price = input('Select the requested price by typing in $, $$, $$$ or $$$$ :  ')
    return price_to_names.get(price)
#---------------------------------------------------------------------------------    
def by_price_and_cusine():
    l = by_price()
    l1 = []
    z ={}
    for el in l:
        x = cuisine_to_names
        z = dict(cuisine_to_names)
        for k, v in x.items():
            if el in v:
                if (list(z.keys())[list(z.values()).index(v)]) not in l1:
                    l1.append(list(z.keys())[list(z.values()).index(v)])
                    z.pop(k)
    print('Select the desired cuisine by typing it in ',l1,' :  ' )
    cuisine = input(' :  ' )
    return cuisine_to_names.get(cuisine), l
    
#---------------------------------------------------------------------------------
def get_ratings():
    a, l = by_price_and_cusine()
    b = dict({k: v for k, v in sorted(name_to_rating.items(), key=lambda item: item[1], reverse = True)})
    print (b)
    for element in b:
        if element in a and element in l:
            print (b.get(element), element)


get_ratings()
