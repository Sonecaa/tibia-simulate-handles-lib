from constants import *
from drag_rotate import *
import PySimpleGUI27 as sg
import pyautogui, sys, time, mouse, keyboard

current_position = ''


# ------ Menu Definition ------ #
menu_def = [['&Options', ['&1', '&2', '3', '4']],
            ['&Help', '&About...'], ]

sg.ChangeLookAndFeel('Black')
layout = [[sg.Menu(menu_def, tearoff=True)],
          [sg.Text('Click to select position of your character')],
          [sg.Button('Select', key='Select', button_color=('white', 'black'))],
          [sg.Input(do_not_clear=True, key='_IN_')],
          [sg.Button('Confirm', key='Confirm', disabled=True), sg.Exit()]]
          
window = sg.Window(title_program, layout, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True, return_keyboard_events=True)

def get_current_position():
    position_x, position_y = mouse.get_position()
    window.Element('_IN_').Update(str(position_x) + ',' + str(position_y))
    mouse.unhook_all()

while True:
    event, values = window.Read()

    if event == 'Confirm':
      position = window.Element('_IN_').Get().split(',')
      start( int(position[0]), int(position[1]) )
    if event == 'Select':
      mouse.on_click(get_current_position)
      window.Element('Confirm').Update(disabled=False)
    if event is None or event == 'Exit':
      print('END PROGRAM')
      break

    print(event, values)

window.Close()