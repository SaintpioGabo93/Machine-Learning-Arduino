import time

import numpy as np
from pyArduino import *
import matplotlib.pyplot as plt
from pyArduino.serialArduino import serialArduino

tiempo_muestreo = 0.1
lectura_sensor = 10
tiempo = np.arange(0, lectura_sensor + tiempo_muestreo, tiempo_muestreo)
numero_de_muestras = len(tiempo)

puerto_COM = 'COM7'
razon_baudios = 9600
tamanio_datos = 6  # Los datos de traslación en z, y, z. Y de la rotación en z, y, z.

arduino = serialArduino(puerto_COM, razon_baudios, tamanio_datos)
arduino.readSerialStart()

p = np.zeros((tamanio_datos,numero_de_muestras)) # Vector para guardar los datos de lectura

for k in range(numero_de_muestras):

    tiempo_inicio = time.time()

    for i in range(tamanio_datos):

        p[i][k] = arduino.rawData[i]

    tiempo_transcurrido = time.time() -tiempo_inicio

    time.sleep(tiempo_muestreo-tiempo_transcurrido)

arduino.close()


with open('DataSet.npy','wb') as f:
    np.save(f,p)
    np.save(f,tiempo)
    np.save(f,tiempo_muestreo)

for i in range(tamanio_datos):
    plt.plot(tiempo, p[i, :], label = 'Datos'+str(i+1))


plt.xlabel('Tiempo [s]')
plt.grid()
plt.legend(loc='upper left')
plt.show()
