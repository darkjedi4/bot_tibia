##################################################
## Parte 3: Obtendo a posição do mouse
##################################################
## Na grande maioria das vezes, você irá criar um programa que emula
## você mesmo como se fosse uma macro. Nesse caso, é interessante
## saber onde está o seu mouse em um dado momento.

### Descomente a linha a seguir para ver o funcionamento.
#print(pyautogui.position())












##Biblioteca que faz leitura da tela
from PIL import ImageGrab
##biblioteca de tempo, para delays
import time
##Biblioteca de controle mouse teclado
import pyautogui





##TECLAS F1 a F12

def f1():
    return pyautogui.hotkey("f1")

def f2():
    return pyautogui.hotkey("f2")

def f3():
    return pyautogui.hotkey("f3")

def f4():
    return pyautogui.hotkey("f4")

def f5():
    return pyautogui.hotkey("f5")

def f6():
    return pyautogui.hotkey("f6")

def f7():
    return pyautogui.hotkey("f7")

def f8():
    return pyautogui.hotkey("f8")

def f9():
    return pyautogui.hotkey("f9")

def f10():
    return pyautogui.hotkey("f10")

def f11():
    return pyautogui.hotkey("f11")


def f12():
    return pyautogui.hotkey("f12")


screen = ImageGrab.grab()

barra_vida = (255, 113, 113)

barra_mana = (101,98,240)

pos_barra_sangue_alto = (1850, 149)
hotkey_vida_alta = "F2"

pos_barra_sangue_medio = (1830,149)
hotkey_vida_media = "F1"

pos_barra_sangue_baixo = (1815, 149)
hotkey_vida_baixa = "F10"


pos_barra_mana = (1814, 161)
hotkey_mana = "F5"




def confere_mana():
    ##função de capturar a tela
    screen = ImageGrab.grab()
    mana = screen.getpixel(pos_barra_mana)
    vida1 = screen.getpixel(pos_barra_sangue_alto)
    vida2 = screen.getpixel(pos_barra_sangue_medio)
    vida3 = screen.getpixel(pos_barra_sangue_baixo)


    if vida3 != barra_vida:
        f1()
        time.sleep(0.7)
    elif vida2 != barra_vida:
        f2()
        time.sleep(0.7)
    elif vida1 != barra_vida:
        f9()
        time.sleep(0.7)

    
    if mana != barra_mana:
        f5()

time.sleep(2)
print('Começando em 2 segundos')

while True:
   confere_mana()

