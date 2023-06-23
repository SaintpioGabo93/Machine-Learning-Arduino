from pyArduino.readDataset import *
import matplotlib.pyplot as plt
import numpy as np

tamanioClase = 2 # Cantidad de clases a clasificar, en este caso la del movimiento que queremos (Positiva) y la de los movimientos que vamos a descartar (Negativa)
d = dataset(tamanioClase)

d.read()

print(f'Tamaño de datos de entrada: {d.datasetInput.shape}')

for i in range(tamanioClase):
    print(f'Tamaño de clase de datos {i + 1}: {d.sizeSubClass[i]}')


# Grafica de entradas

for i in range (d.numInputs):
    plt.plot(d.datasetInput[:,i], label = 'Datos '+str(i+1))
    plt.legend(loc= 'upper left')

plt.grid()
plt.show()

np.save('Datos_Juntos', d.datasetInput)