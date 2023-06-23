from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# Importar o generar conjunto de datos

P = np.load('Datos_Juntos.npy')
T = np.load('T.npy')

# Preprocesamiento de Datos

capa = StandardScaler().fit(P)

P = capa.transform(P)

# Dividmos el conjunto de datos en conjunto de entrenamiento y prueba

# test_size acepta float o none
# Si es float, debe estar entre 0.0 y 1.0 y representa el porcentaje del conjunto de datos a incluir en el conjunto de prueba.
# Si es int, representa el número absoluto de muestras de prueba a usar.
# Si es None, el valor se establece como complemento de train_size. Si train_size también es None, se establecerá en 0.25.

# shuffle:

# Si es True se mezclan los datos antes de dividirlos.

# random_state=42
# Garantiza que se genere la misma secuencia de números aleatorios cada vez que ejecute el código.

P_entrenamiento, P_prueba, T_entrenamiento, T_prueba = train_test_split(P, T, test_size = 0.20,shuffle = True, random_state = 42)

print(f'Tamaños de Datos de Entrada del Entrenamiento: {P_entrenamiento.shape}')
print(f'Tamaños de Datos de Entrada de Prueba: {P_prueba.shape}')

print(f'Tamaños de Datos de Salida del Entrenamiento: {T_entrenamiento.shape}')
print(f'Tamaños de Datos de Salida de Prueba: {T_prueba.shape}')
