import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from language import LANG, current_lang

couleur = {"noir": "#252726",
		   "violet": "#800080",
		   "blan": "#FFFFFF"}

app = tk.Tk()
# app = get_app()
app.title("Hangouts")
app.config(bg="gray30")
app.geometry("400x600")
icon = tk.PhotoImage(file="assets/logo.png")
app.iconphoto(True, icon)

#navbar
topFrame = tk.Frame(app, bg=couleur["violet"])
topFrame.pack(side="top", fill=tk.X)

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

def change_color(color):
    topFrame.config(bg=color)

def get_app():
	return app