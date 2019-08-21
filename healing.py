import pyscreenshot as ImageGrab

def screenshot_life():
  im = ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2
  im.show()