from urllib.request import urlopen
 
optionsUrl = 'http://finance.yahoo.com/q/op?s=AAPL+Options'
optionsPage = urlopen(optionsUrl)

from bs4 import BeautifulSoup
soup = BeautifulSoup(optionsPage)

# soup.findAll(text='AAPL130328C00350000')[0].parent.parent.parent

optionsTable = [
    [x.text for x in y.parent.contents]
    for y in soup.findAll('td', attrs={'class': 'yfnc_h', 'nowrap': ''})
]
