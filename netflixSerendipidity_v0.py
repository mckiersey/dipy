# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from bs4 import BeautifulSoup

# Fill in credentials here
myEmail = 'seanmckiernan01@gmail.com'
myPassword = '91pul30saR'
myProfile = 'Sean'




target = 'https://www.netflix.com/ie/login'
"""
response = requests.get(target)

if response.status_code == 200:
    print('target acquired')
    content = response.headers

else:
    print('website not acquired')
    
loginCredentials = {'email' : myEmail,
                    'password' : myPassword}
                    

with requests.session() as sesh: 
  login =  sesh.post(target, loginCredentials)
  print(login.status_code )
  
  # Parse with beautiful soup
  
soup = BeautifulSoup(login.text, 'html.parser')
print(soup.prettify())

mydivs = soup.findAll("div", {"class": "profile-name"})
print(mydivs)
"""

## Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys;
from collections import defaultdict

import json
import time



myEmail = 'seanmckiernan01@gmail.com'
myPassword = '91pul30saR'
myProfile = 'Sean'
movieQuery ='My Octopus Teacher'
moveieQuerySearchFormat = movieQuery.replace(" ","%20")
moveieQuerySearchFormat

movieTitleList =[]
movieLinkList = []
moviesOnNetflix = {}



target = 'https://www.netflix.com/ie/login'
driverPath = '/Users/Seansmac/Desktop/Dev/NetflixSerendipidity/chromedriver'
driver = webdriver.Chrome(executable_path= driverPath)  # Or Chrome(), or Ie(), or Opera()
driver.get(target)

username = driver.find_element_by_id("id_userLoginId")
password = driver.find_element_by_id("id_password")

username.send_keys(myEmail)
password.send_keys(myPassword)
elem = driver.find_element_by_name("password")
elem.send_keys(Keys.RETURN)
time.sleep(2)
driver.find_element_by_class_name("profile-name").click()


searchTarget = "https://www.netflix.com/search?q="+moveieQuerySearchFormat
driver.get(searchTarget)


htmlResults = driver.page_source
soup = BeautifulSoup(htmlResults, 'html.parser')
firstSlider = soup.find("div", "slider-item slider-item-0")

topResult = firstSlider.findAll('a')[0]['aria-label']
print('Search result is: ', topResult)
if topResult == movieQuery:
    print("**** QUERY MATCH ****")
    print("Matched movie: ", movieQuery)
    movieLink = firstSlider.findAll('a')[0]['href']

#populate results dictionary
    moviesOnNetflix[labels[j]] = results[j]



"""
searchBox = driver.find_element_by_class_name("searchTab")
print(movieQuery)
time.sleep(4)
searchBox.send_keys(movieQuery)
time.sleep(4)

searchElem = driver.find_element_by_name("searchInput")
searchElem.send_keys(Keys.RETURN)


content = driver.page_source
print(content)
type

html = driver.page_source
soup = BeautifulSoup(html)
movieContent = soup.find("div", class_="ptrack-content")["aria-label"]
print(len(movieContent))
numMovies = len(movieContent)

movieNames= []
movieLinks=[]
for i in range(len(movieContent)):
    movieNames.append(movieContent[i].find_all('img')[0]['aria-label'])
    movieLinks.append(movieContent[i].find_all('img')[0]['src'])
re

netflixData = {}
keys = movieNames
values = movieLinks

movieContent[1].find_all('img')[0]['alt']

soup = BeautifulSoup(html, "html.parser")
print( soup.find("div", class_="ptrack-content")["src"] )

driver.getCurrentUrl();

req = requests.get('http://dsx.weather.com/wxd/v2/MORecord/en_US/(USCA0478:1:US)?api=7bb1c920-7027-4289-9c96-ae5e263980bc')
data = req.json()
print(data[0]['doc']['MOData']['tmpF'])
""



