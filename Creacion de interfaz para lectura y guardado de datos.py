from pyArduino.pyArduinoPlot import *
from tkinter import *

# Para este ejercicio sólo obtendremos unas muestras del acelerómetro por lo que comentaremos el código original
#de tiempo real

#
# muestrasMaximas = 100
# tiempoMuestreo = 100
# tamanioDatos = 6
# nombreEtiqueta = ['Eje x','Eje y','Eje z', 'Giro x','Giro y','Giro z']
# limite_x = [(0,muestrasMaximas)]*tamanioDatos # Estos límites iran en Captura Datos Gráfica
# limite_y = [(-20,20),(-20,20),(-20,20),(-500,500),(-500,500),(-500,500)]
# estilo = ['r-','g-','b-','r-','g-','b-']
# datosGuardados = []

muestrasMaximas = 100
tiempoMuestreo = 100
tamanioDatos = 3
nombreEtiqueta = ['Eje x','Eje y','Eje z']
limite_x = [(0,muestrasMaximas)]*tamanioDatos # Estos límites iran en Captura Datos Gráfica
limite_y = [(-20,20),(-20,20),(-20,20)]
estilo = ['r-','g-','b-']
datosGuardados = []

################## Comunicación Arduino Python ###############

puerto = 'COM5'
razonBaudios = 9600

arduino = realTimePlot(puerto,razonBaudios,muestrasMaximas,tamanioDatos)
arduino.readSerialStart()

################# Creación de botones e interfaz Tkinter ############

def empezar(): # Con esta función comenzamos a guardar datos de la gráfica
    arduino.startCollectData()
    estado.set('Recolectando Datos')

def pausar(): # Con esta función pausamos la recolección de datos de la gráfica
    arduino.stopCollectData()
    estado.set('Pausado')

def borrar(): # Con esta función borramos todos lo datos guardados
    arduino.deleteData()
    estado.set('Datos Borrados')

def guardar(): # Con esta función guardamos los datos obtenidos de la lectura
    arduino.saveData(Filename = entrada.get()) # Este es importante, porque le va a dar una dirección al los datos guardados.
    estado.set('Datos Guardados')

def cuando_cerrar(): # Indica qué va a pasar cuando cerremos la función
    root.quit()
    arduino.close()
    plt.close('all')
    root.destroy()


################# Captura Datos Gráfica con función callback ###############
def callback():
    arduino.readSerialStart()

    for i in range(tamanioDatos):
        fig, ax = makeFigure(limite_x[i],limite_y[i],'Datos' + str(i+1))
        lineas = ax.plot([],[],estilo[i],label = nombreEtiqueta[i])[0]
        nombreValor = ax.text(0.50,0.90,'', transform = ax.transAxes)
        datosGuardados.append(animation.FuncAnimation(fig,arduino.getSerialData, fargs= (lineas,nombreValor,nombreEtiqueta[i],i),interval = tiempoMuestreo))
        plt.legend(loc = 'upper left')
        plt.grid()

    plt.show() # Se mete esta función en Callback

#################### Creación de Interfaz y botones ################

# Interfaz Tkinter

root = Tk()
root.protocol("WM_DELETE_WINDOW", cuando_cerrar)
root.title("Colector de Datos Acelerometro en Tiempo Real")

etiqueta = Label(root, text = 'Nombre del Archivo', font = "Times 10 italic bold")
etiqueta.grid(row = 0, column = 1, padx = 20, pady = 10)

entrada = Entry(root, justify = LEFT)
entrada.insert(END, 'p1')
entrada.grid(row = 0, column = 1, padx = 20, pady = 20)

estado = StringVar(root, 'Off')
etiquetaEstado = Label(root, textvariable = estado)
etiquetaEstado.grid(row= 0,column =2, padx=10,pady=10)

# Botones Tkinter


boton1 = Button(root,text = 'Comenzar', command = empezar, bg = 'LightCyan', font = 16)
boton1.grid(row = 1, padx = 20, pady = 20)

boton2 = Button(root,text = 'Pausar', command = pausar, bg = 'LightCyan', font = 16)
boton2.grid(row = 1, column = 1, padx = 20, pady = 20)

boton3 = Button(root,text = 'Borrar', command = borrar, bg = 'LightCyan', font = 16)
boton3.grid(row = 1, column = 2, padx = 20, pady = 20)

boton4 = Button(root,text = 'Guardar', command = guardar, bg = 'LightCyan', font = 16)
boton4.grid(row = 1, column = 3, padx = 20, pady = 20)

root.after(100,callback)

root,mainloop()
