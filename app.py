import pyautogui
from time import sleep

#1 clicar no na vegador 906,1053
pyautogui.click(952,1052,duration=2)
#2 colar algo na barra de pesgisa 738,259
pyautogui.click(738,259)
pyautogui.write('jaca')
#3 quica para pesquisa 582,253
pyautogui.click(582,253, duration=2)
#4 fazer um lupe
with open('valores.txt', 'r') as arquivo:
    for linha in arquivo:
        valor = linha
	#1 quicar no x 714,110
        pyautogui.click(714,110, duration=2)
	#2 colar a streg 443,116
        pyautogui.click(443,116, duration=2)
        pyautogui.write(valor)
	#3 pesquisar 189,106
        #pyautogui.click(189,106, duration=2)
