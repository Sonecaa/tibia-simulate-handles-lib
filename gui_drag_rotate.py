import PySimpleGUI27 as sg
import pyautogui, sys, time, mouse, keyboard
from constants import *
from functions import *
from drag_rotate import *

current_position = ''


tab1_layout =  [[sg.T('Healing')]]
tab2_layout = [
          [sg.Text('Click to select position of your character', background_color="#333", text_color="#fff")  ],
          [sg.Button('Select', key='Select', button_color=('#000', '#fff'))],
          [sg.Input(do_not_clear=True, key='_IN_')],
          [sg.Text('Select directions', background_color="#333", text_color="#fff")],
          [sg.Button('North West', key='d_NW', size=('4','2'), disabled=True), sg.Button('North', key='d_N', size=('4','2'), disabled=True), sg.Button('North East', key='d_NE', size=('4','2'), disabled=True)],
          [sg.Button('Center West', key='d_CW', size=('4','2'), disabled=True), sg.Button('Center', key='d_C', size=('4','2'), disabled=True), sg.Button('Center East', key='d_CE', size=('4','2'), disabled=True)],
          [sg.Button('South West', key='d_SW', size=('4','2'), disabled=True), sg.Button('South', key='d_S', size=('4','2'), disabled=True), sg.Button('South East', key='d_SE', size=('4','2'), disabled=True)],
          [sg.Button('Clear', key='Clear', button_color=('#FF333D', 'white'))],
          [sg.Listbox(key='Records', values=[], size=(30, 6))],
          [sg.Text('Repeat times: ', background_color="#333", text_color="#fff"), sg.Spin(key='Loop', values=[i for i in range(0,10)], size=(17, 6), initial_value=0)],
          [sg.Text('Note: 0 is infinite loop', font='Courier 8', background_color="#333", text_color="#fff")],
          [sg.Button('Start', key='Start', disabled=True, button_color=('#000', '#fff')), sg.Button('Default', key='Default', disabled=True, button_color=('#000', '#fff')), sg.Exit(button_color=('#000', '#fff'))]
          ]



layout = [
          [sg.TabGroup([[sg.Tab('Healing', tab1_layout, background_color="#333", title_color="#333" ), sg.Tab('Drag and Drop', tab2_layout, background_color="#333", title_color="#333")]], background_color="#333")],
         ]

window = sg.Window(title_program, layout, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True, return_keyboard_events=True, margins=(1,1), background_color="#333")

def get_records():
  return window.Element('Records').GetListValues()

def get_repeats():
  return int(window.Element('Loop').Get())

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
      start_array_positions(get_records(), 0.05, get_repeats())
    if event == 'Default':
      position = window.Element('_IN_').Get().split(',')
      start( int(position[0]), int(position[1]) )
    if event == 'Select':
      mouse.on_click(get_current_position)
    if event == 'Clear':
      clear_records()
    if event is None or event == 'Exit':
      print('END PROGRAM')
      break

    #print(event, values)

window.Close()