##

https://github.com/TomSchimansky/CustomTkinter


<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvj-nSZev-z_mo4w5RLXfc2OI5WCWNSRB5aPNuyq4D815WK3AkhMhWiRiT&s=10"/>

##

# LOGIN 🪪📨:
  
    import customtkinter 
    #Costumtkinter é a mesma coisa do tkinter só que você pode personalizar de maneira mais dinâmica.
    
    customtkinter.set_appearance_mode("dark") # Cor de fundo
    
    def cliqueBotao2():
        user = email.get() #Apara adquirir o dado digitado.
        key = senha.get()
    
        if user == "ifpe.edu.br" and key == "1234":
            feedbackLogin.configure(text="Login realizado com sucesso! ", text_color="green") # "Configure" permite alterar propriedades de um elemento
        else:
            feedbackLogin.configure(text="Login incorreto", text_color="red")
    
    janela = customtkinter.CTk()
    #janela.geometry("300x300") #Tamanho da janela
    janela.title("Sistema de Login") #Para o título da janela
    
    texto = customtkinter.CTkLabel(janela, text=" Fazer Login") #Label é um texto de exibição.
    texto.pack(padx=10, pady=10)
    
    email = customtkinter.CTkEntry(janela, placeholder_text="Seu email") #Toda entrada de informação vc utiliza o "Entry"
    email.pack(padx=10, pady=10)
    
    senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
    senha.pack(padx=10, pady=10)
    
    checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar Login")
    checkbox.pack(padx=10, pady=10)
    
    botão2 = customtkinter.CTkButton(janela, text="Login",command=cliqueBotao2)
    botão2.pack(padx=10, pady=10)
    
    feedbackLogin = customtkinter.CTkLabel(janela, text="")
    feedbackLogin.pack(padx=10, pady=10)
    
    janela.mainloop() #Para rodar a janela. 


##
![image](https://github.com/user-attachments/assets/6fcb5d34-d519-40f9-9067-7f4d8acb4b70)
