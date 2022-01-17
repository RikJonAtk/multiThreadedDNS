import socket
import datetime

def resolveDns():
    filename = "hostnames.txt"

    with open(filename) as file:
        hostnames = file.readlines()
        hostnames = [line.rstrip() for line in hostnames]

    start = datetime.datetime.now()

    for host in hostnames:
        try:
            print(f"{host}: {socket.gethostbyname(host)}")
        except Exception as e:
            print(f"{host}: {e}")
            continue

    end = datetime.datetime.now()
    duration = end - start
    print(" ")
    print(f"Time taken: {duration}")
    print("")

if __name__ == "__main__":
    resolveDns()
