import tkinter
from tkinter import *
from PIL import ImageTk, Image



# Creation de la fenetre
app = tkinter.Tk()
app.title('Mon application')
app.geometry("640x480+20+20")


# Creation d'un canvas pour afficher l'image
canvas = tkinter.Canvas(app, width=640, height=480)
canvas.pack()

# Chargement de l'image
chemin = 'Cosmic_Microwave_Background_(CMB).jpeg'
image = Image.open(chemin)
image2 = ImageTk.PhotoImage(image)


# Affichage de l'image sur le canvas
canvas.create_image(0, 0, anchor=tkinter.NW, image=image2)




app.mainloop()