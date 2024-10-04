from tkinter import *
from PIL import Image, ImageTk

JanelaLogin = Tk()

JanelaLogin.title("Login")
JanelaLogin.geometry("430x600")

frame = Frame(JanelaLogin)
frame.pack(padx=20,pady=20)

image = Image.open("img/Brasão.png")
image = image.resize((50,50))
img = ImageTk.PhotoImage(image)

img_label = Label(frame,image=img)
img_label.pack(side="left",padx=10)

texto_Label = Label(frame,text="Biblioteca Erico Verissimo", font=("Open Sans", 20))
texto_Label.pack(side="left")


frame_form = Frame(JanelaLogin, bg="lightgray", padx=20, pady=20)
frame_form.pack(padx=20, pady=20, fill="x")


cpf_label = Label(frame_form, text="CPF:", bg="lightgray")
cpf_label.grid(row=0, column=0, sticky="w", pady=5)
cpf_entry = Entry(frame_form)
cpf_entry.grid(row=0, column=1, pady=5)

 
password_label = Label(frame_form, text="Senha:", bg="lightgray")
password_label.grid(row=1, column=0, sticky="w", pady=5)
password_entry = Entry(frame_form, show="*")
password_entry.grid(row=1, column=1, pady=5)

   
login_button = Button(frame_form, text="Login", command=lambda: print("Login clicado!"))
login_button.grid(row=2, columnspan=2, pady=10)

JanelaLogin.mainloop()