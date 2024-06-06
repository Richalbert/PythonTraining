# print("Hello World")

# import sys
# print(sys.version)

# print("Premiere version a sauver dans mon GitHub")

# print("Seconde version")


import tkinter

# Creation de la fenetre principale
fenetre = tkinter.Tk()

# Un titre pour la fenetre
fenetre.title('Fenetre principale')

# Position de la fenetre "largeurxhauteu+x+y"
fenetre.geometry("640x480+0+0")

# # Les dimensions de la fenetre
# largeur = 440
# hauteur = 280
# fenetre.minsize(largeur, hauteur)
# fenetre.maxsize(largeur+200, hauteur+200)

# Pour bloquer le redimensionnement de la fenetre ou pas
fenetre.resizable(width=False, height=True)

# Rendre la fenetre active
fenetre.mainloop()


