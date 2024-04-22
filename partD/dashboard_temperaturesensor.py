import tkinter as tk
from tkinter import ttk

import logging
import requests
import json

from messaging import SensorMeasurement
import common

import requests

def refresh_btn_cmd(temp_widget, did):
    #Denne metoden skal vi utføre
    
    logging.info("Temperature refresh")    
    
    uuid = common.TEMPERATURE_SENSOR_DID
    url = f"http://127.0.0.1:8000/smarthouse/sensor/{uuid}/current"

    # Henter data basert på url og sensor ID
    response = requests.get(url)
    # Går gjennom respons og gjer den om til ei ordliste
    data = response.json()

    # Henter ut verdiar som ligg i ordlista med nøkkelen 'value'
    sensor_value = str(data['value'])

    # replace statement below with measurement from response
    # sensor_measurement = SensorMeasurement(init_value="-69")
    # oppdaterer sensor måling, ved bruk av classen SensorMeasurment
    sensor_measurement = SensorMeasurement(init_value=sensor_value)

    # update the text field in the user interface
    temp_widget['state'] = 'normal' # to allow text to be changed
    temp_widget.delete(1.0, 'end')
    temp_widget.insert(1.0, sensor_measurement.value)
    temp_widget['state'] = 'disabled'


def init_temperature_sensor(container, did):

    ts_lf = ttk.LabelFrame(container, text=f'Temperature sensor [{did}]')

    ts_lf.grid(column=0, row=1, padx=20, pady=20, sticky=tk.W)

    temp = tk.Text(ts_lf, height=1, width=10)
    temp.insert(1.0, 'None')
    temp['state'] = 'disabled'

    temp.grid(column=0, row=0, padx=20, pady=20)

    refresh_button = ttk.Button(ts_lf, text='Refresh',
                                command=lambda: refresh_btn_cmd(temp, did))

    refresh_button.grid(column=1, row=0, padx=20, pady=20)
