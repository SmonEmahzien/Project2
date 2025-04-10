
if __name__ == "__main__":
    import threading, time, random
    from queue import Queue
    numtell = 3
    numcust = 50
    semdoor = threading.Semaphore(2)
    readytel = threading.Semaphore(0)

    semsafe = threading.Semaphore(2)

    semmanager = threading.Semaphore(1)
    openbank = threading.Event()
    tell = []
    for i in range(numtell):
        t = threading.Thread(target=TellerThread, args=(i,))
        t.start()
        tell.append(t)
    queue_lock = threading.Lock()
    customer_queue = Queue()

    teller_states = ['waiting'] * numtell
    cust = []
    for i in range(numcust):
        c = threading.Thread(target=CustomerThread, args=(i,))
        c.start()
        cust.append(c)
    time.sleep(0.1)
    openbank.set()
    print("open")
    for _ in range(numtell):
        customer_queue.put(None)
    for c in cust:
        c.join()
    for t in tell:
        t.join()
    print("closed")
