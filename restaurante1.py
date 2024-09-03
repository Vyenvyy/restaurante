import customtkinter as ctk
from PIL import Image, ImageTk

#Configuração Janela principal
ctk.set_appearance_mode ("light")

janela = ctk.CTk()
janela.configure(bg='ffffff')
janela.title("Restaurante do Ederson")
janela.geometry("800x600")
janela.resizable(False, False)

#def pra fechar janela
def fechar_janela():
    janela1.pack_forget()
    janela2.pack(fill="both", expand = True)


#frame Janela 1 = Login -------------------------------------------------------------------------------------
janela1 = ctk.CTkFrame(janela)
janela1.pack(fill="both", expand = True)

#função quadrados
def quadrados(cor, width, height,posicaox, posicaoy):
    ctk.CTkFrame(
    master = janela1, 
    width= width, 
    height= height,
    fg_color = cor

    ).place(relx=posicaox, rely=posicaoy, anchor="center")
quadrados("white", 900, 700, 0.5, 0.5)
quadrados("#c4273a", 300, 50, 0.785, 0.17)

#imagem/função
imagem = ctk.CTkImage(
light_image=Image.open("fotocomida.png"),
dark_image=Image.open("fotocomida.png"),
size=(900, 700)
)

def imagem_tela (imagem, posicaox, posicaoy):

    image_label = ctk.CTkLabel(janela1, image=imagem, text="")
    image_label.place(relx=posicaox, rely=posicaoy, anchor="center")

imagem_tela(imagem, 0.01, 0.5)

#função textos avulsos
def textos(texto, fonte, tamanho, cor_texto, fundo_texto, posicaox, posicaoy):
    bemvindo = ctk.CTkLabel(
        janela1, 
        text= texto,
        font=(fonte, tamanho, "bold"),
        text_color= cor_texto,
        fg_color= fundo_texto
        )
    bemvindo.place(relx= posicaox, rely= posicaoy, anchor="center")

textos("Restaurante", "courier new", 25, "white", "#c4273a", 0.785, 0.17)
textos("Realize seu Cadastro", "courier new", 20, "black", "white",0.785, 0.3 )
textos("Nome:", "courier new", 18, "#c4273a", "white",0.669, 0.41)
textos("Senha:", "courier new", 18, "#c4273a", "white",0.678, 0.52)
textos("Confirmar Senha:", "courier new", 18, "#c4273a", "white",0.745, 0.63)
textos("――――――――――――――――", "courier new", 25, "#c4273a", "white", 0.785, 0.34)

#caixas
caixanome = ctk.CTkEntry(
    janela1, 
    placeholder_text="Digite aqui...", 
    width=250, 
    height=30,
    border_width = 2,
    border_color = "#c4273a"
    )
caixanome.place(relx=0.78, rely=0.46, anchor="center")

caixasenha = ctk.CTkEntry(
    janela1, 
    placeholder_text="Digite aqui...", 
    show="*",
    width=250, 
    height=30,
    border_width = 2,
    border_color = "#c4273a"
    )
caixasenha.place(relx=0.78, rely=0.57, anchor="center")

