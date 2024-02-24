import pyautogui 
import time

time.sleep(5)
a = """

write what you want to print

"""
def mesaj():
    pyautogui.write(a)
    pyautogui.press('enter')
while True:

 mesaj()
 
 time.sleep(0)


