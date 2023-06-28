import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

from arduinoKeras import weights
from arduinoKeras import layers
from arduinoKeras import scaling

import matplotlib.pyplot as plt

# Importar o generar conjuntos de datos

P = np.load('P.npy')
T = np.load('T.npy')

# Preprocesamiento de datos.
from sklearn.preprocessing import StandardScaler  # pip install -U scikit-learn

scaler = StandardScaler().fit(P)

P = scaler.transform(P)

one_hot_labels = to_categorical(T, num_classes=5)

# Dividir el conjuntos de datos en conjuntos de entrenamiento y prueba.
from sklearn.model_selection import train_test_split

P_train, P_test, T_train, T_test = train_test_split(P, one_hot_labels, test_size=0.20, random_state=42)

# Establecer hiperparámetros de algoritmo (tasa de aprendizaje, épocas).
epochs = 500
hiddenNodes = 2

# Definir la arquitectura de la red neuronal.
model = Sequential()
model.add(Dense(hiddenNodes, activation='relu', input_dim=3))
model.add(Dense(5, activation='softmax'))
model.summary()

# Declara las funcion de pérdida.
loss = 'categorical_crossentropy'

# Optimizador.
optimizer = tf.keras.optimizers.Adam()

model.compile(loss=loss,
              optimizer=optimizer,
              metrics=['accuracy'])

# Entrenar el modelo
history = model.fit(P_train, T_train, epochs=epochs, verbose=1, validation_split=0.1)
plt.xlabel('Epocas')
plt.ylabel('Pérdida')
plt.plot(history.epoch, np.array(history.history['loss']), 'b', label='Train Loss')
plt.plot(history.epoch, np.array(history.history['val_loss']), 'r', label='Val Loss')
plt.legend()
plt.grid()

# Evaluar el modelo
test_loss, test_acc = model.evaluate(P_test, T_test, verbose=1)
print('Exactitud de prueba: ', test_acc)

# Extraer valores pesos,normalizacion y la arquitectura de la red para Arduino
weights(model.layers, 3)
scaling(scaler, 3)
layers(model.layers)

plt.show()
