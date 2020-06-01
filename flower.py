from PIL import ImageGrab
import pyautogui, sys, time, mouse, keyboard

class Flower:

  window = None

  def __init__(self, window): 
    self.window = window
    keyboard.add_hotkey('num 1', lambda: self.move_flower_to(1))
    keyboard.add_hotkey('num 2', lambda: self.move_flower_to(2))
    keyboard.add_hotkey('num 3', lambda: self.move_flower_to(3))
    keyboard.add_hotkey('num 4', lambda: self.move_flower_to(4))
    keyboard.add_hotkey('num 5', lambda: self.move_flower_to(5)) #dif all
    keyboard.add_hotkey('num 6', lambda: self.move_flower_to(6))
    keyboard.add_hotkey('num 7', lambda: self.move_flower_to(7))
    keyboard.add_hotkey('num 8', lambda: self.move_flower_to(8))
    keyboard.add_hotkey('num 9', lambda: self.move_flower_to(9))


  def move_flower_to(self, pos_drop_flower):
    position_drop_x, position_drop_y = self.get_position_numpad(pos_drop_flower)

    pixel_tibia = 32
    position_flower = self.window.Element('F_txt_pos_bp_first').Get().split(',')
    flower_x = int(position_flower[0])
    flower_y = int(position_flower[1])

    mouse.move(flower_x, flower_y)
    time.sleep(0.03)
    pyautogui.dragTo(position_drop_x, position_drop_y)

  def set_numpad_hotkeys(self):
    print('test')

  def get_position_numpad(self, num):

    if self.window.Element('F_txt_pos_char').Get() == '':
      return

    pixel_tibia = 32

    position_char = self.window.Element('F_txt_pos_char').Get().split(',')
    char_x = int(position_char[0])
    char_y = int(position_char[1])


    if num == 1: #south west
      return char_x - pixel_tibia, char_y + pixel_tibia
    if num == 2: #south
      return char_x, char_y + pixel_tibia
    if num == 3: #south east
      return char_x + pixel_tibia, char_y + pixel_tibia
    if num == 4: #center west
      return char_x - pixel_tibia, char_y
    if num == 5: #center
      return char_x, char_y
    if num == 6: #center east
      return char_x + pixel_tibia, char_y
    if num == 7: #north west
      return char_x - pixel_tibia, char_y - pixel_tibia
    if num == 8: #north
      return char_x, char_y - pixel_tibia
    if num == 9: #north east
      return char_x + pixel_tibia, char_y - pixel_tibia