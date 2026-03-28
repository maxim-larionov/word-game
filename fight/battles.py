from display import Code, Printer
import fight.mechanics
clear = Code('clear code')
printer = Printer()

class Player:
  def __init__(self, props='default', lvl=4, *, clr):
    self.lvl = lvl
    self.props = props if props != 'default' else {'health': 1/2, 'attack': 1/4, 'defence': 1/4} 
    self.get_par = lambda par: self.props[par] * 4 * self.lvl ** 1.1 + 10
