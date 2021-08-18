import os
from tkinter import *
import serial
import matplotlib.pyplot as plt
import time


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
    '''
    Este boton lo deje aqui por si acaso se necesite, si no lo necesitas
    borralo no mas 
    '''
    #Button(Frame1, text="Datos Del Sensor",width="17",
    #       font=("Times New Roman", 14),command = "").place(x=500,y=300)
    
    VentanaPrinc.mainloop()

def Arduino():

    #Codigo Arduino
    #Para Leer la entrada Analogica
    #y enviarla al serial o USB

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

    arduino = serial.Serial('COM6', 9600, timeout=0)
    point = 0
    fig, ax = plt.subplots()
    plt.ion()

    maxlen = 20
    x = []
    y = []

    while True:
        data = arduino.readline().decode().strip()
        time.sleep(0.2)
        if data:
            data = int(data)
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
'''
Estos son como un exito y error del encio de datos
Como para ponerlos dentro de un try y un catch
'''
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

'''
Con estos tengo problemo, no me funciona el destroy me sale
AttributeError: 'function' object has no attribute 'destroy'
'''

def send_to_sever(data: dict):
    try:
        req = requests.post(url = "http://0.0.0.0:/new_feature", json = data)
    except Exception as e:
        print(str(e))


def exito_CerrarED():
    exito_DatE.destroy()
def exito_CerrarFD():
    exito_DatF.destroy()

VentanaPrinc()


