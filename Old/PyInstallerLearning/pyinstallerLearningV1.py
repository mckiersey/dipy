'''
Import libraries
'''


import tkinter as tk
from tkinter import Label , PhotoImage, StringVar, Entry
import sys
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    print('running in a PyInstaller bundle')
else:
    print('running in a normal Python process')

# =============================================================================
# Create GUI
# =============================================================================

root = tk.Tk()

canvas  =tk.Canvas(root, height = 700, width = 800, bg = "red")
canvas.pack()


root.title('Dipy: The Netflix Randomiser')

bodyText = Label(root, text="A simple Tkinter app with PyInstaller", font =('Verdana', 15), bg= 'red', fg = 'white')
bodyText.pack()
bodyText.place(x = 250, y = 350)


introText = Label(root, text="Dipy: Watch something different")
introText.pack()
root.mainloop()