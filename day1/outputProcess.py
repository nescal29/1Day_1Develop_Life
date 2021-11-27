import matplotlib.pyplot as plt
import matplotlib.patches as patches

class OutputProcess():
  def inputData(self, data=''):
    if data == '':
      data = 'test'

    self.outputData(data)

  def outputData(self, data=''):
    fig = plt.figure()
    ax = plt.axes()

    # fc = face color, ec = edge color
    palette = patches.Circle(xy=(0, 0), radius=0.5, fc=data)
    ax.add_patch(palette)
    plt.axis('scaled')

    plt.savefig('./matplotlib_patches.png')

    
if __name__ == '__main__':
  outputPrc = OutputProcess()
  outputPrc.inputData()
