import numpy as np
import pylab as pl

x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
y=[1,1,1,1,1,2,2,2,2,2,3,3,3,4,4,5,6,6,7,7,8,8]


pl.title('Numero de novias y mascotas por anio de vida')
pl.scatter(x, y, s=60, c='b', marker='o')
pl.ylabel('Numero de novias+mascotas')
pl.xlabel('Numero de anios')
pl.savefig('temp1b.png')
pl.show()
