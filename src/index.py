from worker import *
import time


def run():
    try:
        while True:
            time.sleep(5) # Tempo de sleep ainda a definir
            worker()
    except:
        print("Saiu do loop")

run()