from collections import defaultdict as ddict

class Trigger:
  events = ddict(str)
  objs = []
  def __init__(self, key, event, mus, **kwargs):
    self.key = key
    self.event = event
    self.mus = mus
    self.kwargs = kwargs
    self.objs.append(self)
  def update(self):
    if self.events[self.key] == self.event:
      for obj in self.objs:
        obj.mus.stop()
      self.mus.play(0, **self.kwargs) 
      del self.events[self.key]
