import logging
import threading
import time
import requests
import threading
from threading import Thread

from messaging import ActuatorState
import common


class Actuator:

    def __init__(self, did):
        self.did = did
        self.state = ActuatorState('False')
        self.lock = threading.Lock() #Oppretter en lås.

    def simulator(self):

        logging.info(f"Actuator {self.did} starting")

        while True:

            logging.info(f"Actuator {self.did}: {self.state.state}")

            time.sleep(common.LIGHTBULB_SIMULATOR_SLEEP_TIME)

    def client(self):

        logging.info(f"Actuator Client {self.did} starting")

        # TODO: START
        #Skal intragere med skytenesten
        
        #Starter tråd for simulator og client.
        logging.info("Starter tempsensor_simulator thread")        
        tempsensor_thread_simulator = Thread(target=self.simulator)   

        logging.info("Starter tempsensor_client thread")        
        tempsensor_thread_client = Thread(target=self.client)     
        
        tempsensor_thread_simulator.start()        
        tempsensor_thread_client.start()

        # send request to cloud service with regular intervals and
        # set state of actuator according to the received response

        logging.info(f"Client {self.did} finishing")

        # TODO: END

    def run(self):

        pass
        # TODO: START

        # start thread simulating physical light bulb

        # start thread receiving state from the cloud

        # TODO: END


