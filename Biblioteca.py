from tkinter import *
from PIL import Image, ImageTk

JanelaLogin = Tk()

JanelaLogin.title("Login")

frame = Frame(JanelaLogin)
frame.pack(padx=20,pady=20)

image = Image.open("img/Brasão.png")
image = image.resize((50,50))
img = ImageTk.PhotoImage(image)

img_label = Label(frame,image=img)
img_label.pack(side="left",padx=10)

texto_Label = Label(frame,text="Biblioteca Erico Verissimo", font=("Open Sans", 20))
texto_Label.pack(side="left")

JanelaLogin.mainloop()