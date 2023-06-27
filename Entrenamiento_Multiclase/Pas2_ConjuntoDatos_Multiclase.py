from pyArduino.readDataset import *
import matplotlib.pyplot as plt
import numpy as np

tamanioClase = 5  # Cantidad de clases a clasificar

d = dataset(tamanioClase)

d.read()

print(f"Tamaño de Datos de Entrada: {d.datasetInput.shape}")  # Conjunto de Datos de Entrada [muestras,entrada]

for i in range(tamanioClase):
    print(f"Datos de Tamaño de Clase {i + 1}: {d.sizeSubClass[i]}")

T = np.concatenate((0 * np.ones((d.sizeSubClass[0], 1)),
                    1 * np.ones((d.sizeSubClass[1], 1)),
                    2 * np.ones((d.sizeSubClass[2], 1)),
                    3 * np.ones((d.sizeSubClass[3], 1)),
                    4 * np.ones((d.sizeSubClass[4], 1))), axis=0) #Este método
# le agrega las etiquetas a las clases y las convierte en un tensor



print(f"Tamaño de Datos de Salida: {T.shape}")  # Conjunt de Datos Salida[samples,output]

# Plot input
for i in range(d.numInputs): # Este ciclo for junta tanto las clases positivas como las negativas
    plt.plot(d.datasetInput[:, i], label='Datos ' + str(i + 1))
    plt.legend(loc="upper left")

plt.grid()
plt.show()

np.save('ConjuntoDatos', d.datasetInput) # Crean el tensor de Datos
np.save('TensorClases', T) # Crean el tensor de Clases