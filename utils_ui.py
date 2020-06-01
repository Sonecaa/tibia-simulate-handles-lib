from PIL import ImageGrab
import pyautogui, sys, time, mouse, keyboard

class Utils_Ui:

  window = None

  def __init__(self, window): 
    self.window = window

  def _get_mouse_position_on_click(self, ui_field):
    position_x, position_y = mouse.get_position()
    self.window.Element(ui_field).Update(str(position_x) + ',' + str(position_y))

    mouse.unhook_all()

  def get_mouse_position_on_click(self, ui_field):
     mouse.on_button(self._get_mouse_position_on_click, [ui_field], [mouse.LEFT], [mouse.UP])
