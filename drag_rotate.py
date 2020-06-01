import pyautogui, sys, time, mouse, keyboard
from constants import *
from functions import *
from random import randrange


class DragRotate:

  window = None

  def __init__(self, window): 
    self.window = window

  def get_records(self):
    return self.window.Element('Records').GetListValues()

  def get_repeats(self):
    return int(self.window.Element('Loop').Get())

  def get_speed(self):
    return float(self.window.Element('Speed').Get()) 

  def clear_records(self):
    self.window.Element('Records').Update(values=[])

  def set_record(self, position):
    current_records = []
    current_records = self.get_records() # get
    current_records.append(position) # add new
    self.window.Element('Records').Update(values=current_records)

  def enable_buttons_directions(self):
    self.window.Element('d_NW').Update(disabled=False)
    self.window.Element('d_N').Update(disabled=False)
    self.window.Element('d_NE').Update(disabled=False)
    self.window.Element('d_CW').Update(disabled=False)
    self.window.Element('d_C').Update(disabled=False)
    self.window.Element('d_CE').Update(disabled=False)
    self.window.Element('d_SW').Update(disabled=False)
    self.window.Element('d_S').Update(disabled=False)
    self.window.Element('d_SE').Update(disabled=False)

  def handle_direction_buttons(self, event):
    position = self.window.Element('_IN_').Get().split(',')
    pixel_tibia = 32
    x = int(position[0])
    y = int(position[1])

    if event == 'd_NW':
      self.set_record(position_to_array_string(x - pixel_tibia, y - pixel_tibia)) #north west
    if event == 'd_N':
      self.set_record(position_to_array_string(x, y - pixel_tibia)) #north center
    if event == 'd_NE':
      self.set_record(position_to_array_string(x + pixel_tibia, y - pixel_tibia)) #north east
    if event == 'd_CW':
      self.set_record(position_to_array_string(x - pixel_tibia, y)) #center west
    if event == 'd_C':
      self.set_record(position_to_array_string(x, y)) #center
    if event == 'd_CE':
      self.set_record(position_to_array_string(x + pixel_tibia, y)) #center east
    if event == 'd_SW':
      self.set_record(position_to_array_string(x - pixel_tibia, y + pixel_tibia)) #south west
    if event == 'd_S':
      self.set_record(position_to_array_string(x, y + pixel_tibia)) #south center
    if event == 'd_SE':
      self.set_record(position_to_array_string(x + pixel_tibia, y + pixel_tibia)) #south east

  def start_array_positions(self, array, duration, loop):

    if(loop == 0):
      loop = 9999

    i = 0
    while True:
      for position_string in array:
        x, y = array_string_to_position_obj(str(position_string))
        time.sleep(duration)

        pyautogui.dragTo(x, y)

      i = i + 1
      if(i == loop):  
          break

  def get_random_positions(self):
    num_random = randrange(0,8)

    if num_random == 0:
      self.handle_direction_buttons('d_NW')
    if num_random == 1:
      self.handle_direction_buttons('d_N')
    if num_random == 2:
      self.handle_direction_buttons('d_NE')
    if num_random == 3:
      self.handle_direction_buttons('d_CW')
    if num_random == 4:
      self.handle_direction_buttons('d_C')
    if num_random == 5:
      self.handle_direction_buttons('d_CE')
    if num_random == 6:
      self.handle_direction_buttons('d_SW')
    if num_random == 7:
      self.handle_direction_buttons('d_S')
    if num_random == 8:
      self.handle_direction_buttons('d_SE')




