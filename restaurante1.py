import customtkinter as ctk
from PIL import Image, ImageTk

#Configuração Janela principal -------------------------------------------------------------------------------------
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

#função quadrados -------------------------------------------------------------------------------------
def quadrados(cor, width, height,posicaox, posicaoy):
    ctk.CTkFrame(
    master = janela1, 
    width= width, 
    height= height,
    fg_color = cor

    ).place(relx=posicaox, rely=posicaoy, anchor="center")
quadrados("white", 900, 700, 0.5, 0.5)
quadrados("#c4273a", 300, 50, 0.785, 0.17)

#imagem/função -------------------------------------------------------------------------------------
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

#caixas -------------------------------------------------------------------------------------
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

comidas = {
    'Pasteis assados': 8.50,
    'Tabua de frios': 25.00,
    'Bolinhos de peixe': 12.00,
    'Mini hamburgueres': 15.00,
    'Salada pequena': 9.00,
    'Porção de quibe': 10.00,
    'Feijoada': 35.00,
    'Lasanha': 22.00,
    'Bife a parmegiana': 28.00,
    'Espaguete ao molho': 18.00,
    'Bobo de camarão': 30.00,
    'Bife a cavalo': 24.00,
    'Água': 4.00,
    'Suco de acerola': 6.50,
    'Fanta uva': 5.00,
    'Suco de abacaxi com hortelã': 7.00,
    'Água saborizada': 5.50,
    'Suco de morango com leite': 7.50,
    'Heineken': 10.00,
    'Vinho': 45.00,
    'Skol': 6.00,
    'Vodka': 50.00,
    'Cachaça': 35.00,
    'Pinga': 32.00,
    'Brownie': 9.00,
    'Sorvete': 8.00,
    'Torta de limão': 12.00,
    'Gelatina': 4.00,
    'Bala baiana': 2.00,
    'Bolo de cenoura': 10.00,
    'Trakinas': 5.50,
    '7 Belo': 3.00,
    'Pé de moleque': 6.00,
    'Suspiro': 5.00,
    'Maria mole': 4.50,
    'Bolo gelado': 11.00
}

pedido = {}
total = 0

#Botões de adicionar e remover :D
def atualizar_total():
    global total
    total_label.configure(text=f"Total: R${total:.2f}")

def alterar_produto(produto, acao):
    global total
    if acao == "adicionar":
        if produto in pedido:
            pedido[produto] += 1
        else:
            pedido[produto] = 1
        total += comidas[produto]
    elif acao == "remover":
        if produto in pedido and pedido[produto] > 0:
            pedido[produto] -= 1
            total -= comidas[produto]
            if pedido[produto] == 0:
                del pedido[produto]
    atualizar_total()

def criar_interface(eixox1, eixoy1, eixox2, eixoy2, intervalo_inicio, intervalo_fim):

    global total_label
    total_label = ctk.CTkLabel(
        janela, text="Total: R$0.00",
        font=("courier new", 20, "bold"),
        width=60,
        height=30,
        text_color="Black",
        fg_color="white",                               
        )
    total_label.place(relx=0.75, rely=0.11, anchor="center")
    
    produtos_intervalo = list(comidas.keys())[intervalo_inicio:intervalo_fim]

    for produto in produtos_intervalo:
        ctk.CTkButton(janela2, text="+1", 
                        font=("courier new", 15),
                        width=60, 
                        height=30,
                        text_color="white",
                        fg_color="#c4273a",
                        hover_color="#e34d5f",
                        command=lambda p=produto: alterar_produto(p, "adicionar")).place(relx=eixox1, rely=eixoy1, anchor="center")
        
        ctk.CTkButton(janela2, text="-1", 
                        font=("courier new", 15),
                        width=60, 
                        height=30,
                        text_color="white",
                        fg_color="#c4273a",
                        hover_color="#e34d5f",
                        command=lambda p=produto: alterar_produto(p, "remover")).place(relx=eixox2, rely=eixoy2, anchor="center")


def criar_pag_frame(imagem_nome, voltar_comando=None):
    frame = ctk.CTkFrame(janela2)

    foto = ctk.CTkImage(
        light_image=Image.open(imagem_nome),
        dark_image=Image.open(imagem_nome),
        size=(800, 600)
    )
    image_label = ctk.CTkLabel(frame, image=foto, text="")
    image_label.place(relx=0.5, rely=0.5, anchor="center")

    if voltar_comando:
        botao_voltar = ctk.CTkButton(
            frame,
            text="←",
            font=("courier new", 15),
            width=60,
            height=30,
            text_color="white",
            fg_color="#c4273a",
            hover_color="#e34d5f",
            command=voltar_comando
        )
        botao_voltar.place(relx=0.07, rely=0.12, anchor="center")

    return frame

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

