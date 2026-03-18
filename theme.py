import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from language import LANG, current_lang, COLOR
# from chat import chat2

lan = LANG[current_lang]

couleur = COLOR

# ._________________________________________________________________. #
# |						affichage du fond							| #
# |_________________________________________________________________| #
# |	base de l'app (fond d'ecran, chargement des images)				| #
# |	mise en place des Etats											| #
# |_________________________________________________________________| #

app = tk.Tk()
# app = get_app()
app.title("Hangouts")
app.config(bg=couleur["roseF"])
app.geometry("400x600")
icon = tk.PhotoImage(file="assets/logo.png")
app.iconphoto(True, icon)

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

#navbar
topFrame = tk.Frame(app, bg=couleur["bleuC"])
topFrame.pack(side="top", fill=tk.X)

# banner text
can = Canvas(app, width=400, height=600)
can.create_image(0, 0, anchor=NW, image=imgFond)
bannerTexte = tk.Label(app,
					   text=lan["slogant"],
					   font="comicsansms 16",
					   fg=couleur["violet"],
					   bg=couleur["roseF"])
bannerTexte.place(x = 100,y = 500)
can.pack()

# ._________________________________________________________________. #
# |					definition des action bouton					| #
# |_________________________________________________________________| #
# |	creation de chacun des effets bouton:							| #
# |	-le menu, le compte, l'accueil, le chat, l'exit, 				| #
# |_________________________________________________________________| #

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
			app.config(bg=couleur["roseF"])
			profil(False)
		else:
			# profil(app, True)
			bannerTexte.config(fg=couleur["violet"], bg=couleur["roseF"])
			accueilText.config(bg=couleur["bleuC"])
			topFrame.config(bg=couleur["bleuC"])
			app.config(bg=couleur["roseC"])
		btnEtat = False
	else :
		for x in range(-300, 0):
			navLateral.place(x=x, y=0)
			topFrame.update()
		if compteEtat is True:
			profil(True)
		btnEtat=True

def Accueil():
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
	if compteEtat is True:
		profil(True)
		compteEtat = False
	# else :
	# 	for x in range(-300, 0):
	# 		navLateral.place(x=x, y=0)
	# 		topFrame.update()
	# 	btnEtat=True

# permet d'afficher le chat
def Chat():
	global btnEtat
	global chatEtat
	if btnEtat is True:
		btnEtat=False
		for x in range(300):
			navLateral.place(x=-x, y=0)
			topFrame.update()
	chatEtat=True
	for x in range(-400, 1):
		ChatFrame.place(x=-x, y=48)
		topFrame.update()
	# chat2(False)

# affichage fluide du chat
# def chat2(Etat):
	# if Etat is False:
	# 	ChatFrame.config(bg = couleur["bleuF"])

def Amies():
	global btnEtat
	global amisEtat
	if btnEtat is True:
		btnEtat=False
		for x in range(300):
			navLateral.place(x=-x, y=0)
			topFrame.update()
	amisEtat=True
	for x in range(-400, 1):
		AmiesFrame.place(x=-x, y=48)
		topFrame.update()


# permet d'affiche le compte
def Compte():
	global btnEtat
	global compteEtat
	if btnEtat is True:
		btnEtat=False
		for x in range(300):
			navLateral.place(x=-x, y=0)
			topFrame.update()
	compteEtat=True
	for x in range(-400, 1):
		CompteFrame.place(x=-x, y=48)
		topFrame.update()
	# Compte2(False)

# def Compte2(Etat):
	# if Etat is False:
	# 	CompteFrame.config(bg = couleur["bleuF"])

def Quitte():
	global btnEtat
	btnEtat=False
	exit()

# ._________________________________________________________________. #
# |						  Affichage du chat  						| #
# |_________________________________________________________________| #
# |	creation de chaque objet du chat:								| #
# |	-la saisi, l'envoie, l'affichage				 				| #
# |_________________________________________________________________| #


# permet la fonction du chat
def add_to_list():
	text = entry.get()
	if text:
		text_list.insert(tk.END, text)
		entry.delete(0, tk.END)

ChatFrame = tk.Frame(app, bg=couleur["bleuF"], width=400, height=600)
ChatFrame.place(x=-400, y=0)

entry = tk.Entry(ChatFrame,
				 bg=couleur["roseC"],
				 width=38)
entry.place(x=10, y=510)

entry_btn = tk.Button(ChatFrame,
					  text=lan["enter"],
					  height=1,
					  command=add_to_list)
entry_btn.place(x=330, y=510)

text_list = tk.Listbox(ChatFrame,
					   bg=couleur["roseC"],
					   width=39,
					   height=27)
text_list.place(x=10, y=5)

# ._________________________________________________________________. #
# |						  Affichage des ami.es 						| #
# |_________________________________________________________________| #
# |																	| #
# |							 						 				| #
# |_________________________________________________________________| #

AmiesFrame = tk.Frame(app, bg=couleur["bleuF"], width=400, height=600)
AmiesFrame.place(x=-400, y=0)

