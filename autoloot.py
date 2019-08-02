import pyautogui, sys, time

current_position = pyautogui.position()

print(current_position)


#Point(x=320, y=265)


#    #229    #
#    #265    #
#    #301    #

#    #    #
#284    #320    #356
#    #    #

var = pyautogui.prompt('Write duration float example: var and press OK.')
var = float(var)
try:
    while True:
#pyautogui.dragTo(320, 265)
      pyautogui.dragTo(320, 301) #south center
      time.sleep(var)
      pyautogui.dragTo(284, 301) #south west
      time.sleep(var)
      pyautogui.dragTo(284, 265) #center west
      time.sleep(var)
      pyautogui.dragTo(284, 229) #north west
      time.sleep(var)
      pyautogui.dragTo(320, 229) #north center
      time.sleep(var)
      pyautogui.dragTo(356, 229) #north east
      time.sleep(var)
      pyautogui.dragTo(356, 265) #center east
      time.sleep(var)
      pyautogui.dragTo(356, 301) #south east
      time.sleep(var)
      #pyautogui.dragTo(320, 301) #south center
except KeyboardInterrupt:
  print('lol')