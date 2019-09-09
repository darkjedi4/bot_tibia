from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyautogui
from PIL import ImageGrab
from tkinter.ttk import *
import time
from hotkeys import *


screen = ImageGrab.grab()

fonte = "Century Gothic"
tamanho = 10


jan = Tk()

jan.geometry('555x300')
jan.title("Rat's Bot")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)

Frame_janela = Frame(jan, width=600, height=300, relief='raise')
Frame_janela.pack(side=RIGHT)

label_titulo = ttk.Label(jan, text="SELECIONE A POSIÇÂO PRA HEALAR", font=("Arial", 20))
label_titulo.place(x=25, y=10)

def vida1():
    messagebox.showinfo("Vida -1", "Clique na barra de vida na POSIÇÂO da primeira Cura")
    x_vida1 = pyautogui.position().x
    y_vida1 = pyautogui.position().y
    cor_vida = screen.getpixel((x_vida1,y_vida1))
    cor_vida1_x["text"] = cor_vida[0]
    cor_vida1_y["text"] = cor_vida[1]
    cor_vida1_z["text"] = cor_vida[2]
    vida1_x["text"] = x_vida1
    vida1_y["text"] = y_vida1
    lb_vida1["text"] = "X= {}  -  Y= {}".format(x_vida1,y_vida1)


def vida2():
    messagebox.showinfo("Vida -2", "Clique na barra de vida na POSIÇÂO da segunda Cura")
    x_vida2 = pyautogui.position().x
    y_vida2 = pyautogui.position().y
    cor_vida = screen.getpixel((x_vida2, y_vida2))
    cor_vida2_x["text"] = cor_vida[0]
    cor_vida2_y["text"] = cor_vida[1]
    cor_vida2_z["text"] = cor_vida[2]
    vida2_x["text"] = x_vida2
    vida2_y["text"] = y_vida2
    lb_vida2["text"] = "X= {}  -  Y= {}".format(x_vida2, y_vida2)

def vida3():
    messagebox.showinfo("Vida -3", "Clique na barra de vida na POSIÇÂO da terceira Cura")
    x_vida3 = pyautogui.position().x
    y_vida3 = pyautogui.position().y
    cor_vida = screen.getpixel((x_vida3, y_vida3))
    cor_vida3_x["text"] = cor_vida[0]
    cor_vida3_y["text"] = cor_vida[1]
    cor_vida3_z["text"] = cor_vida[2]
    vida3_x["text"] = x_vida3
    vida3_y["text"] = y_vida3
    lb_vida3["text"] = "X= {}  -  Y= {}".format(x_vida3, y_vida3)

def mana1():
    messagebox.showinfo("Mana 1", "Clique na barra de mana na POSIÇÂO da cura de mana")
    x_mana1 = pyautogui.position().x
    y_mana1 = pyautogui.position().y
    cor_mana = screen.getpixel((x_mana1, y_mana1))
    cor_mana1_x["text"] = cor_mana[0]
    cor_mana1_y["text"] = cor_mana[1]
    cor_mana1_z["text"] = cor_mana[2]
    mana1_x["text"] = x_mana1
    mana1_y["text"] = y_mana1
    lb_mana1["text"] = "X= {}  -  Y= {}".format(x_mana1, y_mana1)

def mana2():
    messagebox.showinfo("Mana Opcional", "Clique na barra de mana na POSIÇÂO da cura de mana")
    x_mana2 = pyautogui.position().x
    y_mana2 = pyautogui.position().y
    cor_mana = screen.getpixel((x_mana2, y_mana2))
    cor_mana2_x["text"] = cor_mana[0]
    cor_mana2_y["text"] = cor_mana[1]
    cor_mana2_z["text"] = cor_mana[2]
    mana2_x["text"] = x_mana2
    mana2_y["text"] = y_mana2
    lb_mana2["text"] = "X= {}  -  Y= {}".format(x_mana2, y_mana2)









##Cura alta = EXURA, etc

UserLabel= Label(Frame_janela, text="Cura n1:", font=(fonte,tamanho))
UserLabel.place(x=10, y=55)


Botao_vida_1 = ttk.Button(Frame_janela, text="Selecione a POS", width=30, command=vida1)
Botao_vida_1.place(x=120, y=55)

lb_vida1 = ttk.Label(jan, text="", font=("Century Gothic", 10))
lb_vida1.place(x=350, y=55)



vida1_x = ttk.Label(jan, text="")
vida1_y = ttk.Label(jan, text="")
cor_vida1_x= Label(jan, text="")
cor_vida1_y= Label(jan, text="")
cor_vida1_z= Label(jan, text="")

combo_vida1 = ttk.Combobox(jan, width=5)
combo_vida1.place(x=490, y = 55)
combo_vida1['values'] = ("f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12")
combo_vida1.current(0)

##Cura Media = Exura Gran etc
UserLabel2= Label(Frame_janela, text="Cura n2:", font=(fonte,tamanho))
UserLabel2.place(x=10, y=85)

Botao_vida_2 = ttk.Button(Frame_janela, text="Selecione a POS", width=30, command=vida2)
Botao_vida_2.place(x=120, y=85)

lb_vida2 = ttk.Label(jan, text="", font=(fonte, tamanho))
lb_vida2.place(x=350, y=85)

vida2_x = ttk.Label(jan, text="")
vida2_y = ttk.Label(jan, text="")
cor_vida2_x= Label(jan, text="")
cor_vida2_y= Label(jan, text="")
cor_vida2_z= Label(jan, text="")

combo_vida2 = ttk.Combobox(jan, width=5)
combo_vida2.place(x=490, y = 85)
combo_vida2['values'] = ("f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12")
combo_vida2.current(0)


