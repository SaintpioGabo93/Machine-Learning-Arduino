'''En este programa se van a obtener los tensores de Conjunto de Datos,
así como se le agregaran etiquetas de clasificación a nuestros datos
para la clase positiva será 1 y para la negativa 0

'''



from pyArduino.readDataset import *
import matplotlib.pyplot as plt
import numpy as np

tamanioClase = 2  # Cantidad de clases a clasificar

d = dataset(tamanioClase)

d.read()

print(f"Tamaño de Datos de Entrada: {d.datasetInput.shape}")  # Conjunto de Datos de Entrada [muestras,entrada]

for i in range(tamanioClase):
    print(f"Datos de Tamaño de Clase {i + 1}: {d.sizeSubClass[i]}")

T = np.concatenate((np.ones((d.sizeSubClass[0], 1)), 0 * np.ones((d.sizeSubClass[1], 1))), axis=0) #Este método
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