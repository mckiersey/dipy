# -*- coding: utf-8 -*-

'''
Import libraries
'''


import tkinter as tk
from tkinter import Label , PhotoImage, StringVar, Entry



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
#updateMovieList = partial(updateMovieList, username, password)
loginButton = tk.Button(root, text="Netflix Login"), #command=updateMovieList) 


usernameLabel.forget()
usernameEntry.forget()
passwordLabel.forget()
passwordEntry.forget()
#loginButton.forget()


# Select a movie

selectMovieBtn = tk.Button(root, text = 'Select a movie',  bg= 'white')#,command =  loadMoviesOnNetflix)
                

selectMovieBtn.pack()
selectMovieBtn.place(x = 100, y = 80)

updateListBtn = tk.Button(root, text ='Refresh movie list',bg= 'white')#, command = showCredentialsEntry)
                          
updateListBtn.pack()
updateListBtn.place(x = 600, y = 80)


photo = PhotoImage(file = r"/Users/Seansmac/Desktop/Dev/NetflixSerendipidity/netflixLogo.png") 
   


openLinkButton = tk.Button(frame, text = "Click to watch movie!", image = photo, padx= 10, pady= 5, fg="midnight blue",
                     bg = "white", compound='top')# command = launchMovie)
        
openLinkButton.pack(pady= 40)
openLinkButton.place(y = 100, x = 200)
 
introText = Label(root, text="Dipidity: Watch something different")
introText.pack()
root.mainloop()




