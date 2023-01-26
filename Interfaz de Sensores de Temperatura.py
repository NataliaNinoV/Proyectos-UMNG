#********FUNCIONOOOOOO****** 

import serial
import time
import collections
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


def getSerialData(self,Samples,numData,serialConnection, lines):
    for i in range(numData):
        miaw = serialConnection.readline().strip()  #Leer sensor
        miaw = float(miaw)
        data[i].append(miaw) #Guarda lectura en la última posición
        lines[i].set_data(range(Samples),data[i]) # Dibujar nueva linea

serialPort = 'COM5' # Puerto serial arduino / Arduino serial port
baudRate = 9600  # Baudios

class Index:
    def L0(self,event):
        serialConnection.write(b'1')
    def L4(self,event):
        serialConnection.write(b'4')
    def L5(self,event):
        serialConnection.write(b'5')
    def S1(self,event):
        serialConnection.write(b'6')
    def S2(self,event):
        serialConnection.write(b'7')
    def S3(self,event):
        serialConnection.write(b'8')
    def Stres(self, event):
        serialConnection.write(b'9')

try:
  serialConnection = serial.Serial(serialPort, baudRate) # Instanciar objeto Serial / Instance Serial Object
except:
  print('Cannot conect to the port')

Samples = 50  #Muestras
sampleTime = 150  #Tiempo de muestreo
numData = 3
print(0)

# Limites de los ejes
xmin = 0
xmax = Samples
ymin = [0, 0 , 0 ,0]
ymax = [50, 50 , 50 , 50]
lines = []
data = []

for i in range(numData):
    data.append(collections.deque([0] * Samples, maxlen=Samples))
    lines.append(Line2D([], [], color='orange'))
  
fig = plt.figure(figsize=(12,6))# Crea una nueva figura #Create a new figure.

ax2 = fig.add_subplot(2, 3, 1,xlim=(xmin, xmax), ylim=(ymin[1] , ymax[1]))
ax2.set_xlabel("Tiempo [s]")
ax2.set_ylabel("Temperatura [°C]")
ax2.add_line(lines[0])

ax3 = fig.add_subplot(2, 3, 2 ,xlim=(xmin, xmax), ylim=(ymin[2] , ymax[2]))
ax3.set_xlabel("Tiempo [s]")
ax3.set_ylabel("Temperatura [°C]")
ax3.add_line(lines[1])

ax4 = fig.add_subplot(2, 3, 3,xlim=(xmin, xmax), ylim=(ymin[3] , ymax[3]))
ax4.set_xlabel("Tiempo [s]")
ax4.set_ylabel("Temperatura  [°C]")
ax4.add_line(lines[2])

#***********Boton***********
 opcionLeds=Index()

plt.subplots_adjust(bottom=0.3)

Sensor1 = plt.axes([0.175,0.4,0.125,0.075])
B1 = Button(Sensor1, 'Sensor#1')
B1.on_clicked(opcionLeds.S1)

Sensor2 = plt.axes([0.450,0.4,0.125,0.075])
B2 = Button(Sensor2, 'Sensor#2')
B2.on_clicked(opcionLeds.S2)

Sensor3 = plt.axes([0.725,0.4,0.125,0.075])
B3 = Button(Sensor3, 'Sensor#3')
B3.on_clicked(opcionLeds.S3)

LosTres = plt.axes([0.7,0.02,0.225,0.075])
LosTres = Button(LosTres, 'Los Tres Sensores')
LosTres.on_clicked(opcionLeds.Stres)

##LEDS
LED0 = plt.axes([0.2,0.05,0.1,0.075])
B0 = Button(LED0, 'LED#0')
B0.on_clicked(opcionLeds.L0)

LED4 = plt.axes([0.2,0.15,0.1,0.075])
B4 = Button(LED4, 'LED#4')
B4.on_clicked(opcionLeds.L4)

LED5 = plt.axes([0.2,0.25,0.1,0.075])
B5 = Button(LED5, 'LED#5')
B5.on_clicked(opcionLeds.L5)

anim = animation.FuncAnimation(fig,getSerialData, fargs=(Samples,numData,serialConnection,lines), interval=sampleTime)
plt.show()#mostrar el grafico
serialConnection.close() # cerrar puerto serial/ close serial port

