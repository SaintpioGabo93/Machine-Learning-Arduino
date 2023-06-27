import numpy as np
import tensorflow as tf

from pyArduino.arduinoKeras import weights
from pyArduino.arduinoKeras import layers
from pyArduino.arduinoKeras import scaling

import matplotlib.pyplot as plt

# Importar o generar conjuntos de datos

P = np.load('ConjuntoDatos.npy')
T = np.load('TensorClases.npy')

# Preprocesamiento de datos.
from sklearn.preprocessing import StandardScaler  # pip install -U scikit-learn


escalador = StandardScaler().fit(P)

P = escalador.transform(P)

# Dividir el conjuntos de datos en conjuntos de entrenamiento y prueba.
from sklearn.model_selection import train_test_split

P_entrenamiento, P_prueba, T_entrenamiento, T_prueba = train_test_split(P, T, test_size=0.20,shuffle= True, random_state=42)

# Establecer hiperparámetros de algoritmo (tasa de aprendizaje, épocas).
epocas = 1000
    # tasa_aprendizaje = 0.01 Solo para optimizador SDG
nodos_ocultos = 2

                # Inicialización de Pesos y sesgos..

                 # Ya no hace falta poner los pesos y sesgos, porque el programa y a lo hace

# Definir la arquitectura de la red neuronal.
from keras.models import Sequential
from keras.layers import Dense

modelo = Sequential()
modelo.add(Dense(nodos_ocultos, activation='relu', input_dim=3))
modelo.add(Dense(1, activation='sigmoid'))
modelo.summary()

# Declara las funcion de pérdida.
perdida = 'binary_crossentropy'

# Optimizador.

        #Pueden ser optimizador SGD(learning_rate = tasa_aprendizaje ), RMSprop, Adam
optimizador = tf.keras.optimizers.RMSprop()

modelo.compile(loss=perdida,
              optimizer=optimizador,
              metrics=['accuracy'])

# Entrenar el modelo

history = modelo.fit(P_entrenamiento, T_entrenamiento, epochs=epocas, verbose=1, validation_split=0.1) # Validation Split
        # Es un parámetro de conjunto de validación y corroborar si está bien
        # Nuestro algoritmo
plt.xlabel('Epocas')
plt.ylabel('Pérdida')
plt.plot(history.epoch, np.array(history.history['loss']), 'b', label='Perdida Entrenamiento')
plt.plot(history.epoch, np.array(history.history['val_loss']), 'r', label='Pérdida Validación')
plt.legend()
plt.grid()

# Evaluar el modelo
perdida_prueba, exactitud_prueba = modelo.evaluate(P_prueba, T_prueba, verbose=1)
print('Exactitud de prueba: ', exactitud_prueba)

# Extraer valores pesos,normalizacion y la arquitectura de la red para Arduino
weights(modelo.layers, 3)
scaling(escalador, 3)
layers(modelo.layers)

plt.show()
