import numpy as np
import pylab as pl

x=[1,2,3,4,5]
y=[1,4,9,16,25]

pl.plot(x,y,'ro')
pl.axis([0,6,0,26])
pl.savefig('temp1.png')
pl.show()
