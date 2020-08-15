# Import All Dependencies
from bs4 import BeautifulSoup as bs
import requests
import os
import pymongo
import time
from splinter import Browser
import pandas as pd


def scrape():
#Scraping for All Data
# ### NASA Mars News
    executable_path = {'executable_path': 'C:\\Users\\winyi\\OneDrive\\Desktop\\LearnPython\\chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://mars.nasa.gov/news"
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    soup = bs(html, 'lxml')

    results = soup.find('div', class_='list_text')
    news_title = results.a.text
    teaser = soup.find('div', class_ ='article_teaser_body')
    news_p = teaser.text

    

    # ### JPL Mars Space Images - Featured Image
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=featured#submit"
    browser.visit(url2)
    browser.click_link_by_partial_text("FULL")
    browser.click_link_by_partial_text("more info")
    time.sleep(5)
    html = browser.html
    soup2 = bs(html, 'lxml')
    featured=soup2.find('figure', {'class':'lede'}).find('a')['href']
    main_url = 'https://www.jpl.nasa.gov'
    featured_image_url=main_url + featured

    # ### Mars Weather
    url3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url3)
    time.sleep(5)
    html3 = browser.html
    soup3 = bs(html3, 'lxml')   
    tweet = soup3.find('div', {'class':'css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0'})    
    mars_weather = tweet.text
     

    # ### Mars Facts
    table = pd.read_html('https://space-facts.com/mars/')
    df = table[0]
    df.columns = ['description','value']
    df.set_index('description', inplace=True)
    html = df.to_html()



    # ### Mars Hemispheres
    hemispheres=['Cerberus','Schiaparelli','Syrtis Major','Valles Marineris']
    url4='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    titles=[]
    urls=[]
    for x in hemispheres:
        browser.visit(url4)
        time.sleep(5)
        browser.click_link_by_partial_text(x)
        html4=browser.html
        soup4=bs(html4,'lxml')
        url=soup4.find('div',attrs={"class":"downloads"}).find('li').find('a')['href']
        title = soup4.find('div',{'class':'content'}).h2.text
        titles.append(title)
        urls.append(url)
    hemisphere_image_urls = [
    {'title': titles[0], 'img_url':urls[0]},
    {'title': titles[1], 'img_url':urls[1]},
    {'title': titles[2], 'img_url':urls[2]},
    {'title': titles[3], 'img_url':urls[3]}]    
    

