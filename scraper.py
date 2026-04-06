#!/usr/bin/env python3

import requests
import time
from bs4 import BeautifulSoup

# This script uses my user-agent header as the ID

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/'
}

url = 'https://driveinstyle.com.au/stock-list'

# Fetching the website from the internet with error handling

try:
    response = requests.get(url, headers=user_agent, timeout=60)
    response.raise_for_status()
    print('Page has been successfully grabbed from the server! Response Code:', response.status_code, '| URL:', url)
    time.sleep(10)
except requests.exceptions.HTTPError as e:
    print('A problem has occured while fetching the page!', e)

# Transforming the data gathered from above into a Document Object Model(DOM) so that we can use it inside our python script! 

try:
    soup = BeautifulSoup(response.text, 'lxml')
    print('The fetched website (', url, ') has been successfully parsed!')
    #print(soup)
except Exception as e:
    print('There is a problem that has occured in parsing! Error cause:', e)

# The code given below shows inventory numbers that our code thinks should be present on the actual site!
# All 4 numbers should be similar (i.e the Cars, Cars name, Cars Price Tag and Cars Info)
# In case these aren't similar then it should be concluded that data given to us by the script is inaccurate!

cars = soup.find_all('div', class_='vy-item-wrapper')
print('Cars:', len(cars)) # Car's Placeholder Tag
cars_name = soup.find_all('h2', class_='vy-title-block')
print('Cars name:', len(cars_name)) # Car's Name Tag
cars_price_tag = soup.find_all('div', class_='col vy-price-block')
print('Cars Price Tag:', len(cars_price_tag)) # Car's Price Tag
cars_price = soup.find_all('span', class_='vy-price')
cars_info = soup.find_all('li', class_='list-group-item icons')
print('Cars Info:', len(cars_info)) # Car's Additional Info Tag




