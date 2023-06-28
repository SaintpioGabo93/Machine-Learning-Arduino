from pyArduinoPlot import *
from tkinter import *

maxSample = 100
sampleTime = 100  # Tiempo de muestreo 100ms
sizeData = 3
legendLabel = ['ax', 'ay', 'az']
xLimit = [(0, maxSample)] * sizeData
yLimit = [(-20, 20), (-20, 20), (-20, 20)]
style = ['r-', 'g-', 'b-']
anim = []

port = 'COM5'
baudRate = 9600
arduino = realTimePlot(port, baudRate, maxSample, sizeData)


def start():
    arduino.startCollectData()
    state.set("Recolectando datos")


def pause():
    arduino.stopCollectData()
    state.set("Pausa")


def delete():
    arduino.deleteData()
    state.set("Datos borrados")


def save():
    arduino.saveData(Filename=entry.get())
    state.set("Datos guardados")


def on_closing():
    root.quit()  # finaliza este programa
    arduino.close()
    plt.close('all')
    root.destroy()  # Cierra la ventana creada


def callback():
    arduino.readSerialStart()

    for i in range(sizeData):
        fig, ax = makeFigure(xLimit[i], yLimit[i], 'Data' + str(i + 1))
        lines = ax.plot([], [], style[i], label=legendLabel[i])[0]
        legendValue = ax.text(0.50, 0.90, '', transform=ax.transAxes)
        anim.append(animation.FuncAnimation(fig, arduino.getSerialData, fargs=(lines, legendValue, legendLabel[i], i),
                                            interval=sampleTime))  # fargs has to be a tuple
        plt.legend(loc="upper left")
        plt.grid()

    plt.show()


root = Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title("RealTimeCollectData")  # titulo de la ventana

label = Label(root, text='Filename', font="Times 16 italic bold")
label.grid(row=0, padx=20, pady=20)

entry = Entry(root, justify=LEFT)
entry.insert(END, 'p1')
entry.grid(row=0, column=1, padx=20, pady=20)

state = StringVar(root, "Off")
labelState = Label(root, textvariable=state)
labelState.grid(row=0, column=2, padx=10, pady=10)

button1 = Button(root, text="Start", command=start, bg="LightCyan", font=16)
button1.grid(row=1, padx=20, pady=20)

button2 = Button(root, text="Pause", command=pause, bg="LightCyan", font=16)
button2.grid(row=1, column=1, padx=20, pady=20)

button3 = Button(root, text="Delete", command=delete, bg="LightCyan", font=16)
button3.grid(row=1, column=2, padx=20, pady=20)

button4 = Button(root, text="Save", command=save, bg="LightCyan", font=16)
button4.grid(row=1, column=3, padx=20, pady=20)

root.after(100, callback)  # Es un método definido para todos los widgets tkinter.

root.mainloop()
