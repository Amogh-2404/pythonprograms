import pyautogui
import time
time.sleep(5)

count=0

while count<=200:
  pyautogui.typewrite("")
  pyautogui.press("enter")
  count=count+1