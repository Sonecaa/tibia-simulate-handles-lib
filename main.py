# C:\Users\NextPress\.windows-build-tools\python27\Scripts>pip install pynput

import pyautogui, sys


pyautogui.displayMousePosition()

screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)

currentMouseX, currentMouseY = pyautogui.position() # Retursn two integes, the x and y of the mouse cursor's current position.

#pyautogui.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
#pyautogui.moveTo(1000, 1500) # Move the mouse to the x, y coordinates 100, 150.
#pyautogui.moveTo(500, 650) # Move the mouse to the x, y coordinates 100, 150.
#pyautogui.moveTo(800, 350) # Move the mouse to the x, y coordinates 100, 150.


#pyautogui.alert('Finish Script')
#pyautogui.confirm('This displays text and has an OK and Cancel button.')
#var = pyautogui.prompt('This lets the user type in a string and press OK.')
#pyautogui.alert(var)


#pyautogui.click() # Click the mouse at its current location.
#pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

#pyautogui.dragTo(x, y, duration=num_seconds)  # drag mouse to XY