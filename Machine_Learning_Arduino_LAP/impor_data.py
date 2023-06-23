import numpy as np
import matplotlib.pyplot as plt

############################ Cargar señales medidas #######################
with open('p1.npy', 'rb') as f:
    p  = np.load(f)