from PIL import ImageGrab
import pyautogui, sys, time, mouse, keyboard

class Healing:

  window = None

  def __init__(self, window): 
    self.window = window

  def get_monster_position(self, name):
    return pyautogui.locateOnScreen(name+".png", confidence=.9)

  def get_is_attacking(self):
    return pyautogui.locateOnScreen("images/attacking.png", confidence=.5)

  def get_is_follow(self):
    return pyautogui.locateOnScreen("images/follow.png")

  def get_health(self):
    #half = pyautogui.locateOnScreen("images_health/half.png")
    full = pyautogui.locateOnScreen("images_health/full.png")

    if(full):
        #return 50
        print('lol')
    else:
        keyboard.write('exura gran')
        keyboard.press('enter')

    #if(health):

        #if (pyautogui.pixelMatchesColor((health.left + 105), (health.top + 8), (164, 126, 126) )):
        #    return 100
        #elif (pyautogui.pixelMatchesColor((health.left + 94), (health.top + 8), (164, 126, 126) )):
        #    return 90
        #elif (pyautogui.pixelMatchesColor((health.left + 74), (health.top + 8), (164, 126, 126) )):
        #    return 70
        #elif (pyautogui.pixelMatchesColor((health.left + 54), (health.top + 8), (164, 126, 126) )):
        #    return 58
        #elif (pyautogui.pixelMatchesColor((health.left + 34), (health.top + 8), (164, 126, 126) )):
        #    return 30
        #elif (pyautogui.pixelMatchesColor((health.left + 24), (health.top + 8), (164, 126, 126) )):
        #    return 20
        #elif (pyautogui.pixelMatchesColor((health.left + 14), (health.top + 8), (164, 126, 126) )):
        #    return 15
        #elif (pyautogui.pixelMatchesColor((health.left + 5), (health.top + 8), (164, 126, 126) )):
        #    return 10
        #else:
        #    return 0

  def get_mana(self):
    mana = pyautogui.locateOnScreen("images/mana.png")
    if(mana):
        if (pyautogui.pixelMatchesColor((mana.left + 105), (mana.top + 5), (67, 64, 192))):
            return 100
        elif (pyautogui.pixelMatchesColor((mana.left + 94), (health.top + 5), (67, 64, 192))):
            return 90
        elif (pyautogui.pixelMatchesColor((mana.left + 74), (mana.top + 5), (67, 64, 192))):
            return 70
        elif (pyautogui.pixelMatchesColor((mana.left + 54), (mana.top + 5), (67, 64, 192))):
            return 50
        elif (pyautogui.pixelMatchesColor((mana.left + 34), (mana.top + 7), (219, 79, 79))):
            return 30
        elif (pyautogui.pixelMatchesColor((mana.left + 24), (mana.top + 7), (219, 79, 79))):
            return 20
        elif (pyautogui.pixelMatchesColor((mana.left + 14), (mana.top + 7), (219, 79, 79))):
            return 15
        elif (pyautogui.pixelMatchesColor((mana.left + 5), (mana.top + 28), (219, 79, 79))):
            return 10
        else:
            return 0

  def heal_health(self, percent, spell, time):
      print('heal')
      life = self.get_health()

      if(life):
        while life < percent:
            keyboard.write(spell)
            #time.sleep(time)
            keyboard.press('enter')
            #time.sleep(time)
            life = self.get_health()

  def heal_mana(self, percent, spell, time):
      mana = self.get_mana()

      if(mana):
        while mana > percent:
            keyboard.write(spell)
            keyboard.press('enter')
            time.sleep(time)
            mana = self.get_mana()