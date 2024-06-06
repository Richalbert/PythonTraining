# print("Hello World")

# import sys
# print(sys.version)

# print("Premiere version a sauver dans mon GitHub")

# print("Seconde version")


import tkinter

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

app.config(menu=mainmenu)

# Rendre la fenetre active
app.mainloop()


