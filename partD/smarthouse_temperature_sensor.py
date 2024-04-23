import logging
import threading
import time
import math
import requests
from datetime import datetime

from messaging import SensorMeasurement
import common



class Sensor:

    def __init__(self, did):
        self.did = did
        self.measurement = SensorMeasurement('0.0')
        self.lock = threading.Lock()


    def simulator(self):

        logging.info(f"Sensor {self.did} starting")

        while True:

            temp = round(math.sin(time.time() / 10) * common.TEMP_RANGE, 1)

            logging.info(f"Sensor {self.did}: {temp}")
            self.measurement.set_temperature(str(temp))

            time.sleep(common.TEMPERATURE_SENSOR_SIMULATOR_SLEEP_TIME)

    def client(self):

        logging.info(f"Sensor Client {self.did} starting")
       
        while True:
            
            # Url der sensor verdi skal oppdaterast
            PostUrl = f"http://127.0.0.1:8000/smarthouse/sensor/{self.did}/current"

            timestamp = datetime.now().isoformat() # Leser av aktuell tid
            value = self.measurement.get_temperature()  # Genererer ein temeratur
            unit = "C" # Oppdaterer unit
            
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

        pass
        # TODO: START

        # create and start thread simulating physical temperature sensor

        # Lage løkke som simulerer temperatursensoren og        
        # Lage løkke som kontinuerlig oppdaterer temperaturen til skytenesten.
        logging.info("Starter tempsensor_simulator thread")
        tempsensor_thread_simulator = threading.Thread(target=self.simulator)

        logging.info("Starter tempsensor_client thread")
        tempsensor_thread_client = threading.Thread(target=self.client)

        tempsensor_thread_simulator.start()
        tempsensor_thread_client.start()
        

        # TODO: END

