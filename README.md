# Inventory Monitor

This project is an automated script which pulls the website from the internet and extracts the data from a car dealer website.

### Before using the script

> My advice still here is to use the script once and wait for like 5 to 10 minutes if you want the updated data! The data is also getting saved to an excel file (and files) so I highly doubt that, someone will need to run the script multiple times!

> Also, please make sure to delete the cookie files if you want to re-run the script the next day - by doing this, your IP won't get flagged and your script won't be redirected to the captcha page!

> If the script isn't pulling the data - that means that you probably got redirected to the captcha page even if the header response is 200 so do keep this in mind!

### Benefits

What's the need of extracting information from a website? 

This data can be used for various purposes including: 

* Checking the total number of cars in the inventory of the dealer

* Information like: the name of the car, what kind of car is it, is it automatic or manual, how many kms the car is currently driven, what kind of fuel does it drink and the price of the car - can be accessed with this script!

* The features of this script aren't just limited to just access the information available from the website! You can also use this script to create an excel file or a csv file or even a database in theory if we want to.

* This datapipe can increase the speed tremendously if the dealership decides ever to create an app for the smartphone!

### My motives

So, why am I doing this?

I am interested in the craft of web scraping and I am doing it simply for learning purposes. 

### Safety Guidelines

This script is following the website rules and regulations provided by the website owner at robots.txt file - specifically made for bots and this script is only accessing the public information available on this website!

   > **Guidelines were last checked on the date of April 4, 2026** 

   > **This repo isn't made with ill intentions! If anyone has any problem regarding this repo, please feel free to contact me.**

### Highlights

   > Using User-agents so that script doesn't get suspected as a BOT or a script

   > Using requests.session() for creating a session like a browser

   > Storing and reusing cookies so that we can consistently make multiple requests | Normally the script was getting redirected to the captcha page

### Tech Stack

The tools I use: 

* Python Requests library - for fetching the website from the internet.

* beautifulSoup4 - for creating a DOM(Document-Object Model) of the fetched website, so that I can use it with python for tasks like:

    > Data Extraction: Out of the entire site that we just pulled, we usually wanted selected information and not the entire page.

    > Data Cleaning: The selected information might have have things like unwanted spacing, bullets etc. This website does have random bullets and spaces but I cleaned them and you can actually check the final output of the file!

* lxml: Normally, beautifulSoup uses html.parser which is written in python and is noticably slow in HTML to DOM conversion! lxml is written in C entirely so it solves the speed problem!

* time library: I use time to initiate a wait counter so that the script stops for few minutes and waits for the execution. It waits until the timer is expired so that we don't accidently do a DDoS attack on a website. 

    > If I explain it simply, too many requests can slow the performance of the server running the website on the internet!

    > This wait can also be used to simulate a click done by an actual human. So, in the eyes of the server, it will look like an actual human rather than a bot or a script. But, this was just one page crawl and scrape so for this one I definitely didn't need to this!

* pandas: The job of pandas library was simple! The selected and cleaned information gathered by the script which we need, we push it to an Excel file or a .csv file or even a .json file. We will have a clean file with all the information extracted and cleaned - ready for use! You can check the excel file right here: 

   [Preview of the Excel File](https://www.dropbox.com/scl/fi/qpkoe0lfmlkan2u8r6hpk/Inventory_listings.xlsx?rlkey=98q2ib4n7biamaxavgpvkzefx&st=6bro8z2x&dl=0) | [Direct Download](https://www.dropbox.com/scl/fi/qpkoe0lfmlkan2u8r6hpk/Inventory_listings.xlsx?rlkey=98q2ib4n7biamaxavgpvkzefx&st=6bro8z2x&dl=1)

### Version Log:

* Version 1.0: Inventory Monitor (Major release)

    - The script can only show a total number of cars currently available on the website.

* Version 2.0: Inventory Monitor (Major release)
    
    - The script is now capable of showing details about every single car currently sitting at the inventory of the website.

* Version 2.1: Inventory Monitor (Update)
    
    - Before: It was printing the nested dictionaries stored inside the list. Entire console was getting filled with nested dictionaries.
                
      Bullets and unwanted spaces were present inside the dictionaries.

    - After: The script is only showing the details like: Name, Type, Gearbox, Fuel Type, Driven, Price of the car.

      The bullets and unwanted spaces got removed from the dictionary! Only the cleaned information about the car is showing up.

* Version 3.1: Inventory Monitor (Major release)

    - Added the capability of creating the .xlsx, .json, .csv files and then, adding the cleaned extracted infomation into the files!
