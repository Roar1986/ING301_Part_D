import logging
import threading
import time
import math
import requests
from datetime import datetime
from threading import Thread


from messaging import SensorMeasurement
import common



class Sensor:

    def __init__(self, did):
        self.did = did
        self.measurement = SensorMeasurement('0.0')
        self.lock = threading.Lock() #Oppretter en lås.

    def simulator(self):

        logging.info(f"Sensor {self.did} starting")

        while True:
            #Bruker lock over koden for å forhindre at den kjører samtidig som client
            self.lock.acquire() #Låser koden
            temp = round(math.sin(time.time() / 10) * common.TEMP_RANGE, 1)
            logging.info(f"Sensor {self.did}: {temp}")
            self.measurement.set_temperature(str(temp))
            self.lock.release() #Låser opp koden           
            time.sleep(common.TEMPERATURE_SENSOR_SIMULATOR_SLEEP_TIME)

    def client(self):

        logging.info(f"Sensor Client {self.did} starting")
       
        while True:
            
            # Url der sensor verdi skal oppdaterast
            PostUrl = f"http://127.0.0.1:8000/smarthouse/sensor/{self.did}/current"

            timestamp = datetime.now().isoformat() # Leser av aktuell tid
            value = self.measurement.get_temperature()  # Genererer ein temeratur
            unit = "%" # Oppdaterer unit
            
            # Dataformat til post
            data = {
            "timestamp": timestamp,
            "value": value,
            "unit": unit
            }

            # Sender request til webserver
            UpdateTemp = requests.post(PostUrl, json=data)

            print(f"HTTP Status code: {UpdateTemp.status_code}\n Repsons Body : {UpdateTemp.text}")
            
            time.sleep(common.TEMPERATURE_SENSOR_SIMULATOR_SLEEP_TIME)
            
            logging.info(f"Client {self.did} finishing")

    def run(self):
        # create and start thread simulating physical temperature sensor 
        #Starter tråd for simulator og client.
        logging.info("Starter tempsensor_simulator thread")
        tempsensor_thread_simulator = threading.Thread(target=self.simulator)
        tempsensor_thread_simulator = Thread(target=self.simulator)   

        logging.info("Starter tempsensor_client thread")
        tempsensor_thread_client = threading.Thread(target=self.client)
        tempsensor_thread_client = Thread(target=self.client)     
        
        tempsensor_thread_simulator.start()
        tempsensor_thread_client.start()
        tempsensor_thread_client.start()
        # create and start thread sending temperature to the cloud service
        
        # TODO: END