##Cura Baixa = Exura Vita, UH, etc

UserLabel3= Label(Frame_janela, text="Cura n3:", font=(fonte,tamanho))
UserLabel3.place(x=10, y=115)

Botao_vida_3 = ttk.Button(Frame_janela, text="Selecione a POS", width=30, command=vida3)
Botao_vida_3.place(x=120, y=115)

lb_vida3 = ttk.Label(jan, text="", font=(fonte, tamanho))
lb_vida3.place(x=350, y=115)

vida3_x = ttk.Label(jan, text="")
vida3_y = ttk.Label(jan, text="")
cor_vida3_x= Label(jan, text="")
cor_vida3_y= Label(jan, text="")
cor_vida3_z= Label(jan, text="")

combo_vida3 = ttk.Combobox(jan, width=5)
combo_vida3.place(x=490, y = 115)
combo_vida3['values'] = ("f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12")
combo_vida3.current(0)

##Cura de Mana 1 = GMP, MP, Etc

UserLabel4= Label(Frame_janela, text="Mana MP 1:", font=(fonte,tamanho))
UserLabel4.place(x=10, y=145)

Botao_mana_1 = ttk.Button(Frame_janela, text="Selecione a POS", width=30, command=mana1)
Botao_mana_1.place(x=120, y=145)

lb_mana1 = ttk.Label(jan, text="", font=(fonte, tamanho))
lb_mana1.place(x=350, y=145)

mana1_x = ttk.Label(jan, text="")
mana1_y = ttk.Label(jan, text="")
cor_mana1_x= Label(jan, text="")
cor_mana1_y= Label(jan, text="")
cor_mana1_z= Label(jan, text="")

combo_mana1 = ttk.Combobox(jan, width=5)
combo_mana1.place(x=490, y = 145)
combo_mana1['values'] = ("f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12")
combo_mana1.current(0)

##Combo Mana 2 = UMP etc

UserLabel5= Label(Frame_janela, text="Mana MP 2:", font=(fonte,tamanho))
UserLabel5.place(x=10, y=175)

Botao_mana_2 = ttk.Button(Frame_janela, text="Selecione a POS", width=30, command=mana2)
Botao_mana_2.place(x=120, y=175)

lb_mana2 = ttk.Label(jan, text="", font=(fonte, tamanho))
lb_mana2.place(x=350, y=175)

mana2_x = ttk.Label(jan, text="")
mana2_y = ttk.Label(jan, text="")
cor_mana2_x= Label(jan, text="")
cor_mana2_y= Label(jan, text="")
cor_mana2_z= Label(jan, text="")

combo_mana2 = ttk.Combobox(jan, width=5)
combo_mana2.place(x=490, y = 175)
combo_mana2['values'] = ("f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12")
combo_mana2.current(0)


lb_info_time = ttk.Label(jan, text="Delay [Entre 0 e 1, separando por . ex: 0.5]:", font=(fonte, 8))
lb_info_time.place(x=315, y=245)

combo = ttk.Combobox(jan, width=5)
combo.place(x=410, y=272)
combo['values']=(1.0,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0.0)
combo.current(0)

lbl_info_delay = ttk.Label(jan, text="s", font=(fonte, tamanho))
lbl_info_delay.place(x=465, y=272)





##Função hotkey

def f1(hk):
    return pyautogui.hotkey(hk)



##Botão START##



def parar():
    iniciar = False
    print(iniciar)



class Start():
    def __init__(self):
        screen = ImageGrab.grab()
        delay = float(combo.get())

        print(delay)

        cor_vida1 = (cor_vida1_x["text"], cor_vida1_y["text"], cor_vida1_z["text"])
        cor_vida2 = (cor_vida2_x["text"], cor_vida2_y["text"], cor_vida2_z["text"])
        cor_vida3 = (cor_vida3_x["text"], cor_vida3_y["text"], cor_vida3_z["text"])
        cor_mana1 = (cor_mana1_x["text"], cor_mana1_y["text"], cor_mana1_z["text"])
        cor_mana2 = (cor_mana2_x["text"], cor_mana2_y["text"], cor_mana2_z["text"])

        pos_barra_sangue_alto = int(vida1_x["text"]), int(vida1_y["text"])

        pos_barra_sangue_medio = int(vida2_x["text"]),int(vida2_y["text"])


        pos_barra_sangue_baixo = int(vida3_x["text"]),int(vida3_y["text"])


        pos_barra_mana1 = int(mana1_x["text"]),int(mana1_y["text"])


        pos_barra_mana2 = int(mana2_x["text"]), int(mana2_y["text"])





        while (True):
            vida1 = screen.getpixel((pos_barra_sangue_alto))
            vida2 = screen.getpixel((pos_barra_sangue_medio))
            vida3 = screen.getpixel((pos_barra_sangue_baixo))
            mana1 = screen.getpixel((pos_barra_mana1))
            mana2 = screen.getpixel((pos_barra_mana2))

            if vida3 != cor_vida3:
                hk3 = combo_vida3.get()
                f1(hk3)


            elif vida2 != cor_vida2:
                hk2 = combo_mana2.get()
                f1(hk2)

            elif vida1 != cor_vida1:
                hk1 = combo_vida1.get()
                f1(hk1)

            if mana1 != cor_mana1:
                hk_m = combo_mana1.get()
                f1(hk_m)

            elif mana2 != cor_mana2:
                hk_m2 = combo_mana2.get()
                f1(hk_m2)












botaoStart = ttk.Button(jan, text="INICIAR", width=49, command=Start)
botaoStart.place(x=10, y=230)

botaoPause = ttk.Button(jan, text="PARAR", width=39, command=parar)
botaoPause.place(x=45, y=260)






jan.mainloop()