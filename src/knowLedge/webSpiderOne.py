
from urllib.request import urlopen
from bs4 import BeautifulSoup


openUrl = "http://jr.jd.com"
html = urlopen(openUrl)
bsObject = BeautifulSoup(html.read(), 'html.parser')

testList = bsObject.find_all("a", "nav-item-primary")

for text in testList:
    print(text.get_text())




html.close()