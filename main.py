import re
import urllib.request
import sys
response = urllib.request.urlopen('http://example.webscraping.com/places/default/view/India-102')
html = response.read()
text = html.decode()
re.findall('<td class="w2p_fw">(.*?)</td>',text)
sys.stdout = open("test.txt","w")
print(text)
sys.stdout.close()

