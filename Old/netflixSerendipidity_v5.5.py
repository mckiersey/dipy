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
from tkinter import Label , PhotoImage, StringVar, Entry
import webbrowser
import os
import ast
from functools import partial


driverPath = '/Users/Seansmac/Desktop/Dev/NetflixSerendipidity/chromedriver' # How does this work in prod?
os.chdir("/Users/Seansmac/Desktop/Dev/NetflixSerendipidity") # How to do in prod?

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

'''
def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return
'''

def loadMoviesOnNetflix():
     # Read from file      
    with open('DipyMoviesOnNetflix.csv', mode='r') as infile:
        reader = csv.reader(infile)
        readerII = csv.DictReader(open('DipyMoviesOnNetflix.csv'))
        
        result = {}
        for row in readerII:
            for column, value in row.items():  
            
              # consider .iteritems() for Python 2
                result.setdefault(column, []).append(value)
                
        
        DipyMoviesOnNetflix = {rows[0]:rows[1] for rows in readerII}
        DipyMoviesOnNetflix = {rows[0]:rows[1] for rows in reader}
        
        movieSelection = random.randint(0,len(DipyMoviesOnNetflix))
        selectedMovieTitle = list(DipyMoviesOnNetflix.keys())[movieSelection]   
        global selectedMovieLink
        selectedMovieLink = ast.literal_eval(list(DipyMoviesOnNetflix.values())[movieSelection])[0]#,
        selectedMovieSource = ast.literal_eval(list(DipyMoviesOnNetflix.values())[movieSelection])[1]
        titleTextString = 'Your expert recommended movie is: '+selectedMovieTitle
        sourceTextString = 'This comes from: ' + selectedMovieSource
        
        global titleText
        global sourceText
        
        titleText.destroy()
        sourceText.destroy()
        
        titleText = Label(root, text = (titleTextString), font =( 
            'Verdana', 15), bg= 'black', fg = 'white')
          
        
        sourceText = Label(root, text = (sourceTextString), font =( 
                'Verdana', 15), bg= 'black', fg = 'white') 

        titleText.place(x = 190, y = 600)
        sourceText.place(x = 190, y = 620)
        
        print('selected movie: ', selectedMovieTitle)
        print('selected movie link: ', selectedMovieLink)

        
    return (selectedMovieTitle, selectedMovieLink, selectedMovieSource)
    




def launchMovie():
     # Retrieve the movie
         print('launching ',selectedMovieLink)
       # movieLink = loadMoviesOnNetflix()
       # selectedMovieLink = movieLink[1][0]
         webbrowser.open("https://www.netflix.com"+selectedMovieLink, new=1)
      
        #return selectedMovieTitle, selectedMovieLink, selectedMovieSource

    

    

