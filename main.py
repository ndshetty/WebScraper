#import re
#import urllib.request
# response = urllib.request.urlopen('http://example.webscraping.com/places/default/view/India-102')
# html = response.read()
# text = html.decode()
# re.findall('<td class="w2p_fw">(.*?)</td>',text)
# sys.stdout = open("test.txt","w")
# print(text)
# sys.stdout.close()

#from bs4 import BeautifulSoup
#page = requests.get(" https://data.ontario.ca/dataset/f4112442-bdc8-45d2-be3c-12efae72fb27/resource/455fd63b-603d-4608-8216-7d8647f43350/download/conposco")
#page.status_code
#print(page.status_code)
#page.content
#soup = BeautifulSoup(page.content, 'html.parser')
#sys.stdout = open("test.txt","w")
#print(soup.prettify())
#sys.stdout.close()

#import requests
#import sys
#import seaborn as sns
#import csv


import pandas as pd
import numpy as py
import pymysql
import sqlalchemy
import mysql.connector


url = 'https://en.wikipedia.org/wiki/History_of_Python'
dfs = pd.read_html(url)
df = dfs[0]
df2 = df[['Version', 'Release date']]
#print(df2)

database_username = 'root'
database_password = 'Nihass22!!'
database_ip = '127.0.0.1'
database_name = 'ONCovid19'
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'. format(database_username, database_password, database_ip, database_name))

df2.to_sql(con=database_connection, name='test', if_exists='replace')

#conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Nihass22!!', db='ONCovid19')
#cur = conn.curson()

#cur.execute("USE ONCovid19")
#cur.execute("SELECT ")

