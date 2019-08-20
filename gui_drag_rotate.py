import PySimpleGUI27 as sg
import pyautogui, sys, time, mouse, keyboard
from constants import *
from functions import *
from drag_rotate import *

current_position = ''


# ------ Menu Definition ------ #
menu_def = [['&Options', ['&1', '&2', '3', '4']],
            ['&Help', '&About...'], ]

sg.ChangeLookAndFeel('Black')
layout = [[sg.Menu(menu_def, tearoff=True)],
          [sg.Text('Click to select position of your character')],
          [sg.Button('Select', key='Select')],
          [sg.Input(do_not_clear=True, key='_IN_')],
          [sg.Text('Select directions')],
          [sg.Button('North West', key='d_NW', size=('4','2'), disabled=True), sg.Button('North', key='d_N', size=('4','2'), disabled=True), sg.Button('North East', key='d_NE', size=('4','2'), disabled=True)],
          [sg.Button('Center West', key='d_CW', size=('4','2'), disabled=True), sg.Button('Center', key='d_C', size=('4','2'), disabled=True), sg.Button('Center East', key='d_CE', size=('4','2'), disabled=True)],
          [sg.Button('South West', key='d_SW', size=('4','2'), disabled=True), sg.Button('South', key='d_S', size=('4','2'), disabled=True), sg.Button('South East', key='d_SE', size=('4','2'), disabled=True)],
          [sg.Button('Clear', key='Clear', button_color=('#FF333D', 'white'))],
          [sg.Listbox(key='Records', values=[], size=(30, 6))],
          [sg.Button('Start', key='Start', disabled=True), sg.Button('Default', key='Default', disabled=True), sg.Exit()]]

window = sg.Window(title_program, layout, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True, return_keyboard_events=True)

def get_records():
  return window.Element('Records').GetListValues()

def clear_records():
  window.Element('Records').Update(values=[])

def set_record(position):
  current_records = []
  current_records = get_records() # get
  current_records.append(position) # add new
  window.Element('Records').Update(values=current_records)

def get_current_position():
  position_x, position_y = mouse.get_position()
  window.Element('_IN_').Update(str(position_x) + ',' + str(position_y))

  window.Element('Default').Update(disabled=False)
  window.Element('Start').Update(disabled=False)
  enable_buttons_directions()

  mouse.unhook_all()

def enable_buttons_directions():
  window.Element('d_NW').Update(disabled=False)
  window.Element('d_N').Update(disabled=False)
  window.Element('d_NE').Update(disabled=False)
  window.Element('d_CW').Update(disabled=False)
  window.Element('d_C').Update(disabled=False)
  window.Element('d_CE').Update(disabled=False)
  window.Element('d_SW').Update(disabled=False)
  window.Element('d_S').Update(disabled=False)
  window.Element('d_SE').Update(disabled=False)

def handle_direction_buttons(event):
  position = window.Element('_IN_').Get().split(',')
  pixel_tibia = 36
  x = int(position[0])
  y = int(position[1])

  if event == 'd_NW':
    set_record(position_to_array_string(x - pixel_tibia, y - pixel_tibia)) #north west
  if event == 'd_N':
    set_record(position_to_array_string(x, y - pixel_tibia)) #north center
  if event == 'd_NE':
    set_record(position_to_array_string(x + pixel_tibia, y - pixel_tibia)) #north east
  if event == 'd_CW':
    set_record(position_to_array_string(x - pixel_tibia, y)) #center west
  if event == 'd_C':
    set_record(position_to_array_string(x, y)) #center
  if event == 'd_CE':
    set_record(position_to_array_string(x + pixel_tibia, y)) #center east
  if event == 'd_SW':
    set_record(position_to_array_string(x - pixel_tibia, y + pixel_tibia)) #south west
  if event == 'd_S':
    set_record(position_to_array_string(x, y + pixel_tibia)) #south center
  if event == 'd_SE':
    set_record(position_to_array_string(x + pixel_tibia, y + pixel_tibia)) #south east

while True:
    event, values = window.Read()

    if 'd_' in event:
      handle_direction_buttons(event)
    if event == 'Start':
      start_array_positions(get_records(), 0.05)
    if event == 'Default':
      position = window.Element('_IN_').Get().split(',')
      start( int(position[0]), int(position[1]) )
    if event == 'Select':
      mouse.on_click(get_current_position)
    if event == 'Clear':
      clear_records()
      print(get_records())
    if event is None or event == 'Exit':
      print('END PROGRAM')
      break

    #print(event, values)

window.Close()