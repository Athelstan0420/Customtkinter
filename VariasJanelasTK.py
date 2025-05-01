import tkinter as Tk


janela = Tk.Tk()
janela.geometry("300x300")

def nova_janela1():

    janela2 = Tk.Toplevel()
    botao1 = Tk.Button(janela2, text="Fechar", command=janela2.destroy)
    botao1.grid(padx=20, pady=100)


botao = Tk.Button(janela, text="New window", command=nova_janela1)
botao.grid(padx=20, pady=100)


janela.mainloop()

