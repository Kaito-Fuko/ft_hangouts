import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from database import create_table
from home import HomeFrame
from language import LANG, current_lang
from theme import change_color
import time

# Dico couleur
couleur = {"noir": "#252726",
		   "violet": "#800080",
		   "blan": "#FFFFFF"}

# Para fenetre
app = tk.Tk()
home = HomeFrame(app)
create_table()
home.pack(fill="both", expand=True)
app.title("Hangouts")
app.config(bg="gray30")
app.geometry("400x600")
icon = tk.PhotoImage(file="assets/logo.png")
app.iconphoto(True, icon)

# para Switch
btnEtat = False

# charge image nav
navIcon = PhotoImage(file='assets/menu.png')
closeIcon = PhotoImage(file='assets/croix.png')
imgFond = PhotoImage(file='assets/logo.png')

# definir switch
def switch():
	global btnEtat
	if btnEtat is True:
		for x in range(300):
			navLateral.place(x=-x, y=0)
			topFrame.update()
		bannerTexte.config(fg=couleur["violet"])
		accueilText.config(bg=couleur["violet"])
		topFrame.config(bg=couleur["violet"])
		app.config(bg="gray30")
		btnEtat = False
	else :
		for x in range(-300, 0):
			navLateral.place(x=x, y=0)
			topFrame.update()
		btnEtat=True

#navbar
topFrame = tk.Frame(app, bg=couleur["violet"])
topFrame.pack(side="top", fill=tk.X)

# text navbar
accueilText = tk.Label(topFrame,
					   text="Hangouts",
					   font="comicsansms 16",
					   bg=couleur["violet"],
					   fg=couleur["blan"],
					   height=2,
					   padx=20)
accueilText.pack(side="right")

# banner text
can = Canvas(app, width=400, height=600)
can.create_image(0, 0, anchor=NW, image=imgFond)
bannerTexte = tk.Label(app,
					   text="chat",
					   font="comicsansms 16",
					   fg=couleur["violet"])
bannerTexte.place(x = 180,y = 400)
can.pack()

# navbar icone
navbarBtn = tk.Button(topFrame,
					  image=navIcon,
					  bg=couleur["violet"],
					  padx=20,
					  activebackground=couleur["noir"],
					  command=switch)
navbarBtn.place(x=10, y=10)

#bar lateral
navLateral = tk.Frame(app, bg="gray30", width=300, height=600)
navLateral.place(x=-300, y=0)
tk.Label(navLateral,
		 font="comicsansms 16",
		 bg=couleur["violet"],
		 fg=couleur["noir"],
		 width=300,
		 height=2,
		 padx=20
		 ).place(x=0, y=0)
y = 80

lan = LANG[current_lang]

# option lateral
option = [lan["home"], lan["account"], lan["friends"], lan["chat"], lan["help"], lan["exit"]]

# position option

for i in range(6):
	tk.Button(navLateral, text=option[i], font="comicsansms 16", bg="gray30", fg=couleur["blan"], activebackground=couleur["noir"]).place(x=25, y=y)
	y += 40

# BOUTON fermeture
fermeBtn = tk.Button(navLateral,
					 image=closeIcon,
					 bg=couleur["violet"],
					 activebackground=couleur["noir"],
					 command=switch)
fermeBtn.place(x=250, y=10)

# envoie msg
def send_message(contact_id, sender, content):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO messages(contact_id, sender, content)
        VALUES (?, ?, ?)
    """, (contact_id, sender, content))

    conn.commit()
    conn.close()

# read msg
def get_messages(contact_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT sender, content FROM messages
        WHERE contact_id=?
    """, (contact_id,))

    data = cursor.fetchall()
    conn.close()
    return data

# livecycle android
last_time = None

def leave(event):
    global last_time
    last_time = time.strftime("%H:%M:%S")

def return_app(event):
    if last_time:
        print("App quitté à :", last_time)

app.bind("<FocusOut>", leave)
app.bind("<FocusIn>", return_app)

app.mainloop()





























#You will have to complete various tasks that will help you understand how a mobile app works.
#The goal is to create an app that allows users to create contacts (containing at least 5 details), edit them, and delete them. Once a contact is saved, the user should be able to communicate with them through text messages.
#Contacts will be recorded persistently using an SQLite database. Do not use the shared contact table and create your own. A summary for each contact will appear as a list on the app’s homepage. You should be able to click on each contact to view their details.
#Your app will have to propose two different languages, one being the default language (change the system language for a test). When you’re on the homepage and set the app in the background, the date will be saved and will show in a toast when you return to the front. You will have to create a menu that will allow you to change the app’s header color. Finally, the app icon will have to be the 42 logo.
#• You’re free to use whatever language.
#• No external library is allowed (even for design)
#In case you choose Android, it is strongly advised that you use
#Android Studio as your IDE. Beware, Google does not support the ADT
#plugin for Eclipse anymore.Here is what you will have to create :
#• Create a contact.
#• Edit a contact.
#• Delete a contact.
#• Homepage with a summary for each contact.
#• Receive text messages from recorded contacts.
#• Send text messages to your contacts.
#• You have a clear conversation history that properly shows the sender and the receiver.
#• Create a menu that will allow you to change the header color.
#• The app will have to include two different languages.
#• Show the time the app was set in the background when returning to the app.
#• The app works in landscape and portrait modes.
#• The app icon is the 42 logo.