#!/usr/bin/env python3

import requests
import time
from bs4 import BeautifulSoup
import os 
import json

# This script uses my user-agent header as the ID

user_agent = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/123.0.6312.86 Chrome/123.0.6312.86 Safari/537.36",
              "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
              "Accept-Language": "en-AU,en;q=0.9,en-GB;q=0.8",
              "Accept-Encoding": "gzip, deflate, br",
              "DNT": "1",
              "Connection": "keep-alive",
              "Sec-Fetch-Dest": "document",
              "Sec-Fetch-Mode": "navigate",
              "Sec-Fetch-Site": "same-origin",
              "Sec-Fetch-User": "?1",
              "Upgrade-Insecure-Requests": "1"
    }

# Capturing the website cookies from the website's server with session variable
session = requests.session()
session.headers.update(user_agent)

url = 'https://driveinstyle.com.au/stock-list'

# cookies is the data structure.. which will store the cookies so that we can perform operations like save, update to a file
cookies = {}

# os.path.exists is checking the file 'cookies.json' if it exists, it will load the cookies into the script for use
# This file will only exists if we ever ran this script in the past at least once
if os.path.exists('cookies.json'):
    with open('cookies.json', 'r') as f:
        reuse_cookies = json.load(f)
        session.cookies.update(reuse_cookies)

# Fetching the website from the internet with error handling

try:
    response = session.get(url, timeout=60) # Attempting a GET request to the server
    response.raise_for_status()
    print('Page has been successfully grabbed from the server! Response Code:', response.status_code, '| URL:', url)
    print('Response Header Information:\n')
    for x, y in response.headers.items():   # Checking the response that we got from our GET request
        print(f'{x}: {y}')
    print('Initiating 10 second countdown... | > Script is complying with the rules of the the Server!') # Complying with robots.txt file 
    time.sleep(10)
    
    # The code below is the cookie system
    print('Cookies assigned to us:\n')
    
    for x, y in session.cookies.items():
        print(f'{x}: {y}')
        time.sleep(2)
        print('\n')
        cookies[x] = y
    
    # Creating or overwriting the cookie file depending on if it exists or not in our main script folder
    with open('cookies.json', 'w') as f:
        json.dump(cookies, f, indent=4)


except requests.exceptions.HTTPError as e:
    print('A problem has occured while fetching the page!', e)

# Transforming the data gathered from above into a Document Object Model(DOM) so that we can use it inside our python script!

try:
    soup = BeautifulSoup(response.text, 'lxml')
    print('The fetched website (', url, ') has been successfully parsed!')
    #print(soup)
except Exception as e:
    print('There is a problem that has occured in parsing! Error cause:', e)

print('\n')
print('Inventory List:')
print('\n')

# Now we are gonna extract the information from the DOM that we made above
# and save all cars information in cars_list variable

cars_list = []

# Info_container is responsible for finding all the information about cars in the inventory (at the dealership)
info_container = soup.find_all('ul', class_='list-group list-space')
print('Current Cars in Stock:', len(info_container))    # Checking the total number of cars in the inventory

for x in info_container:    # Finding the details about the car and saving it as a dictionary
    current_car = {}    # This is that dictionary

    name = x.find('h2', class_='vy-title-block').text   # This is the name of the car
    current_car['Name'] = name.strip()

    add_info = x.find('ul')

    li_tags = add_info.find_all('li')
    info_1 = li_tags[0].text    # The type of the car
    current_car['Type'] = info_1.strip()

    info_2 = li_tags[1].text    # The gearbox of the car
    current_car['Gearbox'] = info_2.strip()

    add_info_2 = add_info.find_next_sibling()

    li_tags_2 = add_info_2.find_all('li')

    info_3 = li_tags_2[0].text      # How many kms the car is currently driven
    current_car['Driven'] = info_3.strip()

    info_4 = li_tags_2[1].text      # What kind of fuel does the car use
    current_car['Fuel Type'] = info_4.strip()

    price = x.find('span', class_='vy-price').text
    current_car['Price'] = price.strip()    # The price of the car

    cars_list.append(current_car)   # Pushing the current_car dictionary to the cars_list variable

for x in cars_list:
    print(x)    # Printing the data into the console
