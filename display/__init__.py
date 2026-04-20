import json

code_file = open('display/codes.json')

class Code:
  codes = json.load(code_file)
  def __init__(self, name):
    self.func = self.codes[name]
  def __call__(self):
    print(self.func)

class Printer:
  red = (255, 0, 0)
  green = (0, 255, 0)
  blue = (0, 0, 255)
  def rgb_print(text, *rgb):
    print('\033[38;2;{};{};{}m%s\033[0m'.format(rgb) % text)
    
