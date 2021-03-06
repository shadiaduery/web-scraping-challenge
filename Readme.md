Web-Scraping-Challenge: Mission to Mars 
By : Shadia Duery 
Date: 12/22/2020

Tools Used:
-Jupyter Notebook
-MongoDB
-Flask App

Following Libraries:
- import pandas as pd
- from pprint import pprint
- from splinter import Browser
- from bs4 import BeautifulSoup
- from selenium import webdriver
- from selenium.webdriver.chrome.options import Options
- import time

Background:
- The task requested was to scrape specific information from a designated website (NASA)
- The intention was to prove proficiency in finding elements on any website's html code
- The elements scrapped for this assigment were: A Title, A Paragraph, A Table, and Five images
- Store the scraped information on an online Database (MongoDB)
- Retrieve the stored information and render it into a newly design html landing page

Step 1: Scraping
Four landing web pages were provided to scrape the following information:
- The latest news title
- The latest news paragraph text
- JPL Featured Space Image
- A table with Mars data
- Mars Four Hemispheres Images

To complete this step a Jupyter Notebook was created and all the libraries mentioned above were imported in it.
All the requested information was saved as a dictionary and as a list to test which one would work better to import the information on the next steps

Step 2: MongoDB and Flask Application
All the code written to scrape the requested information done in a jupyter notebook was copy pasted to a .py file to be read in VS Code. The .py file had a scrape fuction to be called from another file if needed.

An app.py file was created to call the scrape fuction from the mars_scrape.py file, then code was written to create a connection to MongoDB, created  and stored the collection of scraped information to be later called and rendered into the previously created and styled index.html file.

The html file was styled using Bootstrap script. 

Once the index.html was fully running two screen shots picture were taken and stored on the Image folder of this repo to show the final product. 

_______________________________________________________________________________________________

# Web Scraping Homework - Mission to Mars

![mission_to_mars](Images/mission_to_mars.png)

In this assignment, you will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what you need to do.

### Before You Begin

1. Create a new repository for this project called `web-scraping-challenge`. **Do not add this homework to an existing repository**.

2. Clone the new repository to your computer.

3. You will add your notebook files to this repo as well as your flask app.

## Step 1 - Scraping

Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Create a Jupyter Notebook file called `mission_to_mars.ipynb` and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.

### NASA Mars News

* Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

### JPL Mars Space Images - Featured Image

* Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

* Make sure to find the image url to the full size `.jpg` image.

* Make sure to save a complete url string for this image.

```python
# Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
```

### Mars Facts

* Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Use Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

- - -

## Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data. The cleanest way is to just copy and paste code from a jupyter notebook into a `.py` file. (Jupyter has built in functionality to change the notebook into a python file, but I find that it doesn't always do what I want it to do.)

* Next, in an `app.py` file, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design. **As long as all the data is displayed, formatting and design are of secondary importance.** Reminder that in order to interact correctly with flask, this HTML file must live in the `templates` folder that is located in the same folder as your `app.py` file.

![final_app_part1.png](Images/final_app_part1.png)
![final_app_part2.png](Images/final_app_part2.png)

- - -

## Step 3 - Submission

To submit your work to BootCampSpot, ensure that your local repository contains the following:

1. The Jupyter Notebook containing the scraping code used.

2. All your `.py` and `.html` files.

3. Screenshots of your final application.

4. Regular commits (i.e. 20+ commits) and a thorough README.md file.

Push your final work to GitHub and then submit your repository link to BootCampSpot.

## Hints

* Use Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.

* Use Pymongo for CRUD applications for your database. For this homework, you can simply overwrite the existing document each time the `/scrape` url is visited and new data is obtained.

* Use Bootstrap to structure your HTML template.

### Copyright

Trilogy Education Services © 2020. All Rights Reserved.
