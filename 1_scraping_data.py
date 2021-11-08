from bs4 import BeautifulSoup
from requests import get
import sqlite3
from sys import argv


######################################
# Defining the database
######################################

#Database creation for table 'olx_offers'
database = sqlite3.connect('database/database_olx.db')
cursor = database.cursor()

if len(argv) > 1 and argv[1] == 'setup':
    cursor.execute('''CREATE TABLE offers (title TEXT, price REAL, city TEXT, link TEXT)''') 
    quit()

######################################
# Scrapping the data from olx.pl
######################################

# set url to extract data
url = 'https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/mazowieckie/'

# function to clean the price string scrapped from the website
def parse_price(price):
    return float(price.replace(' ', '').replace('zł', '').replace(',', '.'))

def parse_page(number):
    print(f'Scrapping page number {number}.')
    response = get(f'{url}?page={number}') # to URL we add &page={number} so that it can iterate
    soup = BeautifulSoup(response.content, 'html.parser')
    offers = soup.find_all('div', class_ = 'offer-wrapper')
    # extraction of data for multiple offers
    for offer in offers:
        # definition of the place where the data will be taken
        footer = offer.find('td', class_ = 'bottom-cell')
        # extraction of location
        location = footer.find('small', class_='breadcrumb').get_text().strip().split(',')[0] # takes the city instead of a town
        # extraction of title of the offer
        title = offer.find('strong').get_text().strip()
        # extraction of price
        price = parse_price(offer.find('p', class_ = 'price').get_text().strip())
        # extraction of link
        link = offer.find('a')['href'] # extracts link
        # Insert values into the database
        cursor.execute('INSERT INTO offers VALUES (?, ?, ?, ?)', (title, price, location, link))
        database.commit()
        

######################################
# Run script and save data in the SQLite database 
######################################

last_page = 25

for page in range(1,last_page):
    parse_page(page)
    
database.close()