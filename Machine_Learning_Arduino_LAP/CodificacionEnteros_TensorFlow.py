from tensorflow.keras.utils import to_categorical
from pyArduino.readDataset import *
import numpy as np

tamanioClase = 3

d = dataset(tamanioClase)

d.read()

print(f'Tamaño de Datos de Entrada: {d.datasetInput.shape}')
for i in range(tamanioClase):
    print(f'Datos de Tamaño de Clase {i+1}: {d.sizeSubClass[i]}')


##### Codificación de las etiquetas con un valor entre 0 y n_cñases-1

T = np.concatenate((0*np.ones((d.sizeSubClass[0],1)),
                    1*np.ones((d.sizeSubClass[1],1)),
                    2*np.ones((d.sizeSubClass[2],1))), axis=0)

print(f'Tamaño de T: {T.shape}')

etiqueta_oneHot = to_categorical(T, num_classes = tamanioClase)

print(f'Tamaño de la Codificación One Hot: {etiqueta_oneHot.shape}')

print(etiqueta_oneHot)