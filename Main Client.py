import socket

BYTES = 64
PORTNUM = 4001
# SERVER = "ipv4 of device" .. OR
FORMAT = 'utf-8'
SERVER = "192.168.1.166"
DISCON = "!DISCONNECT"
ADDR = (SERVER, PORTNUM)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(message): 
    message = message.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("hello world.")

send(DISCON)
