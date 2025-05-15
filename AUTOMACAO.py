#ir na documentação > cheat sheets
import pyautogui
import time

pyautogui.PAUSE=0.3 #depois de um comando vai esperar o tempo p clicar no prox passo

#pegar posições do mouse e da tela
print(pyautogui.position())
print(pyautogui.size())

#pegar funções do mouse
time.sleep(5)# vai aguardar pelo tempo informado e depois clicar
#pyautogui.click(x=860, y=141)#clicar na posição informada. pode passar o parametro de qual botal usar qtos clicks ,clicks=2, button='righ"

pyautogui.moveTo(x=624, y=143) # vai mover o mouse ate a posição informada
pyautogui.click(x=718, y=278)
pyautogui.scroll(-200) # num negativo = scroll para baixo

#pegar funções do teclado
pyautogui.write()
pyautogui.hotkey()
pyautogui.press()


