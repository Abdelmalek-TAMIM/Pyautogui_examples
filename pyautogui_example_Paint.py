import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
#OUVERTURE DE PAINT
pyautogui.moveTo(300, 300, duration=0.3)
pyautogui.hotkey('win')
pyautogui.write('paint', interval=0.25)
pyautogui.press('enter')
#DESSIN SUR PAINT
dis=200
pyautogui.moveTo(300, 300, duration=1)
while dis>5:
    pyautogui.dragRel(0, dis, duration=0.2)
    pyautogui.dragRel(-dis,0, duration=0.2)
    dis=dis-10
    pyautogui.dragRel(0, -dis, duration=0.2)
    pyautogui.dragRel(dis,0, duration=0.2)
    dis=dis-10
