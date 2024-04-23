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
        


        # send request to cloud service with regular intervals and
        # set state of actuator according to the received response

        logging.info(f"Client {self.did} finishing")

        # TODO: END

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


