from PIL import ImageGrab

class Healing:

  window = None

  def __init__(self, window): 
    self.window = window

  def screenshot_life(self):
    image = ImageGrab.grab(bbox=(300,100,500,500))
    image.save("life.jpg", "JPEG")
    #image.show()