def showCredentialsEntry():
    usernameLabel.place(x = 500, y = 105)
    usernameEntry.place(x = 500, y = 105)
    passwordLabel.place(x = 500, y = 135)
    passwordEntry.place(x = 500, y = 135)
    loginButton.place(x = 500, y =165)
    
    global loginExplained
    loginExplained.destroy()
    loginExplained = Label(root, text = "Enter your Netflix account \n" +
                           "details so Dipy can \n" + 
                           "cross-reference scanned \n" +
                           "movies with your local \n" +
                           "Netflix library \n" +
                           "This'll take a few minutes!", font =( 
            'Verdana', 13), bg= 'black', fg = 'white')
    loginExplained.place(x = 500, y = 190)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Update Movie List Function
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def updateMovieList(username, password):
    driver = webdriver.Chrome(executable_path= driverPath) 
    
    email = username.get()
    password = password.get()
    print("username entered :", email)
    print("password entered :", password)
    
    
    global updateText
    global loginExplained
    global updateTextString
    
    loginExplained.destroy()
    updateText.destroy()
    updateTextString.set('this is a test')
  

    # Print progress text
    updateText = Label(root, text = updateTextString,
                       #('Launching Chrome...')
                       font =( 
            'Verdana', 15), bg= 'black', fg = 'white')
    updateText.place(x = 500, y = 300)


    Testtext = tk.StringVar()
    Testtext.set('')
    lab = tk.Label(root, textvariable=Testtext, fg='blue', bg= 'white')
    lab.place(x = 500, y = 300)
    Testtext.set('calling my function1')
        
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """
    Sundance winners
    """
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # Print progress text
    updateText.destroy()

    updateText = Label(root, text = ('Scanning for Sundance awarded films...'), font =( 
            'Verdana', 15), bg= 'black', fg = 'white')
    updateText.place(x = 500, y = 300)
    
    
    sourceTargetSundance = 'https://en.wikipedia.org/wiki/List_of_Sundance_Film_Festival_award_winners'
    driver.get(sourceTargetSundance)
    htmlResults = driver.page_source
    soup_sundance = BeautifulSoup(htmlResults, 'html.parser')
        
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
    print("Number films collected: ", len(DipyDataDict))

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """
    Palme d'or winners
    """
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #driver = webdriver.Chrome(executable_path= driverPath)  
    
    # Print progress text
    updateText.destroy()

    updateText = Label(root, text = ("Scanning for Palme d'Or winners..."), font =( 
            'Verdana', 15), bg= 'black', fg = 'white')
    updateText.place(x = 500, y = 300)
    

    sourceTargetCannes = 'https://en.wikipedia.org/wiki/Palme_d%27Or'
    driver.get(sourceTargetCannes)
    htmlResults = driver.page_source
    soup_dOR = BeautifulSoup(htmlResults, 'html.parser')
    
    
    table = soup_dOR.find_all("table", class_="wikitable sortable")
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
        
    print("Palm d'Or films successfully gathered")  
    print("Number films collected: ", len(DipyDataDict))
            
    
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """
    Roger Ebert
    """
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #driver = webdriver.Chrome(executable_path= driverPath)  
    
    # Print progress text
    updateText.destroy()
    updateText = Label(root, text = ("Scanning for Five Star Robert Ebert reviewed films..."), font =( 
            'Verdana', 15), bg= 'black', fg = 'white')
    updateText.place(x = 500, y = 300)
    
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
           
                            
    
    for movie in soup.find_all("h5", class_="review-stack--title"):
       movieTitle = movie.text
       movieTitle = movieTitle.replace("\n","")
       robertEbertmovieTitleList.append(movieTitle)
    
    
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
       
    print("Robert Ebert films successfully gathered")  
    print("Number films collected: ", len(DipyDataDict))
            
    
    
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """
    Export Movie list
    """
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
     
    
    """
    Remove duplicated moveis (keys)
    """
    # It appears dictionaries do not permit duplicated keys and overwrite with new key values
    
    # Print progress text
    updateText.destroy()
    updateText = Label(root, text = ("Saving scanned films..."), font =( 
            'Verdana', 15), bg= 'black', fg = 'white')
    updateText.place(x = 500, y = 300)
    
    print(os.getcwd())
    os.chdir("/Users/Seansmac/Desktop/Dev/NetflixSerendipidity") # How to do in prod?
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
    myEmail = email
    myPassword = password
    #myProfile = 'Sean'
    
    # Print progress text
    updatingText = Label(root, text = ("Cross check with Netflix library..."), font =( 
            'Verdana', 15), bg= 'black', fg = 'white')
    updatingText.place(x = 600, y = 100)
    
    
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
        searchCount +=1
        
        
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
   
    # Print progress text
    updateText.destroy()
    updateText = Label(root, text = ("Saving films that are on Netflix..."), font =( 
            'Verdana', 15), bg= 'black', fg = 'white')
    updateText.place(x = 500, y = 300)
    
    
  # Write to file
    with open('DipyMoviesOnNetflix.csv', 'w') as f:  
        w = csv.writer(f)
        w.writerows(moviesOnNetflix.items())
        
    print('******************************************************************')
    print('******************************************************************')
    print('******************************************************************')

    print('Dipy movies on your Netflix data exported to: ', os.getcwd())
    print('Number of matched movies on Netflix: ', len(positiveHitTitleList))

     # Print progress text
    updateText.destroy()
    updateText = Label(root, text = ("Done!"), font =( 
            'Verdana', 15), bg= 'black', fg = 'white')
    updateText.place(x = 500, y = 300)





""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
RUN UPDATE MOVIE LIST FUNCITON
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""












###############################################################################
###############################################################################
## SECTION II: GUI
###############################################################################
###############################################################################



# =============================================================================
# Create GUI
# =============================================================================

root = tk.Tk()

canvas  =tk.Canvas(root, height = 700, width = 800, bg = "red")
canvas.pack()

titleText = Label(root)
sourceText = Label(root)
updateText = Label(root)
loginExplained= Label(root)
updateTextString = StringVar()

root.title('Dipy: The Netflix Randomiser')


frame = tk.Frame(root, bg = "black")
frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely = 0.1)


# enter username & password
usernameLabel = Label(root, text="User Name", font =('Verdana', 15), bg= 'black', fg = 'white')
username = StringVar()
usernameEntry = Entry(root, textvariable=username) 



#password label and password entry box
passwordLabel = Label(root,text="Password", font =('Verdana', 15), bg= 'black', fg = 'white') 
password = StringVar()
passwordEntry = Entry(root, textvariable=password, show='*')


# Login button
updateMovieList = partial(updateMovieList, username, password)
loginButton = tk.Button(root, text="Netflix Login", command=updateMovieList) 


usernameLabel.forget()
usernameEntry.forget()
passwordLabel.forget()
passwordEntry.forget()
loginButton.forget()


# Select a movie

selectMovieBtn = tk.Button(root, text = 'Select a movie', command =  loadMoviesOnNetflix,
                 bg= 'white')

selectMovieBtn.pack()
selectMovieBtn.place(x = 100, y = 80)

updateListBtn = tk.Button(root, text ='Refresh movie list', command = showCredentialsEntry,
                          bg= 'white')
updateListBtn.pack()
updateListBtn.place(x = 600, y = 80)


netflixLogoImage = PhotoImage(file = r"/Users/Seansmac/Desktop/Dev/NetflixSerendipidity/netflixLogo.png") 
   


openLinkButton = tk.Button(frame, text = "Click to watch movie!", image = netflixLogoImage, padx= 10, pady= 5, fg="midnight blue",
                     bg = "white", command = launchMovie, compound='top')
        
openLinkButton.pack(pady= 40)
openLinkButton.place(y = 100, x = 200)
 
introText = Label(root, text="Dipidity: Watch something different")
introText.pack()
root.mainloop()




