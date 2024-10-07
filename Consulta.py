from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk




class Consulta(Frame):
    def __init__(self, parent, controller):
        global canvas, frame_scrollable
        Frame.__init__(self, parent)

        frame = Frame(self)
        frame.pack(padx=20, pady=20)

        self.image = Image.open("img/Brasão.png")  
        self.image = self.image.resize((50, 50))
        self.img = ImageTk.PhotoImage(self.image)

        img_label = Label(frame, image=self.img)
        img_label.pack(side="left", padx=10)

    
        texto_Label = Label(frame, text="Biblioteca Erico Verissimo", font=("Open Sans", 20))
        texto_Label.pack(side="left")

  
        frame_menu = Frame(self)
        frame_menu.pack(pady=10)  

    
        botao_alunos = ttk.Button(frame_menu, text="Alunos", command=self.mostrar_alunos)
        botao_alunos.pack(side="left", padx=10)

        botao_professores = ttk.Button(frame_menu, text="Professores", command=self.mostrar_professores)
        botao_professores.pack(side="left", padx=10)

        botao_livros = ttk.Button(frame_menu, text="Livros", command=lambda: print("Livros clicado"))
        botao_livros.pack(side="left", padx=10)

        canvas = Canvas(self, bg="white")
        canvas.pack(side="right", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
  
        canvas.configure(yscrollcommand=scrollbar.set)
  
        frame_scrollable = Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=frame_scrollable, anchor="nw")
   
    


    def exibir_dados(self,dados, titulo, *args):
    
            for widget in frame_scrollable.winfo_children():
                widget.destroy()

    
            titulo_label = Label(frame_scrollable, text=titulo, font=("Arial", 16), pady=10)
            titulo_label.pack()

    
            for item in dados:
                card = Frame(frame_scrollable, bg="lightgrey", bd=2, relief="raised", padx=10, pady=10)
                card.pack(fill="x", padx=10, pady=5)

                titulo_item = Label(card, text=f"Nome: {item['nome']}", font=("Arial", 12, "bold"), bg="lightgrey")
                titulo_item.grid(column=0, row=0,sticky='w')

                descricao_item = Label(card, text=f"Descrição: {item['descricao']}", bg="lightgrey")
                descricao_item.grid(column=0 ,row=1,sticky='w')

                descricao_item = Label(card, text=f"Descrição: {item['descricao']}", bg="lightgrey")
                descricao_item.grid(column=1 ,row=1,sticky='w')

                descricao_item = Label(card, text=f"Descrição: {item['descricao']}", bg="lightgrey")
                descricao_item.grid(column=2 ,row=1,sticky='w')

        
            frame_scrollable.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))


    def mostrar_alunos(self, *args):
            dados_alunos = [
            {"nome": "João", "descricao": "Aluno do 3º ano"},
            {"nome": "Maria", "descricao": "Aluna do 2º ano"},
            {"nome": "Carlos", "descricao": "Aluno do 1º ano"},
            {"nome": "Ana", "descricao": "Aluna do 3º ano"},
            {"nome": "Pedro", "descricao": "Aluno do 4º ano"},
            {"nome": "Lucas", "descricao": "Aluno do 5º ano"},
            
            ]
            self.exibir_dados(dados_alunos, "Lista de Alunos")

    def mostrar_professores(self, *args):
            dados_professores = [
            {"nome": "Professor Silva", "descricao": "Matemática"},
            {"nome": "Professora Souza", "descricao": "Português"},
            ]
            self.exibir_dados(dados_professores, "Lista de Professores")

    
