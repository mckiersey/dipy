# -*- coding: utf-8 -*-

'''
Import libraries
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from collections import defaultdict
import requests
from bs4 import BeautifulSoup
import time
import random
driverPath = '/Users/Seansmac/Desktop/Dev/NetflixSerendipidity/chromedriver'

movieTitleList =[]
movieLinkList = []
moviesOnNetflix = {}



"""
Import quality movie list from experts
"""
driver = webdriver.Chrome(executable_path= driverPath)  


sourceTarget = 'https://www.rogerebert.com/great-movies'
driver.get(sourceTarget)

# Set filters
yearFilter = driver.find_element_by_id("filters_years_")
yearFilter.send_keys('1973')

ratingFilter = driver.find_element_by_name("filters[star_rating][]")
ratingFilter.send_keys("2.0")
ratingFilter.send_keys(Keys.RETURN)

Select(driver.find_element_by_css_selector("select#filters_star_rating_")).select_by_value("3.0")

# Scroll to bottom of page

                                           
html = driver.find_element_by_tag_name('html')
waterfall = 800 #to optimise
for barrel in range(waterfall):
    html.send_keys(Keys.DOWN)
    print('barrel number: ',barrel)
    
# Extract data                                       
    print("------------ SCANNING FOR GREAT FILMS ------------")  
    print("------------ #expertsNotAlgorithms ------------")                                       
                                     
reviewData = driver.page_source
soup = BeautifulSoup(reviewData, 'html.parser')
#print(soup.prettify())
firstSlider = soup.find("div", "slider-item slider-item-0")
       
movies = soup.find_all()                                 
                        

movieTitleList=[]              
for movie in soup.find_all("h5", class_="review-stack--title"):
   # print(div.find('a')['href'])
   #print(movie.text)
   movieTitle = movie.text
   movieTitle = movieTitle.replace("\n","")
   movieTitleList.append(movieTitle)
   #print(movieTitleList)
    #print(div.find('a'))

# Remove possible duplicates  
movieTitleListClean=[]

for i in movieTitleList:
  if i not in movieTitleListClean:
      movieTitleListClean.append(i)
    
print('raw list length:', len(movieTitleList))
print('clean list length:', len(movieTitleListClean))

print("------------ Number of movies collected: ", len(movieTitleList), "------------")                                       

 
# remove suggested recommendations at bottom 
unwantedSuggestedReviews = 4
movieTitleList = movieTitleList[:len(movieTitleList)-unwantedSuggestedReviews]
len(movieTitleList)

"""
Find selected films on Netflix
"""


# Fill in credentials here
myEmail = 'seanmckiernan01@gmail.com'
myPassword = '91pul30saR'
myProfile = 'Sean'





 
target = 'https://www.netflix.com/ie/login'
driver.get(target)

username = driver.find_element_by_id("id_userLoginId")
password = driver.find_element_by_id("id_password")

username.send_keys(myEmail)
password.send_keys(myPassword)
elem = driver.find_element_by_name("password")
elem.send_keys(Keys.RETURN)
time.sleep(0.5)
driver.find_element_by_class_name("profile-name").click()


# Open loop to check if reviewed films are in netflix catalogue:
positiveHitTitleList = []
positiveHitLinkList = []

for reviewedMovie in movieTitleListClean:
    movieQuery = reviewedMovie.replace("'","") #clean out apostrophes
    
    # TEST
   # movieQuery = "batman"
    #TEST
    
    print("Searching for reviewed movie in Netflix' catalogue: ", reviewedMovie)
    moveieQuerySearchFormat = movieQuery.replace(" ","%20")
    print("Search term: ",moveieQuerySearchFormat)
    
  
    
    searchTarget = "https://www.netflix.com/search?q="+moveieQuerySearchFormat
    driver.get(searchTarget)
    #time.sleep(0.01)

    
    htmlResults = driver.page_source
    soup = BeautifulSoup(htmlResults, 'html.parser')
    

    if soup.find("div", "slider-item slider-item-0") is None:
        print("Search failed: No results")
    else:
    
        firstSlider = soup.find("div", "slider-item slider-item-0")
        #matchCheck = soup.body.findAll(text='Explore titles related to:')
        topResult = firstSlider.findAll('a')[0]['aria-label']    
        
        if topResult != movieQuery:   
            print("Search failed: No title match")
        else:    
            #topResult = firstSlider.findAll('a')[0]['aria-label']
            print('Search result is: ', topResult)
            print("**** QUERY MATCH ****")
            print("Matched movie: ", movieQuery)
            movieLink = firstSlider.findAll('a')[0]['href']
            positiveHitTitleList.append(movieQuery)
            positiveHitLinkList.append(movieLink)
            print(positiveHitTitleList)
    
    
#populate results dictionary
for movie in range(len(positiveHitTitleList)):
    moviesOnNetflix[positiveHitTitleList[movie]] = positiveHitLinkList[movie]
    

"""
SELECT MOVIE RECOMMENDATION
"""
movieSelection = random.randint(1,len(moviesOnNetflix))
selectedMovieTitle = list(moviesOnNetflix.keys())[movieSelection]
selectedMovieLink = list(moviesOnNetflix.values())[movieSelection]

print("Your expert reviewed movie is: ", selectedMovieTitle)
print("You can watch it here: https://www.netflix.com"+selectedMovieLink)



