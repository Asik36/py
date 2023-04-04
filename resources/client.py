import socket
import threading 
from time import sleep

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.194"
ADDR = (SERVER, PORT)
USERNAME = "Asik"


USERNAME = "Asik"

global connected

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def recv():
    global connected
    connected = True

    while connected:
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = client.recv(msg_length).decode(FORMAT)
            if msg[0] == 'p':
                msg = msg[1:]
                msg = msg.split(" ", 1)

            
            if msg == DISCONNECT_MESSAGE:
                connected = False
                
            
            print(f"[SERVER] {msg}")
            return msg

    client.close()



def connect_server():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while client.connect_ex(ADDR) != 0:
        print('connecting...')
        sleep(10)

    print("Connected!")

    send(USERNAME)

    thread = threading.Thread(target=recv)
    thread.start()



