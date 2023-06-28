from readDataset import *
import matplotlib.pyplot as plt
import numpy as np

sizeClass = 5  # Cantidad de clases a clasificar

d = dataset(sizeClass)

d.read()

print(f"Size Input Data: {d.datasetInput.shape}")  # datasetInput [samples,input]

for i in range(sizeClass):
    print(f"Size Class Data {i + 1}: {d.sizeSubClass[i]}")

T = np.concatenate((0 * np.ones((d.sizeSubClass[0], 1)),
                    1 * np.ones((d.sizeSubClass[1], 1)),
                    2 * np.ones((d.sizeSubClass[2], 1)),
                    3 * np.ones((d.sizeSubClass[3], 1)),
                    4 * np.ones((d.sizeSubClass[4], 1))), axis=0)

print(f"Size Output Data: {T.shape}")  # datasetOutput[samples,output]

# Plot input
for i in range(d.numInputs):
    plt.plot(d.datasetInput[:, i], label='Data ' + str(i + 1))
    plt.legend(loc="upper left")

plt.grid()
plt.show()

np.save('P', d.datasetInput)
np.save('T', T)
