#!/usr/bin/env python
# coding: utf-8

# In[1]:

# Declaring Dependencies 
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import numpy
import time
import requests

# In[2]:
# Initialize the browser
def init_browser(): 

# Choose the executable path to driver 
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


# In[3]:
# Creating global dictionary to import
mars_info = {}

def scrape_mars_news():
    try: 
        # Initialize the browser 
        browser = init_browser()
        # Visit Nasa news url using splinter module
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)

        # In[5]:

        # HTML Object
        html = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        time.sleep(3)
        
        #getting the news title and news_paragraph
        news_title = soup.find('div', class_='content_title').find('a').text
        news_text = soup.find('div', class_='article_teaser_body').text

        # storing in dictionary
        mars_info['news_title'] = news_title
        mars_info['news_paragraph'] = news_text

        return mars_info

    finally:

        browser.quit()

# In[6]:

def scrape_mars_image():
    try:

        # Initialize the browser 
        browser = init_browser()

        # Visit Mars Space Images through splinter module
        image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(image_url_featured)

        # In[7]:

        # HTML Object 
        html_image = browser.html
        time.sleep(3)

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_image, 'html.parser')
        
        # Getting the background image
        featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
        
        # Website Url 
        head_url = 'https://www.jpl.nasa.gov'

        # Concatenate 
        featured_image_url = head_url + featured_image_url

        # Display full link to featured image
        featured_image_url

        # storing the featured image
        mars_info['featured_image_url'] = featured_image_url 
        
        return mars_info
    finally:

        browser.quit()

# In[9]:

# Mars Weather 
def scrape_mars_weather():
    try:
        # Initialize the browser 
        browser = init_browser()

        # Visit Mars Weather url 
        mars_Weather_url  = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(mars_Weather_url)
        mars_Weather_html = browser.html

        time.sleep(3)
        # Use  BeautifulSoup `read_html` to parse the url
        soup = BeautifulSoup(mars_Weather_html, 'html.parser')
       
        weather_tweet  = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
        
        # storing WEATHER TWEET
        mars_info['weather_tweet'] = weather_tweet
        
        return mars_info
    finally:

        browser.quit()

# In[10]:

def scrape_mars_facts():
    

    # Visit Mars facts url 
    facts_url = 'https://space-facts.com/mars/'

    # Use Panda's `read_html` to parse the url
    mars_facts = pd.read_html(facts_url)

    # assigning the mass_df 
    mars_df = mars_facts[0]


    # Assign the columns `['Description', 'Mars','Earth']`
    mars_df.columns = ['Description','Value','Earth']


    # Set the index to the `Description` column without row indexing
    mars_df.set_index('Description', inplace=True)

    # Save html code to folder Assets
    data = mars_df.to_html()

    # Dictionary entry from MARS FACTS
    mars_info['mars_facts'] = data

    return mars_info

    


# In[11]:

def scrape_mars_hemispheres():

    try: 

        # Initialize the browser 
        browser = init_browser()


        # Visit hemispheres website through splinter module 
        hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemispheres_url)

        # In[12]:

        # HTML Object
        html_hemispheres = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_hemispheres, 'html.parser')

        # Getting all items that contain mars hemispheres information
        items = soup.find_all('div', class_='description')

        # Create empty list for hemisphere urls 
        hemisphere_image_urls = []

        # Store the main_ul 
        hemispheres_main_url = 'https://astrogeology.usgs.gov'

        # Loop through the items previously stored
        for i in items: 
            # Store title
            title = i.find('h3').text.replace('Enhanced','')
    
            # Store link that leads to full image website
            partial_img_url = i.find('a', class_='itemLink product-item')['href']
    
            # link for full image website 
            browser.visit(hemispheres_main_url + partial_img_url)
    
            # HTML Object 
            partial_img_html = browser.html
    
            # Parse HTML with Beautiful Soup 
            soup = BeautifulSoup( partial_img_html, 'html.parser')
    
            # Getting the full image source 
            img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
    
            # Append the information 
            hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
    
            # Display hemisphere_image_urls
            print(hemisphere_image_urls)

        mars_info['hemisphere_image_urls'] = hemisphere_image_urls  
        # Return mars_data dictionary 

        return mars_info
    finally:

        browser.quit()  













