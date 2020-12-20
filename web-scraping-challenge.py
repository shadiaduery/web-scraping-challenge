# Import Dependencies
import requests
import pandas as pd
from pprint import pprint
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Create a browser instance using splinter
executable_path = {"executable_path":"C:/Users/sduer/Desktop/chromedriver"}
browser=Browser("chrome", **executable_path, headless=False)

### Scraping NASA Mars News
# URL of page to be scraped
mars_news_url = "https://mars.nasa.gov/news/"
browser.visit(mars_news_url)
time.sleep(2)

# Object Oriented Programming, create an HTML object
html = browser.html

# Parse the HTML object using the BeautifulSoup Method
soup=BeautifulSoup(browser.html, 'html.parser')

# Find a html component that contains a news title and the news paragraph
element = soup.find('li', class_='slide')

# Create an empty dictionary
mars_news={}

# Parse the News Title from the website
mars_news['news_title'] = element.find('div', class_='content_title').find('a').text

# Parse the News Paragraph from the website
mars_news['news_p'] = element.find('div', class_='rollover_description_inner').text

### JPL Mars Space Images - Featured Image
# URL of page to be scraped
feature_img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(feature_img_url)
time.sleep(2)

# Object Oriented Programming, create an HTML object
html = browser.html

# Parse the HTML object using the BeautifulSoup Method
soup=BeautifulSoup(browser.html, 'html.parser')

# Find a html component that contains featured image high resolution
featured_img = soup.find('article',class_='carousel_item')['style']

featured_img = feature_img_url + (featured_img[23:75])

# Mars Facts
# URL of page to be scraped
mars_facts_url = "https://space-facts.com/mars/"
browser.visit(mars_facts_url)
time.sleep(3)

# Object Oriented Programming, create an HTML object
html = browser.html

# Parse the HTML object using the BeautifulSoup Method
soup=BeautifulSoup(browser.html, 'html.parser')

# Find a html component that contains Mars Facts Table
mars_fact_table_extract = soup.find('table', class_='tablepress tablepress-id-p-mars')

mars_fact_table_extract = pd.read_html(html)
mars_fact_table_df = mars_fact_table_extract[0]
mars_fact_table_df.columns = ['Description', 'Value']
mars_fact_table = mars_fact_table_df.to_html(buf=None, columns=None, col_space=None, header=True, index=False, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, bold_rows=True, classes=None, escape=True, max_rows=None, max_cols=None, show_dimensions=False, notebook=False, decimal='.', border=None, table_id=None)

### Mars Hemispheres
# URL of page to be scraped
mars_cerberus_hemisphere_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
browser.visit(mars_cerberus_hemisphere_url)
time.sleep(3)

# Object Oriented Programming, create an HTML object
html = browser.html

# Parse the HTML object using the BeautifulSoup Method
soup=BeautifulSoup(browser.html, 'html.parser')

# Create an empty dictionary and variables
cerberus={}

# Find a html title and image url to Mars Cerberus Hemisphere 
cerberus['title'] = soup.find('h2', class_='title').text
cerberus['image_url'] = soup.find('div', class_='downloads').find('a')["href"]

# URL of page to be scraped
mars_schiaparelli_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
browser.visit(mars_schiaparelli_url)
time.sleep(3)

# Create an empty dictionary
chiaparelli={}

# Find a html title and image url to Mars schiaparelli Hemisphere
chiaparelli['title'] = soup.find('h2', class_='title').text
chiaparelli['image_url'] = soup.find('div', class_='downloads').find('a')["href"]

# URL of page to be scraped
mars_syrtis_major_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
browser.visit(mars_syrtis_major_url)
time.sleep(3)

# Create an empty dictionary
syrtis={}

syrtis['title'] = soup.find('h2', class_='title').text
syrtis['image_url'] = soup.find('div', class_='downloads').find('a')["href"]

# URL of page to be scraped
mars_valles_marineris_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
browser.visit(mars_valles_marineris_url)
time.sleep(3)

# Create an empty dictionary
valles={}

# Find a html title and image url to Mars schiaparelli Hemisphere
valles['title'] = soup.find('h2', class_='title').text
valles['image_url'] = soup.find('div', class_='downloads').find('a')["href"]

hemisphere_image_urls = [cerberus,chiaparelli,syrtis,valles]

# mars_dict={
#     'mars_news': {'news_title': news_title, 'news_p':news_p},
#     'feature_img': feature_img,
#     'mars_fact_table': mars_fact_table,
#     'hemisphere_image_urls':{'title': title, 'image_url': image_url}
# }

browser.quit()
mars_info = (mars_news, featured_img, mars_fact_table, hemisphere_image_urls)

return mars_info