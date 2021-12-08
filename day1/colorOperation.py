import random
from outputProcess import OutputProcess

class ColorOperation():
  def __init__(self):
    self.colorCode: str = '#'
    self.outputPrc = OutputProcess()

  def randomGenerate(self):
    r: int = lambda: random.randint(0, 255)
    self.colorCode += '%02X%02X%02X' % (r(), r(), r())
    print('Generated ColorCode :\033[32m', self.colorCode, '\033[0m')

    self.outputPrc.inputData(self.colorCode)
    

if __name__ == '__main__':
  colop = ColorOperation()
  colop.randomGenerate()
