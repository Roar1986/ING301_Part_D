import logging
import threading
import time
import math
import requests

from messaging import SensorMeasurement
import common



class Sensor:

    def __init__(self, did):
        self.did = did
        self.measurement = SensorMeasurement('0.0')

    def simulator(self):

        logging.info(f"Sensor {self.did} starting")

        while True:

            temp = round(math.sin(time.time() / 10) * common.TEMP_RANGE, 1)

            logging.info(f"Sensor {self.did}: {temp}")
            self.measurement.set_temperature(str(temp))

            time.sleep(common.TEMPERATURE_SENSOR_SIMULATOR_SLEEP_TIME)

    def client(self):

        logging.info(f"Sensor Client {self.did} starting")

        # TODO: START
        # send temperature to the cloud service with regular intervals

        logging.info(f"Client {self.did} finishing")

        # TODO: END

    def run(self):

        pass
        # TODO: START

        # create and start thread simulating physical temperature sensor

        # Lage løkke som simulerer temperatursensoren og        
        # Lage løkke som kontinuerlig oppdaterer temperaturen til skytenesten.
        logging.info("Starter tempsensor_simulator thread")
        tempsensor_thread_simulator = threading.Thread(target=Sensor.simulator(self))
        logging.info("Starter tempsensor_client thread")
        tempsensor_thread_client = threading.Thread(target=Sensor.client(self))
        tempsensor_thread_simulator.start()
        
        # create and start thread sending temperature to the cloud service

        # TODO: END

