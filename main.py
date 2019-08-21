# C:\Users\NextPress\.windows-build-tools\python27\Scripts>pip install pynput

# C:\Users\NextPress\.windows-build-tools\python27\Scripts>pyinstaller -wF "C:/Users/NextPress/Desktop/bot/main.py"
# C:\Users\NextPress\.windows-build-tools\python27\Scripts>auto-py-to-exe

import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

import pyautogui, sys, time, mouse, keyboard
from PIL import Image
from constants import *
from functions import *
from drag_rotate import DragRotate
from healing import Healing

tab1_layout =  [
                [sg.T('Healing')],
                [sg.Button('Select area', key='btn_sa', button_color=('#000', '#fff'))],
                [sg.Button('Screenshot Life', key='btn_ss_life', button_color=('#000', '#fff'))],
                ]

tab2_layout = [
          [sg.Text('Click to select position of your character', background_color="#333", text_color="#fff")  ],
          [sg.Button('Select', key='btn_Select', button_color=('#000', '#fff'))],
          [sg.Input(do_not_clear=True, key='_IN_')],
          [sg.Text('Select directions', background_color="#333", text_color="#fff")],
          [sg.Button('North West', key='d_NW', size=('4','2'), disabled=True), sg.Button('North', key='d_N', size=('4','2'), disabled=True), sg.Button('North East', key='d_NE', size=('4','2'), disabled=True)],
          [sg.Button('Center West', key='d_CW', size=('4','2'), disabled=True), sg.Button('Center', key='d_C', size=('4','2'), disabled=True), sg.Button('Center East', key='d_CE', size=('4','2'), disabled=True)],
          [sg.Button('South West', key='d_SW', size=('4','2'), disabled=True), sg.Button('South', key='d_S', size=('4','2'), disabled=True), sg.Button('South East', key='d_SE', size=('4','2'), disabled=True)],
          [sg.Button('Clear', key='btn_Clear', button_color=('#FF333D', 'white'))],
          [sg.Listbox(key='Records', values=[], size=(30, 6))],
          [sg.Text('Repeat times: ', background_color="#333", text_color="#fff"), sg.Spin(key='Loop', values=[i for i in range(0,10)], size=(17, 6), initial_value=0)],
          [sg.Text('Note: 0 is infinite loop', font='Courier 8', background_color="#333", text_color="#fff")],
          [sg.Button('Start', key='btn_Start', disabled=True, button_color=('#000', '#fff')), sg.Button('Default', key='btn_Default', disabled=True, button_color=('#000', '#fff')), sg.Exit(button_color=('#000', '#fff'))]
          ]

layout = [
          [sg.TabGroup([[sg.Tab('Healing', tab1_layout, background_color="#333", title_color="#333" ), sg.Tab('Drag and Drop', tab2_layout, background_color="#333", title_color="#333")]], background_color="#333")],
         ]

window = sg.Window(title_program, layout, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True, return_keyboard_events=True, margins=(1,1), background_color="#333")

#Declaring classes passing window param
drag_rotate = DragRotate(window)
healing = Healing(window)

def image_follow_mouse():
  print(win32gui.GetCursor)
  while mouse.is_pressed():
    print(mouse.get_position())
    print(mouse.is_pressed())
    if not mouse.is_pressed():
      break
      mouse.unhook_all()



while True:
    event, values = window.Read()

    if not event == 'NoneType' and 'd_' in event:
      drag_rotate.handle_direction_buttons(event)
    if event == 'btn_Start':
      drag_rotate.start_array_positions(drag_rotate.get_records(), 0.05, drag_rotate.get_repeats())
    if event == 'btn_Default':
      position = window.Element('_IN_').Get().split(',')
      drag_rotate.start( int(position[0]), int(position[1]) )
    if event == 'btn_Select':
      mouse.on_click(drag_rotate.get_current_position)
    if event == 'btn_Clear':
      drag_rotate.clear_records()
    if event == 'btn_ss_life':
      healing.screenshot_life()
    if event == 'btn_sa':
      from mouse._mouse_event import ButtonEvent, MoveEvent, WheelEvent, LEFT, RIGHT, MIDDLE, X, X2, UP, DOWN, DOUBLE
      mouse.on_button(image_follow_mouse, (), [LEFT], [DOWN])

    if event is None or event == 'Exit':
      print('END PROGRAM')
      break

    #print(event, values)

window.Close()