from pyArduino.readDataset import *
import numpy as np

tamanioClase = 3 #Cantidad de clases a clasificar

d = dataset(tamanioClase)

d.read()

print(f'Tamaño de Datos de Entrada {d.datasetInput.shape}: ') # Colocación de datos de entrada [muestras, entradas]

for i in range(tamanioClase):
    print(f'Datos del tamaño de Clase {i+1}: {d.sizeSubClass[i]}')


##### Codificación de las etiquetas con un valo de 0m y nclases-1

T = np.concatenate((0*np.ones ((d.sizeSubClass[0],1)),
                    1*np.ones((d.sizeSubClass[1],1)),
                    2*np.ones((d.sizeSubClass[2],1))), axis = 0)

print(f'Tamaño de T: {T.shape }')

print(T)