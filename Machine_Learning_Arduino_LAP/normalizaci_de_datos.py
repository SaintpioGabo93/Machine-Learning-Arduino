from sklearn.preprocessing import StandardScaler
import numpy as np

p = np.array([[0.1,0.5],[0.8,0.34],[1.5,0.7]]) # [Muestras, entradas]
capas = StandardScaler().fit(p)
datosNormalizados = capas.transform(p)

print(f'Valores medios con sci learn {capas.mean_}')
print(f'Desviación estandar con sci learn {np.sqrt(capas.var_)}')

############################## Con Tensorflow

import tensorflow as tf
from tensorflow.keras.layers.experimental import preprocessing

p1 = np.array([[0.1,0.5],[0.8,0.34],[1.5,0.7]])

capas1 = preprocessing.Normalization()
capas1.adapt(p)
datosNormalizados1 = capas1(p1)

print(f'Valores Medios con TensorFlow {capas1.mean.numpy()}')
print(f'Desviación estandar con TensorFlow {np.sqrt(capas1.variance.numpy())}')