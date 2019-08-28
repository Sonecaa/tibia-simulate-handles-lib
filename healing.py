from PIL import ImageGrab
import pyautogui, sys, time, mouse, keyboard

class Healing:

  window = None

  def __init__(self, window): 
    self.window = window

  def screenshot_life(self):
    image = ImageGrab.grab(bbox=(300,100,500,500))
    image.save("life.jpg", "JPEG")
    #image.show()

  def get_monster_position(self, name):
    return pyautogui.locateOnScreen(name+".png", confidence=.9)

  def get_is_attacking(self):
    return pyautogui.locateOnScreen("images/attacking.png", confidence=.5)

  def get_is_follow(self):
    return pyautogui.locateOnScreen("images/follow.png")

  def get_mana(self):
    return pyautogui.locateOnScreen("images/mana.png")

  def get_health(self):
    return pyautogui.locateOnScreen("images/health.png")

  def getLife(self):
  health = pyautogui.locateOnScreen("images/health.png")
  if (pyautogui.pixelMatchesColor((health.left + 105), (health.top + 7), (219, 79, 79))):
      return 100
  elif (pyautogui.pixelMatchesColor((health.left + 94), (health.top + 7), (219, 79, 79))):
      return 90
  elif (pyautogui.pixelMatchesColor((health.left + 74), (health.top + 7), (219, 79, 79))):
      return 70
  elif (pyautogui.pixelMatchesColor((health.left + 54), (health.top + 7), (219, 79, 79))):
      return 50
  elif (pyautogui.pixelMatchesColor((health.left + 34), (health.top + 7), (219, 79, 79))):
      return 30
  elif (pyautogui.pixelMatchesColor((health.left + 24), (health.top + 7), (219, 79, 79))):
      return 20
  elif (pyautogui.pixelMatchesColor((health.left + 14), (health.top + 7), (219, 79, 79))):
      return 15
  elif (pyautogui.pixelMatchesColor((health.left + 5), (health.top + 7), (219, 79, 79))):
      return 10
  return 0

  def getMana(self):
      health = pyautogui.locateOnScreen("images/mana.png")
      if (pyautogui.pixelMatchesColor((health.left + 105), (health.top + 5), (67, 64, 192))):
          return 100
      elif (pyautogui.pixelMatchesColor((health.left + 94), (health.top + 5), (67, 64, 192))):
          return 90
      elif (pyautogui.pixelMatchesColor((health.left + 74), (health.top + 5), (67, 64, 192))):
          return 70
      elif (pyautogui.pixelMatchesColor((health.left + 54), (health.top + 5), (67, 64, 192))):
          return 50
      elif (pyautogui.pixelMatchesColor((health.left + 34), (health.top + 7), (219, 79, 79))):
          return 30
      elif (pyautogui.pixelMatchesColor((health.left + 24), (health.top + 7), (219, 79, 79))):
          return 20
      elif (pyautogui.pixelMatchesColor((health.left + 14), (health.top + 7), (219, 79, 79))):
          return 15
      elif (pyautogui.pixelMatchesColor((health.left + 5), (health.top + 28), (219, 79, 79))):
          return 10
      return 0

  def heal(self,percent, spell,time):
      life = self.getLife(self)
      while life < percent:
          #w.Write(spell) ***
          sleep(time)
          life = self.getLife(self)

  def mp(self,percent, spell,time):
      mana = self.getMana(self)
      while mana > percent:
          #w.Write(spell) ***
          sleep(time)
          mana = self.getMana(self)