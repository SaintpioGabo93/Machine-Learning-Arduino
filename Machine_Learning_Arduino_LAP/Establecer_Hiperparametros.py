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

# Declaración de la función de pérdida
perdida = 'mean_squared_error'
minimos_cuadrados = tf.keras.losses.MeanSquaredError()
perdida2 = 'binary_crossentropy'
entropiaBinaria_cruzada = tf.keras.losses.BinaryCrossentropy()
perdida3 = 'categorical_crossentropy'
entropiaCategorica_cruzada = tf.keras.losses.CategoricalCrossentropy()

# Optimizador... Calculo Vectorial :'v

optimizador = tf.keras.optimizers.SGD(learning_rate = tasa_aprendizaje)
optimizador1 = tf.keras.optimizers.RMSprop(learning_rate = tasa_aprendizaje)
optimizador2 = tf.keras.optimizers.Adam(learning_rate = tasa_aprendizaje)