caixaconfirmarsenha = ctk.CTkEntry(
    janela1, 
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
        msg = ctk.CTkLabel(janela1,
            text = "Cadastro não realizado :(\nO nome deve ser destinto da senha.",
            font=("courier new", 15, "bold"),
            text_color = "red",
            fg_color = "white"
            )
        msg.place(relx=0.78, rely=0.85, anchor="center")
        msg.after(2000 , lambda: msg.destroy())
     
       
    elif senha!=senha2:
       msg = ctk.CTkLabel(janela1,
            text = "Cadastro não realizado :(\nConfirmação de senha incorreta.",
            font=("courier new", 15, "bold"),
            text_color = "red",
            fg_color = "white"
            )
       msg.place(relx=0.78, rely=0.85, anchor="center")
       msg.after(2000 , lambda: msg.destroy())

    elif senha=="":
       msg = ctk.CTkLabel(janela1,
            text = "Cadastro não realizado :(\nSenha é obrigatória",
            font=("courier new", 15, "bold"),
            text_color = "red",
            fg_color = "white"
            )
       msg.place(relx=0.78, rely=0.85, anchor="center")
       msg.after(2000 , lambda: msg.destroy())

    elif nome=="":
       msg = ctk.CTkLabel(janela1,
            text = "Cadastro não realizado :(\nNome é obrigatório.",
            font=("courier new", 15, "bold"),
            text_color = "red",
            fg_color = "white"
            )
       msg.place(relx=0.78, rely=0.85, anchor="center")
       msg.after(2000 , lambda: msg.destroy())

    else:  
    # elif nome!=senha:
       msg = ctk.CTkLabel(janela1,
            text = "Cadastro realizado ฅ^•ﻌ•^ฅ",
            font=("courier new", 15, "bold"),
            text_color = "green",
            fg_color = "white"
            )
       msg.place(relx=0.78, rely=0.85, anchor="center")
       msg.after(2000 , lambda: msg.destroy())
       botao_fechar = ctk.CTkButton(janela1, 
       text=("Ir ao Cardápio"),
       font=("courier new", 15),
       width=60, 
       height=30,
       text_color = "white",
       fg_color = "#c4273a",
       hover_color = "#e34d5f",
       command = fechar_janela
       ).place(relx=0.78, rely=0.76, anchor="center")

confirmarbotao = ctk.CTkButton(
    janela1,
    text=("Confirmar"),
    font=("courier new", 15),
    width=60, 
    height=30,
    text_color = "white",
    fg_color = "#c4273a",
    hover_color = "#e34d5f",
    command = armazenar
    ).place(relx=0.78, rely=0.76, anchor="center")

#frame Janela 2 = Cardápio -------------------------------------------------------------------------------------

janela2 = ctk.CTkFrame(janela)

#imagem/função
imagem = ctk.CTkImage(
light_image=Image.open("Cardápio.png"),
dark_image=Image.open("Cardápio.png"),
size=(800, 600)
)

def imagem_tela (janela, imagem, posicaox, posicaoy):

    image_label = ctk.CTkLabel(janela, image=imagem, text="")
    image_label.place(relx=posicaox, rely=posicaoy, anchor="center")

imagem_tela(janela2, imagem, 0.5, 0.5)

#Opções do cardápio

def entradas_pag():
    for widget in janela2.winfo_children():
        widget.destroy()
    foto1 = ctk.CTkImage(
    light_image=Image.open("Entradas.png"),
    dark_image=Image.open("Entradas.png"),
    size=(800, 600)
    )
    image_label = ctk.CTkLabel(janela2, image=foto1, text="")
    image_label.place(relx=0.5, rely=0.5, anchor="center")

def principais_pag():
    for widget in janela2.winfo_children():
        widget.destroy()
    foto1 = ctk.CTkImage(
    light_image=Image.open("Principais.png"),
    dark_image=Image.open("Principais.png"),
    size=(800, 600)
    )
    image_label = ctk.CTkLabel(janela2, image=foto1, text="")
    image_label.place(relx=0.5, rely=0.5, anchor="center")

def bebidas_pag():
    for widget in janela2.winfo_children():
        widget.destroy()
    foto1 = ctk.CTkImage(
    light_image=Image.open("Bebidas.png"),
    dark_image=Image.open("Bebidas.png"),
    size=(800, 600)
    )
    image_label = ctk.CTkLabel(janela2, image=foto1, text="")
    image_label.place(relx=0.5, rely=0.5, anchor="center")

def alcoolicas_pag():
    for widget in janela2.winfo_children():
        widget.destroy()
    foto1 = ctk.CTkImage(
    light_image=Image.open("Alcolicas.png"),
    dark_image=Image.open("Alcolicas.png"),
    size=(800, 600)
    )
    image_label = ctk.CTkLabel(janela2, image=foto1, text="")
    image_label.place(relx=0.5, rely=0.5, anchor="center")

def sobremesas_pag():
    for widget in janela2.winfo_children():
        widget.destroy()
    foto1 = ctk.CTkImage(
    light_image=Image.open("Sobremesas.png"),
    dark_image=Image.open("Sobremesas.png"),
    size=(800, 600)
    )
    image_label = ctk.CTkLabel(janela2, image=foto1, text="")
    image_label.place(relx=0.5, rely=0.5, anchor="center")

def pratochefe_pag():
    for widget in janela2.winfo_children():
        widget.destroy()
    foto1 = ctk.CTkImage(
    light_image=Image.open("Chefe.png"),
    dark_image=Image.open("Chefe.png"),
    size=(800, 600)
    )
    image_label = ctk.CTkLabel(janela2, image=foto1, text="")
    image_label.place(relx=0.5, rely=0.5, anchor="center")

def confirmarbotao(eixox, eixoy, command):
    confirmarbotao=ctk.CTkButton(
        janela2,
        text="Visualizar",
        font=("courier new", 15),
        width=60, 
        height=30,
        text_color="white",
        fg_color="#c4273a",
        hover_color="#e34d5f",
        command=command
    ).place(relx=eixox, rely=eixoy, anchor="center")

confirmarbotao(0.32, 0.52, entradas_pag)
confirmarbotao(0.5, 0.52, principais_pag)
confirmarbotao(0.685, 0.52, bebidas_pag)
confirmarbotao(0.32, 0.93, alcoolicas_pag)
confirmarbotao(0.5, 0.93, sobremesas_pag)
confirmarbotao(0.685, 0.93, pratochefe_pag)

janela.mainloop()