import pyautogui, sys, time, mouse, keyboard
from constants import *
from functions import *


def start_array_positions(array, duration):

  for position_string in array:
    x, y = array_string_to_position_obj(str(position_string))
    time.sleep(duration)
    try:
      pyautogui.dragTo(x, y)
    except KeyboardInterrupt:
      print('END PROGRAM')

def start(x, y):
  ##duration = pyautogui.prompt('Write duration float example: duration and press OK.')
  #duration = float(duration)
  duration = 0.03
  pixel_tibia = 36

  while True:
    try:
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

      if keyboard.is_pressed == True:
        print('END PROGRAM')
        break
    except KeyboardInterrupt:
      print('END PROGRAM')
