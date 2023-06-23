from pyArduino.readDataset import *
import numpy as np

tamanioClase = 2 # Cantidad de clases que se van a clasificar

d = dataset(tamanioClase)

d.read()

print(f'Tamaño de los datos de entrada: {d.datasetInput.shape}')

for i in range(tamanioClase):
    print(f'Datos de Tamaño de Clase {i+1}: {d.sizeSubClass[i]}')

T = np.concatenate((np.ones((d.sizeSubClass[0],1)),0*np.ones((d.sizeSubClass[1],1))), axis = 0)

print(f'Tamaño de Datos de Salida: {T.shape}')

np.save('Datos_Juntos2.npy', d.datasetInput)

np.save('T', T)