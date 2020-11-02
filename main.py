#import re
import requests
#import urllib.request
import sys
# response = urllib.request.urlopen('http://example.webscraping.com/places/default/view/India-102')
# html = response.read()
# text = html.decode()
# re.findall('<td class="w2p_fw">(.*?)</td>',text)
# sys.stdout = open("test.txt","w")
# print(text)
# sys.stdout.close()
from bs4 import BeautifulSoup
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page.status_code
print(page.status_code)
page.content
soup = BeautifulSoup(page.content, 'html.parser')
sys.stdout = open("test.txt","w")
print(soup.prettify())
sys.stdout.close()
