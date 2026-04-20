import random

perc = lambda i: round(i / 100, 2)
rperc = lambda: perc(random.random() * 100)
randbool = lambda percents: rperc() <= percents

class Attack:
  def __init__(self, strong, *, accurate=perc(90), func="default"):
    self.accurate = accurate
    self.strong = strong
    self.func = func
  
