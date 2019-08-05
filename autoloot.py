from pynput import mouse
import pyautogui, sys, time 

def start(x, y):
  ##duration = pyautogui.prompt('Write duration float example: duration and press OK.')
  #duration = float(duration)
  duration = 0.04
  pixel_tibia = 36

  while True:
    pyautogui.dragTo(x, y + pixel_tibia) #south center
    time.sleep(duration)
    pyautogui.dragTo(x - pixel_tibia, y + pixel_tibia) #south west
    time.sleep(duration)
    pyautogui.dragTo(x - pixel_tibia, y) #center west
    time.sleep(duration)
    pyautogui.dragTo(x - pixel_tibia, y - pixel_tibia) #north west
    time.sleep(duration)
    pyautogui.dragTo(x, y - pixel_tibia) #north center
    time.sleep(duration)
    pyautogui.dragTo(x + pixel_tibia, y - pixel_tibia) #north east
    time.sleep(duration)
    pyautogui.dragTo(x + pixel_tibia, y) #center east
    time.sleep(duration)
    pyautogui.dragTo(x + pixel_tibia, y + pixel_tibia) #south east
    time.sleep(duration)

start(595, 295)

