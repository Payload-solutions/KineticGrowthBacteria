import os
from tkinter import *
from tkinter import messagebox
import tkinter
import serial
import matplotlib.pyplot as plt
import time
import signal
import sys


ventana_DatE = None
ventana_DatF = None


def VentanaPrinc():
    global VentanaPrinc
    VentanaPrinc=Tk()
    VentanaPrinc.title("Acceso al Sistema")
    VentanaPrinc.resizable(0,0)
    Frame1=Frame()
    Frame1.pack()
    Frame1.config(width="900", height="530", bg="lightgreen")
    #Iconos
    imagenf=PhotoImage(file="Fondo2.0.png")
    imagenesc=PhotoImage(file="logo-universidad-agraria-del-ecuador.png")
    #InserciondeIconos
    Label(Frame1, image=imagenf).place(x=1,y=1)
    Label(Frame1, image=imagenesc).place(x=120,y=180)
    #Boton
    Button(Frame1, text="Mostar Datos Del Sensor",width="19",
           font=("Times New Roman", 14),command = Arduino).place(x=500,y=230)
    
    Button(Frame1, text=" Enviar Datos a la Red ",width="19",
           font=("Times New Roman", 14),command = exito_DatE).place(x=500,y=290)

    #Button(Frame1, text="Datos Del Sensor",width="17",
    #       font=("Times New Roman", 14),command = "").place(x=500,y=300)
    
    VentanaPrinc.mainloop()

def Arduino():

    '''
    int value = 0;
    int inPin = A1;
    void setup() {
     Serial.begin(9600);
     }
     void loop() {
     value = analogRead(inPin);
     Serial.println(value);
     delay(10);
     }
    '''
    
    #Creamos la conexion
    '''
    El /dev/ttyUSB0 se refiere al puerto en el que esta
    conectado el Arduino, este es para linux ñaño, pero
    si tenes la VM puedes probar cambiando esto por 'COMx'
    donde x es el numero del puerto, el 9600 es el boudrate
    ñañon
    '''

    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
    point = 0
    fig, ax = plt.subplots()
    plt.ion()

    maxlen = 20
    x = []
    y = []

    while True:
        try:
            data = arduino.readline().decode("ascii", errors="replace").strip()
            data = data.replace("\r\n", "")
            print(data)
            # time.sleep(0.2)
            if data:
                data = float(data)
                x.append(point)
                y.append(data)
                if len(x) > maxlen:
                    x = x[1:]
                    y = y[1:]
                plt.plot(x, y, color='r')
                point += 1
                plt.pause(0.05)

                ax.clear()
                plt.ylim([0, 1023])
                plt.show()
            # time.sleep(10)
        except KeyboardInterrupt:
            # messagebox.showinfo(message="Saliendo", title="Info")
            print("[*] Saliendo")
            sys.exit(0)

def exito_DatE():
    global ventana_DatE
    ventana_DatE = Toplevel(VentanaPrinc)
    ventana_DatE.title("Exito")
    ventana_DatE.geometry("210x100")
    Label(ventana_DatE, text="Datos Enviados Con Exito", font=("Times New Roman", 14)).pack()
    Button(ventana_DatE, text="OK",font=("Times New Roman", 14), command= exito_CerrarED).place(x=90,y=50)
		

def Falla_DatF():
    global ventana_DatF
    ventana_DatF = Toplevel(VentanaPrinc)
    ventana_DatF.title("Exito")
    ventana_DatF.geometry("210x100")
    Label(ventana_DatF, text="Datos No Enviados", font=("Times New Roman", 14)).pack()
    Button(ventana_DatF, text="OK",font=("Times New Roman", 14), command= exito_CerrarED).place(x=90,y=50)


def exito_CerrarED():
    ventana_DatE.destroy()
def exito_CerrarFD():
    ventana_DatF.destroy()

VentanaPrinc()


