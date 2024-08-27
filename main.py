from tkinter import *
import tkinter as tk
import os

root = tk.Tk()
root.geometry("200x200")
root.resizable(False, False)
root.title("carteira")
lbl1 = tk.Label(root, text="Olá **********!\n\n1.3 Bitcoins disponíveis\n\n", font="Arial 13")
lbl1.pack()
lbl2 = tk.Label(root, text="Seu pix:", font="Arial 13 bold")
lbl2.pack()
etr1 = tk.Entry(root, width=15)
etr1.pack()

def criar_janela():
    # Cria uma instância da janela
    janela = tk.Toplevel(root)
    
    # Configura o título da janela
    janela.title("Sistema comprometido")
    janela.configure(bg="pink")
    # Cria um label na janela
    label = tk.Label(janela, text=" VOCÊ FOI HACKEADO",bg="pink",fg="black", font="Arial 30 bold")
    label.pack()
    
    # Aguarda 2 segundos antes de fechar a janela
    janela.after(2000, janela.destroy)

def k():
    for i in range(200):
        criar_janela()
    os.system("shutdown -i")
    

btn1 = tk.Button(root, text="Enviar", command=k)
btn1.pack()

root.mainloop()
