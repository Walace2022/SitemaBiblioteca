from tkinter import *
from PIL import Image, ImageTk

#Tela exemplo de cadastro

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

frame_form.grid_columnconfigure(1, weight=1)


Nome_label = Label(frame_form, text="Nome:", bg="lightgray")
Nome_label.grid(row=0, column=0, sticky="w", pady=5)
Nome_entry = Entry(frame_form)
Nome_entry.grid(row=0, column=1,sticky="we", pady=5)

cpf_label = Label(frame_form, text="CPF:", bg="lightgray")
cpf_label.grid(row=1, column=0, sticky="w", pady=5)
cpf_entry = Entry(frame_form)
cpf_entry.grid(row=1, column=1, sticky="we",pady=5)

Endereco_label = Label(frame_form, text="Endereço:", bg="lightgray")
Endereco_label.grid(row=2, column=0, sticky="w", pady=5)
Endereco_entry = Entry(frame_form)
Endereco_entry.grid(row=2, column=1, sticky="we",pady=5)

Telefone_label = Label(frame_form, text="Telefone:", bg="lightgray")
Telefone_label.grid(row=3, column=0, sticky="w", pady=5)
Telefone_entry = Entry(frame_form)
Telefone_entry.grid(row=3, column=1, sticky="we", pady=5)
   
login_button = Button(frame_form, text="Cadastrar", command=lambda: print("Cadastrado!"))
login_button.grid(row=8, columnspan=2, pady=10)

JanelaLogin.mainloop()