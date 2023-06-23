import numpy as np
import matplotlib.pyplot as plt

######### Cargas Señales Medidas ############

with open('p1.npy','rb') as f:

    p = np.load(f)
    t = np.load(f)
    ts = np.load(f)


######## Mostrar Figuras #########

for i in range(p.shape[0]):
    plt.plot(t,p[i,:], label = 'Datos '+str(i+1))



plt.xlabel('Tiempo [s]')
plt.grid()
plt.legend(loc='upper left')
plt.show()