from PIL import ImageGrab
import pyautogui, sys, time, mouse, keyboard

class RuneMaker:

  window = None

  def __init__(self, window): 
    self.window = window

  def making_runes(self):

    rune_spell = self.window.Element('RM_txt_spell').Get()
    rune_time  = self.window.Element('RM_txt_speed').Get()

    while rune_spell != "":
      # *** check mana 
      self.eat_food()
      keyboard.write(rune_spell)
      keyboard.send('enter')
      time.sleep(float(rune_time))
 
      print("Making runes: " + rune_spell)
      time.sleep(float(rune_time))

  def eat_food(self):
    pos = pyautogui.locateOnScreen('images/brownmushroom.png')
    if pos == 'None':
      print('No food.')
    pyautogui.rightClick(pos)

