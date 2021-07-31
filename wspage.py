# -- coding: utf-8 --
"""
Created on Fri Jul 30 17:55:09 2021
WebScrapping de los juegos olimpicos mediante la 
funente noticias de internet
https://olympics.com/tokyo-2020/es/
[]punto de scrapeo "sobre los juegos"
@author: aguil
"""

import requests
from pymongo import MongoClient
page = requests.get("https://olympics.com/tokyo-2020/es/")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
list_about = soup.find(class_="tk-nav-footer_list tk-nav-footer_list--about-the-games")
list_items = list_about.find(class_="tk-nav-footer__item")
About=[]

for iterator in list_items:
    list_link = list(iterator.find_all(class_="tk-nav-footer__link"))[0].get_text()    
    About.append(list_link.strip())
    
    
CLIENT = MongoClient('mongodb+srv://heroe:heroe@cluster0.wkxtx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = CLIENT['JuegosOlimpicos']
col = db['Temas']  

iterator_fly = 1

for iterator in About:
    print(iterator_fly)
    print(iterator)
    col.insert_one({
        "_id": iterator_fly,
        'Tema': iterator
        })
    iterator_fly = iterator_fly + 1

import pandas as pd


#Data Frame
import pandas as pd
weather = pd.DataFrame({About
})

weather.to_json('exampleData.json')
weather.to_json('exampleData.csv', delimiter="," )



# bson_file = open('courses.bson', 'rb')
# bson_data1 = bson.loads(bson_file.read())
# print(type(bson_data1))
# for data in bson_data1:
#     print(data)
    
#     print("code dataframe:")
# main_df=pd.DataFrame(bson_data1)
# print(main_df.describe() )