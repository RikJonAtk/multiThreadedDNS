import threading
import socket
import datetime

def resolveDns(hostnames):
    
    for host in hostnames:
        try:
            print(f"{host}: {socket.gethostbyname(host)}")
        except Exception as e:
            print(f"{host}: {e}")
            continue

if __name__ == "__main__":

    filename = "hostnames.txt"

    with open(filename) as file:
        hostnames = file.readlines()
        hostnames = [line.rstrip() for line in hostnames]

    start = datetime.datetime.now()
    
    threads = list()

    chunksize = 100

    chunks = [hostnames[i:i + chunksize] for i in range(0, len(hostnames), chunksize)]
    for chunk in chunks:
        x = threading.Thread(target=resolveDns, args=(chunk,))
        threads.append(x)
        x.start()

    for chunk, thread in enumerate(threads):
        thread.join()

    end = datetime.datetime.now()
    duration = end - start
    print(" ")
    print(f"Time taken: {duration}")
    print("")
