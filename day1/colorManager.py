import random

class ColorManager():
  def __init__(self):
    self.colorCode: str = '#'

  def randomGenerate(self):
    r: int = lambda: random.randint(0, 255)
    self.colorCode += '%02X%02X%02X' % (r(), r(), r())
    print('Generated ColorCode :', self.colorCode)
    return self.colorCode
    

if __name__ == '__main__':
  colmg = ColorManager()
  colmg.randomGenerate()
