import tkinter as tk
from Login import Login
from Consulta import Consulta
from Cadastro import Cadastro

class NavegacaoApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
       
        self.title("Sistema de Biblioteca")
        self.geometry("800x600")
        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        
        for F in (Login,Consulta,Cadastro):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        
        self.mostrar_frame("Login")
    
    def mostrar_frame(self, page_name):
        """Exibe a página solicitada"""
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = NavegacaoApp()
    app.mainloop()
