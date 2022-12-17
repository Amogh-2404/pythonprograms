import pyautogui
import time
time.sleep(4)

count=0

while count<=50:
  pyautogui.typewrite("Breakfast time!!")
  pyautogui.press("enter")
  count=count+1