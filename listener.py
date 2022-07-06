import socket
import os

print("[Active Listener]")
ip = str(input("Enter IP Address: "))
port = int(input("Enter Port To Check: "))
ADDR = (ip, port)
os.system("cls")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def start():
    print("[Listener Starting]")
    server.listen()
    print(f"[Started] Listening on Port {port}")
    while True:
        pass

    
start()

