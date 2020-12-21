# -*- coding: utf-8 -*-

# cultural echo chambers

'''
Import libraries
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
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
import sys
from pathlib import Path


if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    bundle_dir = Path(sys._MEIPASS)
    print("******* PRODUCTION MODE *******")
    print('The bundle dircectory is: ', bundle_dir)
else:
    bundle_dir = Path(__file__).parent
    print("******* DEV MODE *******")
    print('The bundle dircectory is: ', bundle_dir)

driver_path = Path.cwd() / bundle_dir / "chromedriver/chromedriver"
scanned_movie_list_path = Path.cwd() / bundle_dir / "scannedMoviesList.csv"
hit_movie_list_path = Path.cwd() / bundle_dir / "DipyMoviesOnNetflix.csv"
netflix_logo_path = Path.cwd() / bundle_dir / "netflixLogo.png"

print("***** PAHTS ******")
print("DRIVER: ", driver_path)
print("DATA: ",hit_movie_list_path)
print("LOGO: ", netflix_logo_path)

sundanceMovieTitleList = []
palmMovieTitleList =[]
robertEbertmovieTitleList =[]

movieLinkList = []
moviesOnNetflix = {}
DipyDataDict ={}






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
    #try:  
    with open(hit_movie_list_path, mode='r') as infile:
        print('opening data file: ', hit_movie_list_path)
        reader = csv.reader(infile)
        readerII = csv.DictReader(open(hit_movie_list_path))

        
        result = {}
        for row in readerII:

            for column, value in row.items():  
            
                result.setdefault(column, []).append(value)  

        DipyMoviesOnNetflix = {rows[0]:rows[1] for rows in readerII}
        DipyMoviesOnNetflix = {rows[0]:rows[1] for rows in reader}

        movieSelection = random.randint(0,len(DipyMoviesOnNetflix))
        selectedMovieTitle = list(DipyMoviesOnNetflix.keys())[movieSelection]   

        global selectedMovieLink

        selectedMovieLink = ast.literal_eval(list(DipyMoviesOnNetflix.values())[movieSelection])[0]
        print('movie selection link: ', selectedMovieLink)

        selectedMovieSource = ast.literal_eval(list(DipyMoviesOnNetflix.values())[movieSelection])[1]
        print('movie selection source: ', selectedMovieSource)

        titleTextString = 'Your expert recommended movie is: '+selectedMovieTitle
        sourceTextString = 'Recommended by: ' + selectedMovieSource

        global titleText
        global sourceText
                
        try:
            updateText.destroy()
        except:
            pass

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



        titleText.destroy()
        sourceText.destroy()
        updateText.destroy()

        updateText = Label(root, text = ("You need to scan for movies first so Dipy can select one for you  \n (it'll take a few mins)"), font =( 
            'Verdana', 15), bg= 'black', fg = 'white')
        updateText.place(x = 190, y = 600)   
        print("Exception 1")
        


def launchMovie():
     # Retrieve the movie
        try:
            webbrowser.open("https://www.netflix.com"+selectedMovieLink, new=1)
        except:
            try:
                titleText.destroy()
                sourceText.destroy()
                updateText.destroy()
            except:
                pass

            updateText = Label(root, text = ("Make sure to select a movie first!"), font =( 
                'Verdana', 15), bg= 'black', fg = 'white')
            updateText.place(x = 240, y = 600)   
            print("Exception 0")

  

def showCredentialsEntry():
    usernameLabel.place(x = 100, y = 105)
    usernameEntry.place(x = 100, y = 105)
    passwordLabel.place(x = 100, y = 135)
    passwordEntry.place(x = 100, y = 135)
    loginButton.place(x = 100, y =170)

    global updateText
    global loginExplained
    loginExplained.destroy()
    loginExplained = Label(root, text = "Enter your Netflix account \n" +
                           "details so Dipy can \n" + 
                           "cross-reference scanned \n" +
                           "movies with your local \n" +
                           "Netflix library \n" +
                           "This'll take a few minutes!", font =( 
            'Verdana', 12), bg= 'black', fg = 'white')
    loginExplained.place(x = 90, y = 198)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Update Movie List Function
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#global updateText
global loginExplained
global updateTextString

def updateMovieList(username, password):
    try:

        driver = webdriver.Chrome(executable_path= driver_path) 
        email = username.get()
        password = password.get()
        print("username entered :", email)
        print("password entered :", password)
 
  
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        """
        Sundance winners
        """
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        
        try:
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
                DipyDataDict[sundanceMovieTitleListClean[movie]] = "Sundance Film Festival"
            
            print("Sundance films successfully gathered")
            print("Number films collected: ", len(DipyDataDict))

        except:
            try: 
             titleText.destroy()
             sourceText.destroy()
             updateText.destroy()
            except:
                pass
            updateText = Label(root, text = ("Hey! Sorry, this is a little embarrassing, but do you have Chrome installed/working internet connection? \n" +
            "Maybe have a look & try again"), font =( 
                'Verdana', 15), bg= 'black', fg = 'white')
            updateText.place(x = 190, y = 600)  
            print("Exception 2")
 

        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        """
        Palme d'or winners
        """
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        
        try:
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
                DipyDataDict[palmMovieTitleList[movie]] = "Cannes Film Festival (Palm d'Or winner)"
                
            print("Palm d'Or films successfully gathered")  
            print("Number films collected: ", len(DipyDataDict))

        except:

            try: 
             titleText.destroy()
             sourceText.destroy()
             updateText.destroy()
            except:
                pass

            updateText = Label(root, text = ("Hey! Sorry, this is a little embarrassing, but do you have Chrome installed/working internet connection? \n" +
            "Have another look & try again"), font =( 
                'Verdana', 15), bg= 'black', fg = 'white')
            updateText.place(x = 190, y = 600)   
            print("Exception 3")

            
        
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        """
        Roger Ebert
        """
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""    
        
        try:
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
                DipyDataDict[robertEbertmovieTitleListClean[movie]] = "Robert Egbert: 5 Star Review"
            
            print("Robert Ebert films successfully gathered")  
            print("Number films collected: ", len(DipyDataDict))

        
        except:

            try: 
                titleText.destroy()
                sourceText.destroy()
                updateText.destroy()
            except:
                pass
            updateText = Label(root, text = ("Hey, this is a little embarrassing, but do you have Chrome installed/working internet connection? \n" +
            "Have another look & try again"), font =( 
                'Verdana', 15), bg= 'black', fg = 'white')
            updateText.place(x = 190, y = 600) 
            print("Exception 4")
           
            
        driver.quit()
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        """
        Export Movie list
        """
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        
            
        # Write to file
        with open(scanned_movie_list_path, 'w') as f:  
            w = csv.writer(f)
            w.writerows(DipyDataDict.items())
        
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        """
        Find selected films on Netflix
        """
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        
        # Fill in credentials here
        UserEmail = email
        UserPassword = password
    
        
        driver = webdriver.Chrome(executable_path= driver_path)  
        target = 'https://www.netflix.com/ie/login'
        driver.get(target)
        
        username = driver.find_element_by_id("id_userLoginId")
        password = driver.find_element_by_id("id_password")
        username.send_keys(UserEmail)
        password.send_keys(UserPassword)
        elem = driver.find_element_by_name("password")
        elem.send_keys(Keys.RETURN)
        
        time.sleep(0.5)
        try:

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

            driver.quit()
        
            
            
        # Write to file
            with open(hit_movie_list_path, 'w') as f:  
                w = csv.writer(f)
                w.writerows(moviesOnNetflix.items())
                
            print('******************************************************************')
            print('******************************************************************')
            print('******************************************************************')

            print('Dipy movies on your Netflix data exported to: ', hit_movie_list_path)
            print('Number of matched movies on Netflix: ', len(positiveHitTitleList))
            
            titleText.destroy()
            sourceText.destroy()
            updateText.destroy()
            loginExplained.destroy()

            updateText = Label(root, text = ("Scan complete! You can watch a film now"), font =( 
                'Verdana', 15), bg= 'black', fg = 'white')
            updateText.place(x = 190, y = 600)   


        except:
            titleText.destroy()
            sourceText.destroy()
            updateText.destroy()
    
            updateText = Label(root, text = ("Opps! Your Netflix username or password seems wrong. \n" + "Maybe have another look & try it again."), font =( 
                'Verdana', 15), bg= 'black', fg = 'white')
            updateText.place(x = 190, y = 600)
            print("Exception 5")

            
    except:
        try: 
            titleText.destroy()
            sourceText.destroy()
            updateText.destroy()
        except:
            pass
        updateText = Label(root, text = ("Opps! Your Netflix username or password seems wrong. \n" + "Maybe have another look & try it again."), font =( 
        'Verdana', 15), bg= 'black', fg = 'white')
        updateText.place(x = 190, y = 600)   
        print("Exception 6")

 

    

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

root.title('Dipy: The Netflix Randomiser | Watch something different')


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

updateListBtn = tk.Button(root, text ='Scan for movies', command = showCredentialsEntry, bg= 'white')
updateListBtn.pack()
updateListBtn.place(x = 100, y = 80)

selectMovieBtn = tk.Button(root, text = 'Select a movie', command =  loadMoviesOnNetflix, bg= 'white')

selectMovieBtn.pack()
selectMovieBtn.place(x = 600, y = 80)

netflixLogoImage = PhotoImage(file =  netflix_logo_path) 

openLinkButton = tk.Button(frame, text = "Click to watch movie!", image = netflixLogoImage, padx= 10, pady= 5, fg="midnight blue",
                     bg = "white", command = launchMovie, compound='top')
        
openLinkButton.pack(pady= 40)
openLinkButton.place(y = 120, x = 200)
 
introText = Label(root, text="#ExpertsNotAlgorithms")
introText.pack()
root.mainloop()



########################## END OF SCRIPT  ##########################

## Seán McKiernan | Nov 2020 | A lockdown Project
