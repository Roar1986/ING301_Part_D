import tkinter as tk # https://www.pythontutorial.net/tkinter/
#Når denna filen kjører, skal gui dukke opp, bruker tkinter for å lage dette.
#Oppgava går ut på å lage en dashboard klient og en smarthous applikasjon
#Følgende skal implementeres, dashboard_lightbulb.py
#dashboard_temperatursensor.py
#Messaging.py har metoder som kan brukes for å konstruere body/payload i de request som skal sendes til skytenesten

import logging

from dashboard_lightbulb import init_lightbulb
from dashboard_temperaturesensor import init_temperature_sensor

import common

log_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")

#Grensesnitt boksen
root = tk.Tk()
root.geometry('450x300')
root.title('ING301 SmartHouse Dashboard ')

init_lightbulb(root, common.LIGHTBULB_DID)
init_temperature_sensor(root, common.TEMPERATURE_SENSOR_DID)

root.mainloop()
