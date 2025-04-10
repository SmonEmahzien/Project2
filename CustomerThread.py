import threading

import queue





openbank = threading.Event()
semdoor = threading.Semaphore(2)
readytel = threading.Semaphore(0)
safe = threading.Semaphore(2)
accessMan = threading.Semaphore(1)
numtell = 3
numcust = 50
teller_states = ['not ready'] * numtell
custqueue = queue.Queue()
qulock = threading.Lock()


