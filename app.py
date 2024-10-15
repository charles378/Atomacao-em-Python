# import pyautogui
# from time import sleep

# pyautogui.alert('Vai comesar a automatisaçao, não mecha no conputado, mas se vocé quere para e so arasta o mause ' 
#                     'para o topo da tela esquerdo')
# #1 clicar no na vegador 906,1053
# pyautogui.click(952,1052,duration=2)
# #2 colar algo na barra de pesgisa 738,259
# pyautogui.click(738,259)
# pyautogui.write('jaca')
# #3 quica para pesquisa 582,253
# pyautogui.click(582,253, duration=2)
# #4 fazer um lupe
# with open('valores.txt', 'r') as arquivo:
#     for linha in arquivo:
#         valor = linha
# 	#1 quicar no x 714,110
#         pyautogui.click(714,110, duration=2)
# 	#2 colar a streg 443,116
#         pyautogui.click(443,116, duration=2)
#         pyautogui.write(valor)
# 	#3 pesquisar 189,106
#         #pyautogui.click(189,106, duration=2)

        
from time import sleep
import pyautogui
# para abrir a ferramenta de localisação do mause
# 1 abra o terminal e digite python e perte entre
# 2 digite fom mouseinfo import mouseInfo a perte entre
# 3 digite mouseInfo() a perta entre e a ferramenta sera abrerta
# F6 para salvar a cordenada do curso

pyautogui.PAUSE = 1
# 1 click no navergador na aria de trabalho cordenada 952,1052
sleep(1)
pyautogui.press('winleft')
pyautogui.write('microsoft Edge')
pyautogui.press('enter')
# 2 colar a mensagem jaca no navergado cordenada 738, 259
pyautogui.write('jaca')

pyautogui.press('enter')
# 4 fazer um lop para fica navegando
with open('valores.txt', 'r') as arquivo:
    for linha in arquivo:
        valor = linha
        pyautogui.write(valor)
        # 1 clicar no x 724,125, 750,111
        pyautogui.click(724,125, duration=2)
        # 2 cola o valor na barra de pesguisa
        pyautogui.click(443, 116, duration=2)

