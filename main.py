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

import pandas as pd
#import csv

url = 'https://www.basketball-reference.com/leagues/NBA_2019_per_game.html'

df = pd.read_html(url, header = 0)
df

