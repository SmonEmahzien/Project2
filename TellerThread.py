
import threading
import time
import random
import queue



numtell = 3
numcust = 50

custqueue = queue.Queue()
qulock = threading.Lock()
tellstates = ['notready'] * numtell

semmanager = threading.Semaphore(1)

semdoor = threading.Semaphore(2)
semsafe = threading.Semaphore(2)

readytel = threading.Semaphore(0)
openthebank = threading.Event()




def teller_thread(tellid):
    tellstates[tellid] = 'ready'
    readytel.release()
    print(f"Teller {tellid} [Teller {tellid}]: ready ")
    while True:
        customer = custqueue.get()
        if customer is None:
            break
        with qulock:
            tellstates[tellid] = 'busy'
        print(f"Teller {tellid} [Customer {customer['id']}]: asks ")
        customer['condition'].wait()
        customer['condition'].acquire()
        customer['condition'].notify()
        customer['condition'].wait()
        customer['condition'].release()
        print(f"Teller {tellid} [Teller {tellid}]: ready to serve again")
        with qulock:
            tellstates[tellid] = 'ready'
        tellready.release()
        customer['condition'].acquire()
        customer['condition'].notify()
        transaction = customer['transaction']
        customer['condition'].release()
        if transaction == 'withdraw':
            print(f"Teller {tellid} [Teller {tellid}]:  manager")
            with semmanager:
                print(f"Teller {tellid} [Teller {tellid}]: interact with manager")
                print(f"Teller {tellid} [Teller {tellid}]: done ")
                time.sleep(random.uniform(0.005, 0.03))

        print(f"Teller {tellid} [Teller {tellid}]:  to safe")
        with semsafe:
            time.sleep(random.uniform(0.01, 0.05))
            print(f"Teller {tellid} [Teller {tellid}]: using safe")
            print(f"Teller {tellid} [Teller {tellid}]: done with safe")




