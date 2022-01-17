#
# Credit to:
# Troy Fawkes for his primer on using queues with Multithreading
# > https://www.troyfawkes.com/learn-python-multithreading-queues-basics/
#
# The Python3 queue documentation
# > https://docs.python.org/3/library/queue.html#queue.Empty
#

import threading
import socket
import datetime
from queue import Queue

def resolveDns(hostnames,lookupFail,lookupSuccess):
    for host in hostnames:
        try:            
            lookupSuccess.put(f"{host},{socket.gethostbyname(host)}")        
        except Exception as e:
            lookupFail.put(f"{host}, {e}")


if __name__ == "__main__":

    lookupFail = Queue(maxsize=0)
    lookupSuccess = Queue(maxsize=0)

    filename = "bigHostnames.txt"

    with open(filename) as file:
        hostnames = file.readlines()
        hostnames = [line.rstrip() for line in hostnames]

    start = datetime.datetime.now()
    
    threads = list()

    chunksize = 250
    
    chunks = [hostnames[i:i + chunksize] for i in range(0, len(hostnames), chunksize)]

    for chunk in chunks:
        x = threading.Thread(target=resolveDns, args=(chunk,lookupFail,lookupSuccess))
        threads.append(x)
        x.start()

    for chunk, thread in enumerate(threads):
        thread.join()

    end = datetime.datetime.now()
    duration = end - start
    totalFails = lookupFail.qsize()
    totalSuccesses = lookupSuccess.qsize()

    failures = [lookupFail.get() for i in range(lookupFail.qsize())]
    print("Failures:")
    for fail in failures:
        print(fail)
    print(" ")

    successes = [lookupSuccess.get() for i in range(lookupSuccess.qsize())]
    print("Successes:")
    for success in successes:
        print(success)

    print(" ")
    print(f"Time taken: {duration}")
    print(f"Successfully resolved: {totalSuccesses}")
    print(f"DNS Resolution errors: {totalFails}")
    print(" ")
