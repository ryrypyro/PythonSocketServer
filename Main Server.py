# connect multiple clients to a server using python 3 sockets.
# ipv4 devices connect to router. Router communicates with modem, requests info for info, info comes, sends to router, router sends to clients.
# modem reptsents public IP address, physical location on the world.
# LOCAL IP Address --> IPV4.. Your exact devices address, how router commicates with your device, hence giving WiFi.
# ping router --> pings modem --> ping internet --> giving back to modem --> giving back to router --> back to you.

import socket
import threading

BYTES = 64
PORTNUM = 4001
# SERVER = "ipv4 of device" .. OR
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
ADDR = (SERVER, PORTNUM)
DISCON = "!DISCONNECT"

serverr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverr.bind(ADDR)  # bound socket + address.


def handler_connect(conn, addr):
    print(f"[new connection made!] {addr} has connected to the server.")


    conn = True
while connected: 
    message_length = conn.recv(BYTES).decode(FORMAT)
    message_length = int(message_length)
    message = conn.recv(message_length).decode(FORMAT)
if message == DISCON: 
    connected = False 
    

print(f"[{addr}] {message}")

conn.close()
 
def start():
    serverr.listen()
    print(f"[~~LISTENING~~] Server is connected on {SERVER}")
    while True:
        # waits for a new connection. If occurs, address and port is stored.
        conn, addr = serverr.accept()
        thread = threading.Thread(target=handler_connect, args=(conn, addr))
        thread.start()
        print(f"[NUMBER OF ACTIVE CLIENTS:] {threading.activeCount() - 1}")

        print("[BOOTING UP..] server is booting up.")
    start()
