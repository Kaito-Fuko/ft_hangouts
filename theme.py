import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from language import LANG, current_lang

lan = LANG[current_lang]

couleur = {"noir": "#252726",
		   "violet": "#6F6D9E",
		   "blan": "#FFFFFF",
		   "roseC": "#F5BFDA",
		   "roseF": "#F5ACC6",
		   "bleuC": "#C2D8F7",
		   "bleuF": "#99AFE7"}

app = tk.Tk()
# app = get_app()
app.title("Hangouts")
app.config(bg="white")
app.geometry("400x600")
icon = tk.PhotoImage(file="assets/logo.png")
app.iconphoto(True, icon)

#navbar
topFrame = tk.Frame(app, bg=couleur["bleuC"])
topFrame.pack(side="top", fill=tk.X)

# para fonction
btnEtat = False
compteEtat = False
amisEtat = False
chatEtat = False
helpEtat = False


# charge image nav
navIcon = PhotoImage(file='assets/menu.png')
closeIcon = PhotoImage(file='assets/croix.png')
imgFond = PhotoImage(file='assets/fond.png')

# definir switch
def switch():
	global btnEtat
	global compteEtat
	if btnEtat is True:
		for x in range(300):
			navLateral.place(x=-x, y=0)
			topFrame.update()
		if compteEtat is True:
			bannerTexte.config(fg=couleur["roseC"], bg=couleur["roseC"])
			accueilText.config(bg=couleur["bleuC"])
			topFrame.config(bg=couleur["bleuC"])
			app.config(bg=couleur["roseC"])
		else:
			bannerTexte.config(fg=couleur["violet"], bg=couleur["blan"])
			accueilText.config(bg=couleur["bleuC"])
			topFrame.config(bg=couleur["bleuC"])
			app.config(bg=couleur["roseC"])
		btnEtat = False
	else :
		for x in range(-300, 0):
			navLateral.place(x=x, y=0)
			topFrame.update()
		btnEtat=True

def accueil():
	global btnEtat
	global compteEtat
	if btnEtat is True:
		for x in range(300):
			navLateral.place(x=-x, y=0)
			topFrame.update()
		bannerTexte.config(fg=couleur["violet"], bg=couleur["blan"])
		accueilText.config(bg=couleur["bleuC"])
		topFrame.config(bg=couleur["bleuC"])
		app.config(bg=couleur["roseC"])
		btnEtat = False
		compteEtat = False
	else :
		for x in range(-300, 0):
			navLateral.place(x=x, y=0)
			topFrame.update()
		btnEtat=True

# text navbar
accueilText = tk.Label(topFrame,
					   text="Hangouts",
					   font="comicsansms 16",
					   bg=couleur["bleuC"],
					   fg=couleur["blan"],
					   height=2,
					   padx=20)
accueilText.pack(side="right")

# banner text
can = Canvas(app, width=400, height=600)
can.create_image(0, 0, anchor=NW, image=imgFond)
bannerTexte = tk.Label(app,
					   text="Que votre lumiere parvient\na eclaire les autres.",
					   font="comicsansms 16",
					   fg=couleur["violet"],
					   bg=couleur["blan"])
bannerTexte.place(x = 100,y = 500)
can.pack()

# Que votre lumiere parvient a eclaire les autres.

# navbar icone
navbarBtn = tk.Button(topFrame,
					  image=navIcon,
					  bg=couleur["bleuC"],
					  padx=20,
					  activebackground=couleur["bleuF"],
					  command=switch)
navbarBtn.place(x=5, y=5)

#bar lateral
navLateral = tk.Frame(app, bg=couleur["roseC"], width=300, height=600)
navLateral.place(x=-300, y=0)
tk.Label(navLateral,
		 font="comicsansms 16",
		 bg=couleur["bleuC"],
		 fg=couleur["bleuF"],
		 width=300,
		 height=2,
		 padx=20
		 ).place(x=0, y=0)
y = 80

def Compte():
	global btnEtat
	global compteEtat
	if btnEtat is True:
		for x in range(300):
			navLateral.place(x=-x, y=0)
			topFrame.update()
		topFrame.config(bg=couleur["bleuC"])
		accueilText.config(bg=couleur["bleuC"])
		app.config(bg=couleur["noir"])
		bannerTexte.config(bg=couleur["roseC"], fg=couleur["roseC"])
		profil = tk.Label(app,
						  bg=couleur["violet"],
						  height=2,
						  width=5,
						  padx=10,
						  pady=10,
						  ).place(x=10, y=60)
		infoUsername = tk.Label(app,
								text="Username",
								font="comicsansms 12",
								fg=couleur["violet"],
								bg=couleur["blan"]).place(x=85, y=75)
		infoAmies = tk.Label(app,
							 text=lan["friends"],
							 font="comicsansms 12",
							 fg=couleur["violet"],
							 bg=couleur["blan"]).place(x=85, y=95)
		infoSettings = tk.Label(app,
								text=lan["settings"],
								font="comicsansms 12",
								fg=couleur["violet"],
								bg=couleur["blan"]).place(x=10, y=125)
		btnEtat = False
		compteEtat = True

def Quitte():
	global btnEtat
	btnEtat=False
	exit()

# option lateral
option = [lan["home"], lan["account"], lan["friends"], lan["chat"], lan["help"], lan["exit"]]
com = [accueil, Compte, None, None, None, Quitte]
#com = [switch, Compte, Amies, Chat, Aide, Quitte]

# position option

for i in range(6):
	tk.Button(navLateral, text=option[i],
						  font="comicsansms 16",
						  bg=couleur["roseC"],
						  fg=couleur["blan"],
						  activebackground=couleur["roseF"],
						  command=com[i]
			 ).place(x=25, y=y)
	y += 40

# BOUTON fermeture
fermeBtn = tk.Button(navLateral,
					 image=closeIcon,
					 bg=couleur["bleuC"],
					 activebackground=couleur["bleuF"],
					 command=switch)
fermeBtn.place(x=255, y=5)

def change_color(color):
    topFrame.config(bg=color)

def get_app():
	return app