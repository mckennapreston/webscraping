
from cgi import print_exception
from traceback import print_tb
from unicodedata import name
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from twilio.rest import Client
import twilio 

URL = 'https://www.livecoinwatch.com/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(URL, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')



CryptoTable = soup.find('table')

CryptoRows = CryptoTable.findAll('tr')

print()
print('The Top 5 Cryptocurrency Companies')

for x in range(1,6):
    td = CryptoRows[x].findAll('td')
    num = td[0].text
    name = td[1].text
    CurrentPrice = float(td[2].text.strip('$'))
    PercentChange = float(td[8].text.strip('%'))

    print()
    print('Ranking:', num)
    print('Name:', name)

    Current_Price = "${:,.2f}".format(CurrentPrice)
    print('Current Price:', Current_Price)

    print("Percent Change:",PercentChange, "%")
    Change = round((CurrentPrice)/(1+(PercentChange/100)),2)
    ChangeFormat = "${:,.2f}".format(Change)
    print("Price based on % change:", ChangeFormat)
    print()


AccountSID = 'AC2c3432f82ecd5ef9188c3871dc5e49ab'
AuthToken = 'b44e0be023e5c5e1c7396f40a81a4ed1'
client = Client(AccountSID, AuthToken)
TwilioNumber = '+12566678523'
MyNumber = '+17133519799'


if "Bitcoin" in name and CurrentPrice < 40000:
        BitcoinText = client.messages.create(to = MyNumber, from_= TwilioNumber, body = "Bitcoin value has fallen below $40,000")
if "Ethereum" in name and CurrentPrice < 3000: 
        Ethereum_phonetext = client.messages.create(to = MyNumber, from_= TwilioNumber, body = "Ethereum value has fallen below $3,000")

