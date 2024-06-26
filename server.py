import socket
import os
import threading


HEADER = 64
PORT = 5050
SERVER = input("enter server ip adress : ")
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MSG = "disconnected!"

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn,addr):
    print(f"new connection, {addr} connected.")
    connected = True
    while connected :
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length: 
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == "GET / HTTP/1.1":
                with open("index.html", "r") as file:
                    response = file.read()
                conn.send(response.encode(FORMAT))
            elif msg == DISCONNECT_MSG:
                connected = False
            print(f"{addr} - {msg}")             
    conn.close()

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"active connections : {threading.active_count() -1}")
print(f"starting server at {ADDR}")