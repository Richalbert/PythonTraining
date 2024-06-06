# print("Hello World")

# import sys
# print(sys.version)

# print("Premiere version a sauver dans mon GitHub")

# print("Seconde version")


import tkinter
#from tkinter import *

# Creation de la fenetre principale avec un menu
app = tkinter.Tk()

# Un titre pour la fenetre
app.title('Mon application')

# Position de la fenetre "largeurxhauteu+x+y"
app.geometry("640x480+20+20")

# Ajout d'un widget Menu
mainmenu = tkinter.Menu(app)

# Creation de 2 menus File et Edit
menu1 = tkinter.Menu(mainmenu)
menu1.add_command(label='Nouveau')
menu1.add_command(label='Ouvrir')
menu1.add_command(label='Enregistrer')

menu2 = tkinter.Menu(mainmenu)
menu2.add_command(label='Couper')
menu2.add_command(label='Copier')
menu2.add_command(label='Coller')

menu3 = tkinter.Menu(mainmenu)
menu3.add_command(label='Afficher')
menu3.add_command(label='Zoomer')
menu3.add_command(label='Info')

mainmenu.add_cascade(label='Fichier', menu=menu1)
mainmenu.add_cascade(label='Edition', menu=menu2)
mainmenu.add_cascade(label='Outils', menu=menu3)


# Ajout d'une case a cocher
bouton = tkinter.Checkbutton(app, text='Confirmer')
bouton.pack()

# Ajout d'une liste
liste = tkinter.Listbox(app)
liste.insert(1, "Python")
liste.insert(2, "Html")
liste.insert(3, "C")
liste.insert(4, "C++")
liste.insert(5, "Java")
liste.pack()

# Ajout d'un bouton
bouton1 = tkinter.Button(app, text='Annuler')
bouton1.pack(side=tkinter.LEFT, padx=5, pady=5)

# Ajout d'un spinbox
spinbox = tkinter.Spinbox(app, from_=0, to=10)
spinbox.pack()

# Ajout d'un curseur
valeur = tkinter.DoubleVar()
echelle = tkinter.Scale(app, variable=valeur)
echelle.pack()


# Ajout d'une boite de dialogue



app.config(menu=mainmenu)

# Rendre la fenetre active
app.mainloop()


