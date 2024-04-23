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
            self.lock.acquire() #Låser koden
            logging.info(f"Actuator {self.did}: {self.state.state}")
            self.lock.release() #Låser opp koden   
            time.sleep(common.LIGHTBULB_SIMULATOR_SLEEP_TIME)

    def client(self):

        while True:
            self.lock.acquire() #Låser koden
            logging.info(f"Actuator Client {self.did} starting")

            # TODO: START
            #Skal intragere med skytenesten    
        

            logging.info(f"Client {self.did} finishing")
            self.lock.release() #Låser opp koden   
            time.sleep(common.LIGHTBULB_CLIENT_SLEEP_TIME)

            # TODO: END

    def run(self):

        pass
        # TODO: START

        # start thread simulating physical light bulb
        #Starter tråd for simulator og client.
        logging.info("Starter lightbulb_simulator thread")        
        lightbulb_thread_simulator = Thread(target=self.simulator)   

        logging.info("Starter lightbulb_client thread")        
        lightbulb_thread_client = Thread(target=self.client)     
        
        lightbulb_thread_simulator.start()        
        lightbulb_thread_client.start()
        # start thread receiving state from the cloud

        # TODO: END


