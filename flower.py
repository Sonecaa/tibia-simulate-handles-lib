from PIL import ImageGrab
import pyautogui, sys, time, mouse, keyboard

class Flower:

  window = None

  def __init__(self, window): 
    self.window = window
    keyboard.add_hotkey('num 1', self.move_flower_to(1))
    keyboard.add_hotkey('num 2', self.move_flower_to(2))
    keyboard.add_hotkey('num 3', self.move_flower_to(3))
    keyboard.add_hotkey('num 4', self.move_flower_to(4))
    keyboard.add_hotkey('num 5', self.move_flower_to(5)) #dif all
    keyboard.add_hotkey('num 6', self.move_flower_to(6))
    keyboard.add_hotkey('num 7', self.move_flower_to(7))
    keyboard.add_hotkey('num 8', self.move_flower_to(8))
    keyboard.add_hotkey('num 9', self.move_flower_to(9))

  def move_flower_to(self, pos_drop_flower):
    print('nada ainda')

  def test(self):
    print('ts')

  def get_mouse_position_on_click(self):
    position_x, position_y = mouse.get_position()
    self.window.Element('F_txt_pos_char').Update(str(position_x) + ',' + str(position_y))

    mouse.unhook_all()