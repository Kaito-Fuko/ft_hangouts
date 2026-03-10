import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
# from theme import btnEtat
from language import LANG, current_lang

lan = LANG[current_lang]

couleur = {"noir": "#252726",
		   "violet": "#6F6D9E",
		   "blan": "#FFFFFF",
		   "roseC": "#F5BFDA",
		   "roseF": "#E493CA",
		   "bleuC": "#C2D8F7",
		   "bleuF": "#99AFE7"}


# def profil(app, Etat):

# 	print(Etat)
# 	imgFond = PhotoImage(file='assets/fond.png')

# 	can = Canvas(app, width=390, height=600)
# 	can.create_image(0, 0, anchor=NW, image=imgFond)
# 	bannerTexte = tk.Label(app,
# 						   text="Que votre lumiere parvient\na eclaire les autres.",
# 						   font="comicsansms 16",
# 						   fg=couleur["violet"],
# 						   bg=couleur["roseF"])
# 	bannerTexte.place(x = 100,y = 500)
# 	can.pack()

# 	profil = tk.Label(app,
# 					  bg=couleur["violet"],
# 					  height=2,
# 					  width=5,
# 					  padx=10,
# 					  pady=10,)
# 	infoUsername = tk.Label(app,
# 							text="Username",
# 							font="comicsansms 12",
# 							fg=couleur["violet"],
# 							bg=couleur["blan"])
# 	infoAmies = tk.Label(app,
# 							text=lan["friends"],
# 							font="comicsansms 12",
# 							fg=couleur["violet"],
# 							bg=couleur["blan"])
# 	infoSettings = tk.Label(app,
# 							text=lan["settings"],
# 							font="comicsansms 12",
# 							fg=couleur["violet"],
# 							bg=couleur["blan"])
# 	if Etat is True:
# 		profil.place(x=-85, y=60)
# 		infoUsername.place(x=-85, y=75)
# 		infoAmies.place(x=-85, y=95)
# 		infoSettings.place(x=-85, y=125)
# 	else:
# 		profil.place(x=10, y=60)
# 		infoUsername.place(x=85, y=75)
# 		infoAmies.place(x=85, y=95)
# 		infoSettings.place(x=10, y=125)