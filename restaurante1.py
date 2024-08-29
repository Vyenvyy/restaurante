import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk

#config_yaay
ctk.set_appearance_mode ("light")

janela = ctk.CTk()
janela.configure(bg='ffffff')
janela.title("Restaurante do Ederson")
janela.geometry("800x600")
janela.resizable(False, False)

#imagem/função
imagem = ctk.CTkImage(
light_image=Image.open("fotocomida.png"),
dark_image=Image.open("fotocomida.png"),
size=(900, 700)
)

def imagem_tela (imagem, posicaox, posicaoy):

    image_label = ctk.CTkLabel(janela, image=imagem, text="")
    image_label.place(relx=posicaox, rely=posicaoy, anchor="center")

imagem_tela(imagem, 0.01, 0.5)

#função quadrados
def quadrados(cor, width, height,posicaox, posicaoy):
    ctk.CTkFrame(
    master = janela, 
    width= width, 
    height= height,
    fg_color = cor

    ).place(relx=posicaox, rely=posicaoy, anchor="center")

quadrados("#c4273a", 300, 50, 0.785, 0.13)

#função textos avulsos
def textos(texto, fonte, tamanho, cor_texto, fundo_texto, posicaox, posicaoy):
    bemvindo = ctk.CTkLabel(
        janela, 
        text= texto,
        font=(fonte, tamanho, "bold"),
        text_color= cor_texto,
        fg_color= fundo_texto
        )
    bemvindo.place(relx= posicaox, rely= posicaoy, anchor="center")

textos("Restaurante", "courier new", 25, "white", "#c4273a", 0.785, 0.13)
textos("Realize seu Cadastro", "courier new", 20, "black", "transparent",0.785, 0.3 )
textos("Nome:", "courier new", 18, "#c4273a", "transparent",0.669, 0.41)
textos("Senha:", "courier new", 18, "#c4273a", "transparent",0.678, 0.52)
textos("Confirmar Senha:", "courier new", 18, "#c4273a", "transparent",0.745, 0.63)

#caixas
caixanome = ctk.CTkEntry(
    janela, 
    placeholder_text="Digite aqui...", 
    width=250, 
    height=30,
    border_width = 2,
    border_color = "#c4273a"
    )
caixanome.place(relx=0.78, rely=0.46, anchor="center")

caixasenha = ctk.CTkEntry(
    janela, 
    placeholder_text="Digite aqui...", 
    show="*",
    width=250, 
    height=30,
    border_width = 2,
    border_color = "#c4273a"
    )
caixasenha.place(relx=0.78, rely=0.57, anchor="center")

caixaconfirmarsenha = ctk.CTkEntry(
    janela, 
    placeholder_text="Digite aqui...",
    show="*",
    width=250, 
    height=30,
    border_width = 2,
    border_color = "#c4273a"
    )
caixaconfirmarsenha.place(relx=0.78, rely=0.68, anchor="center")

def armazenar():
    global nome, senha, senha2, msg
    nome = caixanome.get()
    senha = caixasenha.get()
    senha2 = caixaconfirmarsenha.get()

    if nome==senha:
        msg = ctk.CTkLabel(janela,
            text = "Cadastro não realizado :(\nO nome deve ser destinto da senha.",
            font=("courier new", 15, "bold"),
            text_color = "red",
            )
        msg.place(relx=0.78, rely=0.85, anchor="center")
        msg.after(2000 , lambda: msg.destroy())
     
       
    elif senha!=senha2:
       msg = ctk.CTkLabel(janela,
            text = "Cadastro não realizado :(\nConfirmação de senha incorreta.",
            font=("courier new", 15, "bold"),
            text_color = "red"
            )
       msg.place(relx=0.78, rely=0.85, anchor="center")
       msg.after(2000 , lambda: msg.destroy())

    elif senha=="":
       msg = ctk.CTkLabel(janela,
            text = "Cadastro não realizado :(\nSenha é obrigatória",
            font=("courier new", 15, "bold"),
            text_color = "red"
            )
       msg.place(relx=0.78, rely=0.85, anchor="center")
       msg.after(2000 , lambda: msg.destroy())

    elif nome=="":
       msg = ctk.CTkLabel(janela,
            text = "Cadastro não realizado :(\nNome é obrigatório.",
            font=("courier new", 15, "bold"),
            text_color = "red"
            )
       msg.place(relx=0.78, rely=0.85, anchor="center")
       msg.after(2000 , lambda: msg.destroy())

    else:  
    # elif nome!=senha:
       msg = ctk.CTkLabel(janela,
            text = "Cadastro realizado ฅ^•ﻌ•^ฅ",
            font=("courier new", 15, "bold"),
            text_color = "green"
            )
       msg.place(relx=0.78, rely=0.85, anchor="center")
       msg.after(2000 , lambda: msg.destroy())

confirmarbotao = ctk.CTkButton(
    janela,
    text=("Confirmar"),
    font=("courier new", 15),
    width=60, 
    height=30,
    text_color = "white",
    fg_color = "#c4273a",
    hover_color = "#e34d5f",
    command = armazenar
    ).place(relx=0.78, rely=0.76, anchor="center")

janela.mainloop()