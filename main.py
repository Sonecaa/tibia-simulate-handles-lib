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
from utils_ui import Utils_Ui
from drag_rotate import DragRotate
from healing import Healing
from rune_maker import RuneMaker
from flower import Flower

tab1_layout = [
                [sg.T('Healing')],
                [sg.Button('Screenshot Life', key='btn_ss_life', button_color=('#000', '#fff'))],
                [sg.Button('Get locate mana', key='xxxxx', button_color=('#000', '#fff'))],
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
                [sg.Text('Speed: ', background_color="#333", text_color="#fff"), sg.Spin(key='Speed', values=[], size=(17, 6), initial_value=0.03)],
                [sg.Text('Note: 0 is infinite loop', font='Courier 8', background_color="#333", text_color="#fff")],
                [sg.Button('Start', key='btn_Start', disabled=True, button_color=('#000', '#fff')), sg.Button('Random', key='btn_Random', disabled=True, button_color=('#000', '#fff')), sg.Exit(button_color=('#000', '#fff'))]
              ]

tab3_layout = [
                [sg.T('Rune Maker')],
                [sg.Text('Spell: ', background_color="#333", text_color="#fff"), sg.Input(key='RM_txt_spell')],
                [sg.Text('Speed: ', background_color="#333", text_color="#fff"), sg.Spin(key='RM_txt_speed', values=[], size=(17, 6), initial_value=0)],
                [sg.Button('Start', key='RM_btn_start', button_color=('#000', '#fff'))],
                [sg.Button('Stop', key='RM_btn_stop', button_color=('#000', '#fff'))],
              ]

tab4_layout = [
                [sg.T('Flower')],
                [sg.Text('Click to select position of your character', background_color="#333", text_color="#fff")  ],
                [sg.Button('Select', key='F_btn_pos_char', button_color=('#000', '#fff'))],
                [sg.Input(do_not_clear=True, key='F_txt_pos_char')],
                [sg.Text('Click to select position of first item of flower backpack', background_color="#333", text_color="#fff")  ],
                [sg.Button('Select', key='F_btn_pos_bp_first', button_color=('#000', '#fff'))],
                [sg.Input(do_not_clear=True, key='F_txt_pos_bp_first')],
                #[sg.Text('Enable flowers on numpad: ', background_color="#333", text_color="#fff"), sg.Checkbox('', key='F_chkbox', disabled=True)],
              ]

layout = [
          [sg.TabGroup([
            [
            sg.Tab('Healing', tab1_layout, background_color="#333", title_color="#333" ), 
            sg.Tab('Drag and Drop', tab2_layout, background_color="#333", title_color="#333"),
            sg.Tab('Rune Maker', tab3_layout, background_color="#333", title_color="#333"),
            sg.Tab('Flower', tab4_layout, background_color="#333", title_color="#333"),
            ]
          ], background_color="#333"),],
         ]

window = sg.Window(title_program, layout, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True, return_keyboard_events=True, margins=(1,1), background_color="#333")

#Declaring classes passing window param
utils_ui = Utils_Ui(window)
drag_rotate = DragRotate(window)
healing = Healing(window)
rune_maker = RuneMaker(window)
flower = Flower(window)

while True:
    event, values = window.Read()

    # START DRAG AND DROP
    if not event == 'NoneType' and 'd_' in event:
      drag_rotate.handle_direction_buttons(event)

    if event == 'btn_Start':
      drag_rotate.start_array_positions(drag_rotate.get_records(), drag_rotate.get_speed(), drag_rotate.get_repeats())

    if event == 'btn_Random':
      drag_rotate.get_random_positions()
      #drag_rotate.start_array_positions(drag_rotate.get_records(), 0.05, drag_rotate.get_repeats())

    if event == 'btn_Select':
      utils_ui.get_mouse_position_on_click('_IN_')
      window.Element('btn_Random').Update(disabled=False)
      window.Element('btn_Start').Update(disabled=False)
      drag_rotate.enable_buttons_directions()
      drag_rotate.clear_records()

    if event == 'btn_Clear':
      drag_rotate.clear_records()
    # END DRAG AND DROP

    # START RUNE MAKER
    if event == 'RM_btn_start':
      rune_maker.making_runes()
    # END RUNE MAKER  

    # START FLOWER
    if event == 'F_btn_pos_char':
     utils_ui.get_mouse_position_on_click('F_txt_pos_char')
     flower.set_numpad_hotkeys()

    if event == 'F_btn_pos_bp_first':
     utils_ui.get_mouse_position_on_click('F_txt_pos_bp_first')
    # END FLOWER  

    if event is None or event == 'Exit':
      print('END PROGRAM')
      break

    #print(event, values)

window.Close()