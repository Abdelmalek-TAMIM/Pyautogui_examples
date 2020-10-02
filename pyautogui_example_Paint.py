import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
#OUVERTURE DE PAINT
pyautogui.moveTo(300, 300, duration=0.3)
pyautogui.hotkey('win')
pyautogui.write('paint', interval=0.25)
pyautogui.press('enter')
#DESSIN SUR PAINT
pyautogui.moveTo(300, 300, duration=1)
pyautogui.dragRel(100, 100, duration=1)
pyautogui.dragRel(-100, 100, duration=1)
pyautogui.dragRel(-100, -100, duration=1)
pyautogui.dragRel(100, -100, duration=1)
pyautogui.click(370,66)
pyautogui.click(233,397)
pyautogui.write('Python is really funny !!', interval=0.25)