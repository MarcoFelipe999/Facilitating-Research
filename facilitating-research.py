#Bibliotecas que eu utilizei para rodar esse código
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time
from PySimpleGUI import (
    Window, Button,Text, Image, Input, Column, VSeparator, Push, theme)


theme('LightGrey')

layout_esquerda = [
    [Image(filename='pesquisarapida.png')] #Imagem para a interface
]

#Layout do lado direito da interface
layout_direita = [
    [Text("Google"), Input()],
    [Button('Pesquisar Google'),Push()],
    [Text("Youtube"), Input()],
    [Button('Pesquisar Youtube'),Push()],
    [Text("TikTok"), Input()],
    [Button('Pesquisar Tiktok'),Push()],
    [Text("Unifacol"),],
    [Button('Entrar Unifacol'),Push()],

]
layout = [
    [Column(layout_esquerda),  VSeparator(), Column(layout_direita)]
]
window = Window(
    'Pesquisa rápida', # < esse vai ser o nome que aparece no programa.
    layout= layout,
    element_justification='c'
)








while True:
    event, values = window.read()
    # print(events,values)


#window.FindElement('Prog_bar').UpdateAnimation("gif2.gif", time_between_frames=100)
#if event is None:
#break


    match (event):
        case 'Pesquisar Google':
            navegadorr = webdriver.Chrome(executable_path=r'./chromedriver.exe') #webdriver é necessário para o uso do programa
            link = 'https://www.google.com/?rdk=rk1' # Link de pesquisa
            navegadorr.get(url=link) #
            campo_email = navegadorr.find_element(By.NAME, "q")
            campo_email.send_keys(values[2])
            time.sleep(2)
            pyautogui.press('enter') #Usando a biblioteca pyautogui para apertar a tecla "enter" e realizar a pesquisa
        case 'Pesquisar Youtube':
            navegadorr = webdriver.Chrome(executable_path=r'./chromedriver.exe')
            link = 'https://www.youtube.com/'
            navegadorr.get(url=link)
            campo_email = navegadorr.find_element(By.NAME, "search_query")
            campo_email.send_keys(values[3])
            time.sleep(2)
            pyautogui.press('enter')
        case 'Pesquisar Tiktok':
            navegadorr = webdriver.Chrome(executable_path=r'./chromedriver.exe')
            link = 'https://www.tiktok.com/'
            navegadorr.get(url=link)
            campo_email = navegadorr.find_element(By.NAME, "q")
            campo_email.send_keys(values[4])
            time.sleep(2)
            pyautogui.press('enter')
        case 'Entrar Unifacol':
            navegador = webdriver.Chrome(executable_path=r'./chromedriver.exe')
            link = 'https://sia.unifacol.edu.br/unifacol/' #link do site da universidade
            navegador.get(url=link)
            email = 'digite seu id/e-mail' #aqui eu coloco o id/e-mail da minha conta
            senha = 'digite a sua senha'  #aqui eu coloco a senha da minha conta
            campo_email = navegador.find_element(By.ID, "fLogin")
            sleep(1)
            campo_email.send_keys(email)
            campo_senha = navegador.find_element(By.ID, "fSenha")
            sleep(1)
            campo_senha.send_keys(senha)
            botao_entrar = navegador.find_element(By.CSS_SELECTOR, ".btn")
            sleep(0.5)
            botao_entrar.click()
        case None:
            break
window.close()