#era pra chamar a tela principal -------------------------------------------------------------------------------------
def telaprincipalcardapio():
    for widget in janela2.winfo_children():
        widget.destroy()

    imagem = ctk.CTkImage(
    light_image=Image.open("Cardápio.png"),
    dark_image=Image.open("Cardápio.png"),
    size=(800, 600)
    )

    def imagem_tela (janela, imagem, posicaox, posicaoy):

        image_label = ctk.CTkLabel(janela, image=imagem, text="")
        image_label.place(relx=posicaox, rely=posicaoy, anchor="center")

    imagem_tela(janela2, imagem, 0.5, 0.5)

    confirmarbotao(0.32, 0.52, entradas_pag)
    confirmarbotao(0.5, 0.52, principais_pag)
    confirmarbotao(0.685, 0.52, bebidas_pag)
    confirmarbotao(0.32, 0.93, alcoolicas_pag)
    confirmarbotao(0.5, 0.93, sobremesas_pag)
    confirmarbotao(0.685, 0.93, pratochefe_pag)

#opções -------------------------------------------------------------------------------------

def entradas_pag():
    for widget in janela2.winfo_children():
        widget.destroy()
    frame = criar_pag_frame("Entradas.png", voltar_comando=telaprincipalcardapio)
    frame.pack(fill="both", expand=True)

    criar_interface(0.19, 0.46, 0.31, 0.46, 0, 1)
    criar_interface(0.44, 0.46, 0.56, 0.46, 1, 2)
    criar_interface(0.69, 0.46, 0.81, 0.46, 2, 3)
    criar_interface(0.19, 0.81, 0.31, 0.81, 3, 4)
    criar_interface(0.44, 0.81, 0.56, 0.81, 4, 5)
    criar_interface(0.69, 0.81, 0.81, 0.81, 5, 6) 

def principais_pag():
    for widget in janela2.winfo_children():
        widget.destroy()
    frame = criar_pag_frame("Principais.png", voltar_comando=telaprincipalcardapio)
    frame.pack(fill="both", expand=True)

    criar_interface(0.19, 0.46, 0.31, 0.46, 6, 7)
    criar_interface(0.44, 0.46, 0.56, 0.46, 7, 8)
    criar_interface(0.69, 0.46, 0.81, 0.46, 8, 9)
    criar_interface(0.19, 0.81, 0.31, 0.81, 9, 10)
    criar_interface(0.44, 0.81, 0.56, 0.81, 10, 11)
    criar_interface(0.69, 0.81, 0.81, 0.81, 11, 12) 

def bebidas_pag():
    for widget in janela2.winfo_children():
        widget.destroy()
    frame = criar_pag_frame("Bebidas.png", voltar_comando=telaprincipalcardapio)
    frame.pack(fill="both", expand=True)

    criar_interface(0.19, 0.46, 0.31, 0.46, 12, 13)
    criar_interface(0.44, 0.46, 0.56, 0.46, 13, 14)
    criar_interface(0.69, 0.46, 0.81, 0.46, 14, 15)
    criar_interface(0.19, 0.81, 0.31, 0.81, 15, 16)
    criar_interface(0.44, 0.81, 0.56, 0.81, 16, 17)
    criar_interface(0.69, 0.81, 0.81, 0.81, 17, 18) 

def alcoolicas_pag():
    for widget in janela2.winfo_children():
        widget.destroy()
    frame = criar_pag_frame("Alcolicas.png", voltar_comando=telaprincipalcardapio)
    frame.pack(fill="both", expand=True)

    criar_interface(0.19, 0.46, 0.31, 0.46, 18, 19)
    criar_interface(0.44, 0.46, 0.56, 0.46, 19, 20)
    criar_interface(0.69, 0.46, 0.81, 0.46, 20, 21)
    criar_interface(0.19, 0.81, 0.31, 0.81, 21, 22)
    criar_interface(0.44, 0.81, 0.56, 0.81, 22, 23)
    criar_interface(0.69, 0.81, 0.81, 0.81, 23, 24)

def sobremesas_pag():
    for widget in janela2.winfo_children():
        widget.destroy()
    frame = criar_pag_frame("Sobremesas.png", voltar_comando=telaprincipalcardapio)
    frame.pack(fill="both", expand=True)

    criar_interface(0.19, 0.46, 0.31, 0.46, 24, 25)
    criar_interface(0.44, 0.46, 0.56, 0.46, 25, 26)
    criar_interface(0.69, 0.46, 0.81, 0.46, 26, 27)
    criar_interface(0.19, 0.81, 0.31, 0.81, 27, 28)
    criar_interface(0.44, 0.81, 0.56, 0.81, 28, 29)
    criar_interface(0.69, 0.81, 0.81, 0.81, 29, 30)

def pratochefe_pag():
    for widget in janela2.winfo_children():
        widget.destroy()
    frame = criar_pag_frame("Chefe.png", voltar_comando=telaprincipalcardapio)
    frame.pack(fill="both", expand=True)

    criar_interface(0.19, 0.46, 0.31, 0.46, 30, 31)
    criar_interface(0.44, 0.46, 0.56, 0.46, 31, 32)
    criar_interface(0.69, 0.46, 0.81, 0.46, 32, 33)
    criar_interface(0.19, 0.81, 0.31, 0.81, 33, 34)
    criar_interface(0.44, 0.81, 0.56, 0.81, 34, 35)
    criar_interface(0.69, 0.81, 0.81, 0.81, 35, 36)

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