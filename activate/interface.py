from pynput.keyboard import Listener

class Event:
  objs = {}
  def __init__(self, key, func):
    self.func = func
    self.is_pressed = False
    self.objs[key] = self.func

  
class Agent(Listener):

  def __init__(self):
    super().__init__(on_press=self.on_press, on_release=self.on_release)

  def on_press(self, key):
   try:
      Event.objs[key]()
   except KeyError:
      pass

  def on_release(self, key):
    pass


__all__ = ('Event', 'Agent')
