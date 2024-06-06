import tkinter



# Creation de la fenetre
app = tkinter.Tk()
app.title('Mon application')
app.geometry("640x480+20+20")


# Changer l'icone de la fenetre
# il faut convertir l'image en .ico
# https://convertio.co/fr/png-ico/
app.iconbitmap('Tux.ico')


# Changer la couleur de fond
app.config(background='#FF0000')



# Ajouter une image
#   1ere Methode avec une conversion du fichier en .gif
#       
#   2ieme methode en inserant directement l'image
#   mais avec l'importation d'un package
#
# # 1ere methode
# # on dimensionne l'image
# canvas = tkinter.Canvas(app, width=640, height=480)
# image = tkinter.PhotoImage(file='Polarisation_of_the_CMB.gif')
# canvas.create_image(0, 0, anchor=tkinter.NW, image=image)

# 2ieme Methode 
from PIL import ImageTk, Image

canvas = tkinter.Canvas(app, width=640, height=480)
image2 = ImageTk.PhotoImage('Cosmic_Microwave_Background_(CMB).jpeg')
canvas.create_image(0, 0, anchor=tkinter.NW, image=image2)




canvas.pack()

app.mainloop()