listeFriend = ["Kaito", "Helga", "Yuri", "Max", "Rachel", "Nana", "Heka", "Krys", "Kai"]
y = 10
if len(listeFriend) > 0:
	for i in range(len(listeFriend)):
		tk.Frame(AmiesFrame, bg=couleur["violet"], width=50, height=50).place(x=10, y=y)
		# FriendBar = tk.Frame(AmiesFrame, bg=couleur["violet"], width=380, height=50).place(x=10, y=y)
		Name = tk.Button(AmiesFrame, text=listeFriend[i],
							 font="comicsansms 14",
							 bg=couleur["bleuF"],
							 fg=couleur["blan"],
							 width=3,
							 height=2,
							 activebackground=couleur["bleuF"],
							 command=None).place(x=60, y=y-2)
		tk.Frame(AmiesFrame, bg=couleur["violet"], width=280, height=50).place(x=112, y=y)
		ChatMsg = tk.Button(AmiesFrame, text=lan["chat"],
										bg=couleur["bleuF"],
										fg=couleur["blan"],
										width=7,
										height=1,
										activebackground=couleur["bleuF"],
										command=None).place(x=280, y=y + 10)
		y+=60

# ._________________________________________________________________. #
# |						  Affichage du compte  						| #
# |_________________________________________________________________| #
# |	creation de chaque objet du compte:								| #
# |	-le profil, les reglages, 						 				| #
# |_________________________________________________________________| #

CompteFrame = tk.Frame(app, bg=couleur["bleuF"], width=400, height=600)
CompteFrame.place(x=1, y=-600)

# affichage compte
profil = tk.Label(CompteFrame,
				  bg=couleur["violet"],
				  height=2,
				  width=5)
profil.place(x=10, y=20)

infoUsername = tk.Label(CompteFrame,
						text="Username",
						font="comicsansms 12",
						fg=couleur["violet"],
						bg=couleur["bleuF"])
infoUsername.place(x=60,y=20)
infoAmies = tk.Label(CompteFrame,
					 text=lan["friends"],
					 font="comicsansms 12",
					 fg=couleur["violet"],
					 bg=couleur["bleuF"]).place(x=60, y=40)
infoSettings = tk.Label(CompteFrame,
						text=lan["settings"],
						font="comicsansms 12",
						fg=couleur["violet"],
						bg=couleur["bleuF"]).place(x=10, y=65)

# def profil(Etat):
	# global btnEtat
	# global compteEtat
	# if btnEtat is True:
		# for x in range(300):
		# 	navLateral.place(x=-x, y=0)
		# 	topFrame.update()
		# topFrame.config(bg=couleur["bleuC"])
		# accueilText.config(bg=couleur["bleuC"])
		# app.config(bg=couleur["noir"])
		# bannerTexte.config(bg=couleur["roseC"], fg=couleur["roseC"])
		# profil = tk.Label(app,
		# 				  bg=couleur["violet"],
		# 				  height=2,
		# 				  padx=10,
		# 				  width=5,
		# 				  pady=10,
		# 				  ).place(x=10, y=60)
		# infoUsername = tk.Label(app,
		# 						text="Username",
		# 						font="comicsansms 12",
		# 						fg=couleur["violet"],
		# 						bg=couleur["blan"]).place(x=85, y=75)
		# infoAmies = tk.Label(app,
		# 					 text=lan["friends"],
		# 					 font="comicsansms 12",
		# 					 fg=couleur["violet"],
		# 					 bg=couleur["blan"]).place(x=85, y=95)
		# infoSettings = tk.Label(app,
		# 						text=lan["settings"],
		# 						font="comicsansms 12",
		# 						fg=couleur["violet"],
		# 						bg=couleur["blan"]).place(x=10, y=125)
		# btnEtat = False
		# compteEtat = True

# ._________________________________________________________________. #
# |								Navbar								| #
# |_________________________________________________________________| #
# |	creation de chaque objet du Navbar:								| #
# |	-hangout, le bouton menu										| #
# |_________________________________________________________________| #

# text navbar
accueilText = tk.Label(topFrame,
					   text="Hangouts",
					   font="comicsansms 16",
					   bg=couleur["bleuC"],
					   fg=couleur["blan"],
					   height=2,
					   padx=20)
accueilText.pack(side="right")

# navbar icone
navbarBtn = tk.Button(topFrame,
					  image=navIcon,
					  bg=couleur["bleuC"],
					  padx=20,
					  activebackground=couleur["bleuF"],
					  command=switch)
navbarBtn.place(x=5, y=5)

# ._________________________________________________________________. #
# |							Menu lateral							| #
# |_________________________________________________________________| #
# |	creation de chaque objet du menu								| #
# |	-Accueil, Compte, Amies, Chat, Aide, Quitte, fermeture			| #
# |_________________________________________________________________| #

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

# option lateral
option = [lan["home"], lan["account"], lan["friends"], lan["chat"], lan["help"], lan["exit"]]
com = [Accueil, Compte, Amies, Chat, None, Quitte]
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

# ._________________________________________________________________. #
# |					definition des fonction utils					| #
# |_________________________________________________________________| #
# |	get_app et change color											| #
# |_________________________________________________________________| #

def change_color(color):
    topFrame.config(bg=color)

def get_app():
	return app

# Que votre lumiere parvient a eclaire les autres.