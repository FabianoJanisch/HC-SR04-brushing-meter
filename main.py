from pymata4 import pymata4
import time
from tkinter import *

contM = 0
contT = 0
contN = 0
sing = 'ção'
pluralM = 'ção'
pluralT = 'ção'
pluralN = 'ção'
root = Tk()
root.title('HC-SR04 Distance')
root.geometry("400x400")


board = pymata4.Pymata4()
trigger_pin = 11
echo_pin = 12


def the_callback(data):
    global contM, contT, contN, pluralM, pluralT, pluralN, sing
    my_label.config(text=(data[2]))
    
    if data[2] > 60:
        localtimeT = time.ctime().split()[3]
        localtime = localtimeT[:5]
        localhora.config(text=(f"Retirado do local: {localtime}"))
        if int(localtime[0:2]) >= 6 and int(localtime[0:2]) < 12:
            contM +=1
            pluralM = 'ções'
        elif int(localtime[0:2]) >= 12 and int(localtime[0:2]) < 20:
            contT +=1
            if pluralT > 1: 
                pluralT = 'ções'
        elif int(localtime[0:2]) >= 20 or int(localtime[0:2]) < 6:
            contN +=1
            if contN > 1:
                pluralN = 'ções'    

    escov.config(text=(f'Escova{pluralM} manhã: {contM} vezes\n Escova{pluralT} período tarde: {contT} vezes\nEscova{pluralN} período noite: {contN} vezes'))


my_label = Label(root, text="", font=("Helvetica", 18))
my_label.pack(pady=10)


localhora = Label(root, text=(f"Retirado do local:"), font=("Helvetica", 18))
localhora.pack(pady=30) 

escov = Label(root, text=(f'Escova{sing} manhã: {contM} vez\n Escova{sing} período tarde: {contT} vez\nEscova{sing} período noite: {contN} vezes'), font=("Helvetica", 18))
escov.pack(pady=30)

board.set_pin_mode_sonar(trigger_pin, echo_pin, the_callback)

root.mainloop()

while True:
    try:
        time.sleep(1)
        board.sonar_read(trigger_pin)
    except Exception:
        board.shutdown

