import logging
import threading
import time
import requests
from threading import Thread

from messaging import ActuatorState
import common


class Actuator:

    def __init__(self, did):
        self.did = did
        self.state = ActuatorState('False')
        self.lock = threading.Lock()

    def simulator(self):

        logging.info(f"Actuator {self.did} starting")

        while True:
            self.lock.acquire() #Låser koden
            logging.info(f"Actuator {self.did}: {self.state.state}")
            self.lock.release() #Låser opp koden   
            time.sleep(common.LIGHTBULB_SIMULATOR_SLEEP_TIME)

    def client(self):

        while True:
            self.lock.acquire() #Låser koden
            logging.info(f"Actuator Client {self.did} starting") # Logg tekst til terminal
            
            # Url til smarthouse, der ein finn aktuell actuator state
            Geturl = f"http://127.0.0.1:8000/smarthouse/actuator/{self.did}/current"
            
            # Responsen ein får frå webserveren
            response = requests.get(Geturl)

            # Går gjennom respons og gjer den om til ei ordliste
            data = response.json()

            # Henter ut verdiar som ligg i ordlista med nøkkelen 'state'
            sensor_value = str(data['state'])
            
            # Oppdaterer staten, slik at client metoden kan hente den siste oppdaterete aktuator status
            self.state = ActuatorState(sensor_value)
            print(f"New State Value: {self.state.state}")

            logging.info(f"Client {self.did} finishing")
            
            time.sleep(common.LIGHTBULB_CLIENT_SLEEP_TIME) # Sovetid for tråden.
            self.lock.release() #Låser opp koden   

    def run(self):

        pass
        # TODO: START

        # start thread simulating physical light bulb
        #Starter tråd for simulator og client.
        logging.info("Starter tempsensor_simulator thread")        
        lightbulb_thread_simulator = Thread(target=self.simulator)   

        logging.info("Starter tempsensor_client thread")        
        lightbulb_thread_client = Thread(target=self.client)     
        
        lightbulb_thread_simulator.start()        
        lightbulb_thread_client.start()
        # start thread receiving state from the cloud

        # TODO: END


