import tkinter as tk
from tkinter import ttk
import logging
import requests

from messaging import ActuatorState
import common


def refresh_btn_cmd():
    #laget av vegard
    #denne metoden kalles når brukeren trykker på refresh knappen
    pass

#Denne styrerer on/off toggle knapp lightbulb
#Denne metoden må vi gjøre ferdig

def lightbulb_cmd(state, did):

    # Ny tilstand frå GUI
    new_state = state.get()

    # Henter tilstand fra skytjeneste
    uuid = common.LIGHTBULB_DID
    Geturl = f"http://127.0.0.1:8000/smarthouse/actuator/{uuid}/current"
    Puturl = f"http://127.0.0.1:8000/smarthouse/actuator/{uuid}"
    response = requests.get(Geturl)

    # Går gjennom respons og gjer den om til ei ordliste
    data = response.json()

    # Henter ut verdiar som ligg i ordlista med nøkkelen 'state'
    sensor_value = str(data['state'])

    print(data)
    print(sensor_value)

    # Logikk før og skru va og på lys pæra. Put in commando her!
    if sensor_value == "off" and new_state == "On":
        print("No må denna sensoren gå PÅ for pokkeren")
        # Make the PUT request to update the state
        new_data = {"state": "off"}
        Cmd_To_Actuator = requests.put(Puturl, json=new_data)
        
        print(Cmd_To_Actuator.status_code, Cmd_To_Actuator.text)
    
    if sensor_value == "on" and new_state == "Off":
        print("Skrudd av, kjøh")
        print("No må denna sensoren gå PÅ for pokkeren")
        # Make the PUT request to update the state
        Cmd_To_Actuator = requests.put(Puturl, json=new_state)
        print(Cmd_To_Actuator.status_code, Cmd_To_Actuator.text)

    logging.info(f"Dashboard: {new_state}")

    # TODO: START
    # send HTTP request with new actuator state to cloud service
    # Sender den nye tilstand til skytenesten

    # TODO: END


def init_lightbulb(container, did):

    lb_lf = ttk.LabelFrame(container, text=f'LightBulb [{did}]')
    lb_lf.grid(column=0, row=0, padx=20, pady=20, sticky=tk.W)

    # variable used to keep track of lightbulb state
    lightbulb_state_var = tk.StringVar(None, 'Off')

    on_radio = ttk.Radiobutton(lb_lf, text='On', value='On',
                               variable=lightbulb_state_var,
                               command=lambda: lightbulb_cmd(lightbulb_state_var, did))

    on_radio.grid(column=0, row=0, ipadx=10, ipady=10)

    off_radio = ttk.Radiobutton(lb_lf, text='Off', value='Off',
                                variable=lightbulb_state_var,
                                command=lambda: lightbulb_cmd(lightbulb_state_var, did))

    off_radio.grid(column=1, row=0, ipadx=10, ipady=10)
