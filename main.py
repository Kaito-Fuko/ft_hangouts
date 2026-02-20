import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from database import create_table
from home import HomeFrame
from theme import change_color, get_app
import time

# Dico couleur
couleur = {"noir": "#252726",
		   "violet": "#800080",
		   "blan": "#FFFFFF"}

app = get_app()
home = HomeFrame(app)
create_table()
home.pack(fill="both", expand=True)

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