import matplotlib.pyplot as plt
from pyArduino.pyArduinoPlot import *

############### Datos para la graficadora #################


muestrasMaximas = 100
tiempoMuestreo = 100
tamanioDatos = 6
nombreEtiqueta = ['Eje x','Eje y','Eje z', 'Giro x','Giro y','Giro z']
limite_x = [(0,muestrasMaximas)]*tamanioDatos # Estos límites iran en Captura Datos Gráfica
limite_y = [(-20,20),(-20,20),(-20,20),(-500,500),(-500,500),(-500,500)]
estilo = ['r-','g-','b-','r-','g-','b-']
datosGuardados = []

################## Comunicación Arduino Python ###############

puerto = 'COM5'
razonBaudios = 9600

arduino = realTimePlot(puerto,razonBaudios,muestrasMaximas,tamanioDatos)
arduino.readSerialStart()

################# Captura Datos Gráfica ###############

for i in range(tamanioDatos):
    fig, ax = makeFigure(limite_x[i],limite_y[i],'Datos' + str(i+1))
    lineas = ax.plot([],[],estilo[i],label = nombreEtiqueta[i])[0]
    nombreValor = ax.text(0.50,0.90,'', transform = ax.transAxes)
    datosGuardados.append(animation.FuncAnimation(fig,arduino.getSerialData, fargs= (lineas,nombreValor,nombreEtiqueta[i],i),interval = tiempoMuestreo))
    plt.legend(loc = 'upper left')
    plt.grid()


plt.show()

arduino.close()
