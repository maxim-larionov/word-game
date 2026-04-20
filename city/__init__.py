from display import Printer, Code
from typing import Iterable
import json

printer = Printer()
clear_code = Code('clear code')

class Point:
  def __init__(self, name, sub_points):
    self.name = name
    self.sub_points = sub_points
    self.master_point = None
    for point in sub_points:
      point.master_point = self
  def list(self):
    res = {}
    for point in self.sub_points:
      res[point.name] = point.list()
    return res
  __repr__ = lambda self: repr(self.list())

class Map:
  def __init__(self):
    with open('plot/tree.json', 'r') as f:
      self.tree = json.load(f)
    self.points = []
    self.points.append(self.unpuck(self.tree))
  
  def unpuck(self, tree, name=''):
    if not isinstance(tree, Iterable) or isinstance(tree, str):
      return Point(name, [])
    
    sub_points = []
    for key, value in tree.items():
      sub_point = self.unpuck(value, name=key)
      sub_points.append(sub_point)
    
    return Point(name, sub_points)
  
  def build(self):
    self.points.append(self.unpuck(self.tree))

