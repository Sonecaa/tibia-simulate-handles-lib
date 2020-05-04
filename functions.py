from PIL import ImageGrab
import pyautogui, sys, time, mouse, keyboard

def position_to_array_string(x,y):
  return [str(x) + ',' + str(y)]

def array_string_to_position_obj(array_str):
  array_str = array_str.replace("['", "") # remove brackets
  array_str = array_str.replace("']", "") # remove brackets
  array = array_str.split(',') # explode
  x = array[0]
  y = array[1]
  return (int(x), int(y))