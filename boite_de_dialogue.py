import tkinter
import tkinter.messagebox


# Creation de la fenetre
app = tkinter.Tk()
app.title('Mon application')
app.geometry("640x480+20+20")


def supprimer_fichier():
    titre = 'Supprimer le fichier'
    message = 'Voulez vous vraiment supprimer ce fichier de facon permanente'
    if tkinter.messagebox.askyesno(title=titre, message=message):
        titre = 'Supprimer le fichier'
        message = 'Ce fichier ne peut pas etre supprime'
        tkinter.messagebox.showwarning(title=titre, message=message)
    else:
        titre = 'Annulation'
        message = 'Fichier non supprime'
        tkinter.messagebox.showinfo(title=titre, message=message)


bouton = tkinter.Button(text='Supprimer', command=supprimer_fichier)
bouton.pack()

app.mainloop()