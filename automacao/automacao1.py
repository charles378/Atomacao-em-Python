import pyautogui
from time import sleep


def automacao1():
    pyautogui.PAUSE = 1
    # 1 click no navergador na aria de trabalho cordenada 952,1052
    pyautogui.press('winleft')
    pyautogui.write('microsoft Edge')
    pyautogui.press('enter')
    sleep(2)
    # 2 colar a mensagem jaca no navergado cordenada 738, 259
    pyautogui.write('jaca')
    pyautogui.press('enter')
    # 4 fazer um lop para fica navegando
    with open('valores.txt', 'r') as arquivo:
        for linha in arquivo:
            valor = linha
            # 1 clicar no x
            pyautogui.click(714, 110, duration=2)
            # 2 cola o valor na barra de pesguisa
            pyautogui.click(443, 116, duration=2)
            pyautogui.write(valor)