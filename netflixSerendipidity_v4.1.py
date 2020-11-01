# -*- coding: utf-8 -*-

'''
Import libraries
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
#import requests
from bs4 import BeautifulSoup
import time
import random
import csv
import tkinter as tk
from tkinter import Label, TOP #, PhotoImage, Button, CENTER
import webbrowser
import os
import ast

driverPath = '/Users/Seansmac/Desktop/Dev/NetflixSerendipidity/chromedriver' # How does this work in prod?

sundanceMovieTitleList = []
palmMovieTitleList =[]
robertEbertmovieTitleList =[]

movieLinkList = []
moviesOnNetflix = {}
DipyDataDict ={}


"""
Note, to create a 'cell' you can add: #%% (see: https://stackoverflow.com/a/50222294)
"""

















###############################################################################
###############################################################################
## SECTION I: DEFINE FUNCTIONS
###############################################################################
###############################################################################


     
def titleCleaner(title):
    cleanTitle1 = title.replace("§","")
    cleanTitle2 = cleanTitle1.replace("(tie)","")
    cleanTitle3 = cleanTitle2.replace("[16]","")
    cleanTitle4 = cleanTitle3.replace("[14]","")  
    cleanTitle5 = cleanTitle4.replace("[15]","")
    cleanTitle = cleanTitle5.replace("#","")
    return cleanTitle

def loadMoviesOnNetflix():
     # Read from file            
    with open('DipyMoviesOnNetflix.csv', mode='r') as infile:
        reader = csv.reader(infile)
        readerII = csv.DictReader(open('DipyMoviesOnNetflix.csv'))
        print(readerII)
        
        result = {}
        for row in readerII:
            for column, value in row.items():  
                print(column)
            
              # consider .iteritems() for Python 2
                result.setdefault(column, []).append(value)
        print(result)
                
        
        DipyMoviesOnNetflix = {rows[0]:rows[1] for rows in readerII}

        
        #with open('DipyScannedMovieList_new.csv', mode='w') as outfile:
            #writer = csv.writer(outfile)
        DipyMoviesOnNetflix = {rows[0]:rows[1] for rows in reader}
        # source; https://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file
        return DipyMoviesOnNetflix
    
    

    
def launchMovie():
      webbrowser.open("https://www.netflix.com/"+selectedMovieLink, new=1)
    
    
def displayMovieTitle():
    titleText = Label(root, text = ('Your expert recommended movie is: ',selectedMovieTitle), font =( 
            'Verdana', 15))
    sourceText = Label(root, text = ('This comes from: ',selectedMovieSource), font =( 
            'Verdana', 15)) 
    titleText.place(x = 300, y = 300)
    sourceText.place(x = 300, y = 350)
    
    

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Update Movie List Function
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def updateMovieList():
    driver = webdriver.Chrome(executable_path= driverPath)  

        
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """
    Sundance winners
    """
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    sourceTargetSundance = 'https://en.wikipedia.org/wiki/List_of_Sundance_Film_Festival_award_winners'
    driver.get(sourceTargetSundance)
    htmlResults = driver.page_source
    soup_sundance = BeautifulSoup(htmlResults, 'html.parser')
    print(soup_sundance.prettify())
    
    
    
    sundance_content= soup_sundance.find_all("div", id="bodyContent")
    print(sundance_content[0].prettify())
    
    sundance_content_list= soup_sundance.find_all("ul")
    for i in range(0, len(sundance_content_list)):
        italics_items = sundance_content_list[i].find_all("i")
        for j in range(0, len(italics_items)):
            sundanceTitle = italics_items[j].get_text(strip = True)
            print("Sundance title is: ", sundanceTitle)
            sundanceMovieTitleList.append(sundanceTitle)
    
    
    print(sundanceMovieTitleList)
    print('number of sundance films: ', len(sundanceMovieTitleList))
    
    # Remove duplicates  
    sundanceMovieTitleListClean=[]
    
    for i in sundanceMovieTitleList:
      if i not in sundanceMovieTitleListClean:
          sundanceMovieTitleListClean.append(i)
        
    print('raw list length:', len(sundanceMovieTitleList))
    print('clean list length:', len(sundanceMovieTitleListClean))
    
    """
    Populate Dipy data with Sundance films
    """
    # create test dictionary with Sundance titles
    for movie in range(len(sundanceMovieTitleListClean)):
        DipyDataDict[sundanceMovieTitleListClean[movie]] = "Sundance winner"
    
    print("Sundance films successfully gathered")
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """
    Palme d'or winners
    """
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #driver = webdriver.Chrome(executable_path= driverPath)  
    
    
    sourceTargetCannes = 'https://en.wikipedia.org/wiki/Palme_d%27Or'
    driver.get(sourceTargetCannes)
    htmlResults = driver.page_source
    soup_dOR = BeautifulSoup(htmlResults, 'html.parser')
    
    table = soup_dOR.find_all("table", class_="wikitable sortable jquery-tablesorter")
    len(table)
    table_body = table[0].find('tbody')
    rows = table_body.find_all('tr')
    
    
    for row in rows:
        cols = row.find_all('td')
        col_num = 0
        for col in cols:
            if col_num == 1:
                titlePalmWinner = col.get_text(strip=True)
                print('recovered text ', titlePalmWinner)
                titlePalmWinnerClean = titleCleaner(titlePalmWinner)
                print('clean title: ',titlePalmWinnerClean )
                palmMovieTitleList.append(titlePalmWinnerClean)
                col_num += 1
            else:
                col_num += 1
                                             
                                 
    print(palmMovieTitleList)
    
    """
    Populate Dipy data with Palm d'Or films
    """
    # create test dictionary with Sundance titles
    for movie in range(len(palmMovieTitleList)):
        DipyDataDict[palmMovieTitleList[movie]] = "Palm d'Or Winner"
            
    
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """
    Roger Ebert
    """
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #driver = webdriver.Chrome(executable_path= driverPath)  
    
    
    sourceTargetRobertEbert = 'https://www.rogerebert.com/great-movies'
    driver.get(sourceTargetRobertEbert)
    
    htmlResults = driver.page_source
    soup = BeautifulSoup(htmlResults, 'html.parser')

    
    # Set filters
    yearFilter = driver.find_element_by_id("filters_years_")
    yearFilter.send_keys('1973')
    
    ratingFilter = driver.find_element_by_name("filters[star_rating][]")
    ratingFilter.send_keys("5.0")
    ratingFilter.send_keys(Keys.RETURN)
    
    Select(driver.find_element_by_css_selector("select#filters_star_rating_")).select_by_value("3.0")
    
    # Scroll to bottom of page
    
                                               
    html = driver.find_element_by_tag_name('html')
    waterfall = 600 #to optimise at a later point.
    for barrel in range(waterfall):
        html.send_keys(Keys.DOWN)
        print('barrel number: ',barrel)
        
    # Extract data                                       
        print("------------ SCANNING FOR GREAT FILMS ------------")  
        print("------------ #expertsNotAlgorithms ------------")                                       
                                         
    reviewData = driver.page_source
    soup = BeautifulSoup(reviewData, 'html.parser')
    #print(soup.prettify())
    #firstSlider = soup.find("div", "slider-item slider-item-0")
           
                            
    
    for movie in soup.find_all("h5", class_="review-stack--title"):
       # print(div.find('a')['href'])
       #print(movie.text)
       movieTitle = movie.text
       movieTitle = movieTitle.replace("\n","")
       robertEbertmovieTitleList.append(movieTitle)
       #print(movieTitleList)
        #print(div.find('a'))
    
    
    # Remove possible duplicates  
    robertEbertmovieTitleListClean=[]
    
    for i in robertEbertmovieTitleList:
      if i not in robertEbertmovieTitleListClean:
          robertEbertmovieTitleListClean.append(i)
          
    # remove suggested recommendations at bottom 
    unwantedSuggestedReviews = 4
    robertEbertmovieTitleListClean = robertEbertmovieTitleListClean[:len(robertEbertmovieTitleListClean)-unwantedSuggestedReviews]
    
        
    print('raw list length:', len(robertEbertmovieTitleList))
    print('clean list length:', len(robertEbertmovieTitleListClean))
    
    
     
   
    
    """
    Populate Dipy data with Robert Ebert films
    """
    # create test dictionary with Sundance titles
    for movie in range(len(robertEbertmovieTitleListClean)):
        DipyDataDict[robertEbertmovieTitleListClean[movie]] = "Robert Egbert: ***** Review"
            
    
    
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """
    Export Movie list
    """
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    
    
    
    """
    Remove duplicated moveis (keys)
    """
    # It appears dictionaries do not permit duplicated keys and overwrite with new key values
    
    
    print(os.getcwd())
    os.chdir("/Users/Seansmac/Desktop/Dev/NetflixSerendipidity") # Need to make generalisable
    print(os.getcwd())
    
    
        
    # Write to file
    with open('DipyScannedMovieList.csv', 'w') as f:  
        w = csv.writer(f)
        w.writerows(DipyDataDict.items())
        
    print('Dipy data exported to: ', os.getcwd())
    
   
            
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """
    Find selected films on Netflix
    """
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    # Fill in credentials here
    myEmail = 'seanmckiernan01@gmail.com'
    myPassword = '91pul30saR'
    #myProfile = 'Sean'
    
    
    
    
    driver = webdriver.Chrome(executable_path= driverPath)  
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
    searchCount = 0
    for movie in DipyDataDict:
        print("search count: ", searchCount)
        print(round(searchCount/len(DipyDataDict)*100, 2), "% completed")
        
        
         # TEST
        #movie = "Spirited Away"
        #TEST
        movieQueryOriginal = movie
        movieQuery = movie.replace("'","") #clean out apostrophes
        
       
        
        print("Searching for reviewed movie in Netflix' catalogue: ", movie)
        moveieQuerySearchFormat = movieQuery.replace(" ","%20")
        print("Search term: ",moveieQuerySearchFormat)
        
        
        searchTarget = "https://www.netflix.com/search?q="+moveieQuerySearchFormat
        driver.get(searchTarget)
        
        htmlResults = driver.page_source
        soup = BeautifulSoup(htmlResults, 'html.parser')
    
        if soup.find("div", "slider-item slider-item-0") is None:
            print("Search failed: No results")
        else:
        
            firstSlider = soup.find("div", "slider-item slider-item-0")
            topResult = firstSlider.findAll('a')[0]['aria-label']    
            
            if topResult != movieQuery:   
                print("Search failed: No title match")
            else:    
                print('Search result is: ', topResult)
                print("**** QUERY MATCH ****")
                print("Matched movie: ", movieQuery)
                movieLink = firstSlider.findAll('a')[0]['href']
                positiveHitTitleList.append(movieQueryOriginal)
                positiveHitLinkList.append(movieLink)
                print(positiveHitTitleList)
        
        
    #populate results dictionary
    for matchedMovie in range(len(positiveHitTitleList)):
        
        moviesOnNetflixValueList =[] #the values

        matchedMovieTitle = positiveHitTitleList[matchedMovie] #the key
        matchedMovieLink = positiveHitLinkList[matchedMovie] # value: 1
        matchedMovieSource = DipyDataDict[matchedMovieTitle] # value: 2
        
        # Value list defined
        moviesOnNetflixValueList.append(matchedMovieLink)
        moviesOnNetflixValueList.append(matchedMovieSource)

        # Key/ Value list pair defined
        moviesOnNetflix[matchedMovieTitle] = moviesOnNetflixValueList
    
  # Write to file
    with open('DipyMoviesOnNetflix.csv', 'w') as f:  
        w = csv.writer(f)
        w.writerows(moviesOnNetflix.items())
        
    print('Dipy movies on your Netflix data exported to: ', os.getcwd())








""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
RUN UPDATE MOVIE LIST FUNCITON
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


updateMovieList()










###############################################################################
###############################################################################
## SECTION II: GUI
###############################################################################
###############################################################################


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
GUI
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# NEED TO ADD CREDENTIALS INPUT


#refreshList = 'TRUE'
refreshList = 'FALSE'

if refreshList == 'TRUE':
    updateMovieList()
    print('Dipy list updated')
else:
    print('Loading pre-matched Netflix movies')
    dipyMoviesOnNetflix= loadMoviesOnNetflix()
    
    """
    SELECT MOVIE RECOMMENDATION
    """
    movieSelection = random.randint(0,len(dipyMoviesOnNetflix))
    selectedMovieTitle = list(dipyMoviesOnNetflix.keys())[movieSelection]   
    selectedMovieLink = ast.literal_eval(list(dipyMoviesOnNetflix.values())[movieSelection])[0]
    selectedMovieSource = ast.literal_eval(list(dipyMoviesOnNetflix.values())[movieSelection])[1]

    print("Your expert reviewed movie is: ", selectedMovieTitle)
    print("You can watch it here: https://www.netflix.com/"+selectedMovieLink)
    print("Source of movie: ",selectedMovieSource)

    
    
    root = tk.Tk()
    canvas  =tk.Canvas(root, height = 500, width = 700, bg = "red")
    canvas.pack()
    
    root.title('Dipy: The Netflix Randomiser')
    
    test = tk.Button(root, text = 'Randomise', command = displayMovieTitle, 
                     bg= 'white')
    test.pack()
    test.place(x = 300, y = 200)
    
    root.mainloop()
    
    
    # =============================================================================
    # def helloCallBack():
    #    tkMessageBox.showinfo( "Hello Python", "Hello World")
    # 
    # B = Tkinter.Button(top, text ="Hello", command = helloCallBack)
    # 
    # B.pack()
    # top.mainloop()
    # =============================================================================
    
    
    
    
    
    
    frame = tk.Frame(root, bg = "black")
    frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely = 0.1)
    
    Label(root, text = 'Choose a film', font =( 
      'Verdana', 15)).pack(side = TOP, pady = 10)
    
    # =============================================================================
    # photo = PhotoImage(file = r"/Users/Seansmac/Desktop/Dev/NetflixSerendipidity/netflixLogo.png") 
    #   
    # # here, image option is used to 
    # # set image on button 
    # Button(root, text = 'Select Film!', image = photo, command = launchMovie).place(
    #         relx=0.5, rely=0.5, anchor=CENTER) 
    #        
    # #openLink.pack()
    # 
    # =============================================================================
    introText = Label(root, text="Dipidity: Watch something different")
    introText.pack()
    
    #openLink = tk.Button(frame, text = "Watch movie", padx= 10, pady= 5, fg="midnight blue",
    #                     bg = "white", command = launchMovie)
    #
    
    root.mainloop()