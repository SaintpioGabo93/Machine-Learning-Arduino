import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

# Importación o Generación de Datos

P = np.load('Datos_Juntos.npy')
T = np.load('T.npy')

# Preprocesamiento de Datos

from sklearn.preprocessing import StandardScaler

escalador = StandardScaler().fit(P)

# División de Conjunto de Datos de entrenamiento y prueba.

from sklearn.model_selection import train_test_split

P_entrenamiento, P_prueba, T_entrenamiento, T_prueba = train_test_split(P, T, test_size = 0.20, shuffle = True, random_state = 42)


# Establecimiento de los Hiperparámetros de algoritmo (tasa de aprendizaje, épocas)

epocas = 100
tasa_aprendizaje = 0.01
nodos_ocultos = 2

# Inicialización de pesos y sesgos

inizializador_pesos = tf.keras.initializers.RandomNormal()

W = inizializador_pesos(shape = (2,2))
inicializador_bias = tf.keras.initializers.Zeros() # No se recomienda usar zeros, pero se usan aquí para fines pedagógicos
b = inicializador_bias(shape=(1,2))

# Definición de la arquitectura de la Red Neuronal
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import  Dense

modelo = Sequential()
modelo.add(Dense(nodos_ocultos, activation = 'relu', input_dim = 3, kernel_initializer = inizializador_pesos, bias_initializer = inicializador_bias))
modelo.add(Dense(1, activation = 'sigmoid'))
modelo.summary()

#### Otros Modelos #####################################################3

modelo2 = Sequential()
modelo2.add(Dense(nodos_ocultos, activation = 'relu', input_dim = 3, kernel_initializer = inizializador_pesos, bias_initializer = inicializador_bias))
modelo2.add(Dense(1, activation = 'sigmoid'))
modelo2.summary()

modelo3 = Sequential()
modelo3.add(Dense(nodos_ocultos, activation = 'relu', input_dim = 3, kernel_initializer = inizializador_pesos, bias_initializer = inicializador_bias))
modelo3.add(Dense(1, activation = 'sigmoid'))
modelo3.summary()

###################################################################

# Declaración de la función de pérdida
perdida = 'mean_squared_error'
minimos_cuadrados = tf.keras.losses.MeanSquaredError()
perdida2 = 'binary_crossentropy'
entropiaBinaria_cruzada = tf.keras.losses.BinaryCrossentropy()
perdida3 = 'categorical_crossentropy'
entropiaCategorica_cruzada = tf.keras.losses.CategoricalCrossentropy()

# Optimizador... Calculo Vectorial :'v

optimizador = tf.keras.optimizers.SGD(learning_rate = tasa_aprendizaje)
optimizador2 = tf.keras.optimizers.RMSprop(learning_rate = tasa_aprendizaje)
optimizador3 = tf.keras.optimizers.Adam(learning_rate = tasa_aprendizaje)

modelo.compile(loss = perdida, optimizer = optimizador)
modelo2.compile(loss = perdida2, optimizer = optimizador2)
modelo3.compile(loss = perdida3, optimizer = optimizador3)


#Entrenamiento del modelo

historia = modelo.fit(P_entrenamiento, T_entrenamiento,epochs = epocas, verbose = 1)

plt.xlabel('Epocas')
plt.ylabel('Pérdida')
plt.plot(historia.epoch, np.array(historia.historia['loss']),'b', label='Train Loss')
plt.legend()
plt.grid()

plt.show()

historia2 = modelo2.fit(P_entrenamiento, T_entrenamiento,epochs = epocas, verbose = 1)

plt.xlabel('Epocas')
plt.ylabel('Pérdida')
plt.plot(historia2.epoch, np.array(historia2.historia2['loss']),'b', label='Train Loss')
plt.legend()
plt.grid()

plt.show()

historia3 = modelo3.fit(P_entrenamiento, T_entrenamiento,epochs = epocas, verbose = 1)

plt.xlabel('Epocas')
plt.ylabel('Pérdida')
plt.plot(historia3.epoch, np.array(historia3.historia3['loss']),'b', label='Train Loss')
plt.legend()
plt.grid()

plt.show()

