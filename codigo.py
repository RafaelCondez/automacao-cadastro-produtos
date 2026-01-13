import pyautogui
import time

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=668, y=456)
pyautogui.write('treinamento123@hotmail.com')
pyautogui.press('tab')
pyautogui.write('123456789')    
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)

import os
import pandas as pandas

base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, 'produtos.csv')

tabela = pandas.read_csv(csv_path)
print(tabela)

for linha in tabela.index: 
    pyautogui.click(x=671, y=292)
    
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')
    
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')
    
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')
    
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')
    
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')
   
    pyautogui.press('enter')
    pyautogui.scroll(5000)

        