#!/usr/bin/env python3
import socket

from common import calc_sha1_sum
from termcolor import cprint

host = '127.0.0.1'
port = 50001
BUFFER = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(2)

client_socket, address = server_socket.accept()
cprint(f"Connection established from {address}", "green")
print(f"Receiving file name to be copied...")

file_name = ""
while True:
    data = client_socket.recv(1).decode("utf-8")
    file_name += data
    if file_name.endswith(".csv"):
        break

cprint(f"File name {file_name} received.", "green")

with open(f"server/{file_name}", "wb") as f:
    while True:
        data = client_socket.recv(BUFFER)
        print("Receving data")
        if not data:
            break

        f.write(data)

cprint("Done receving file", "green")
print("Calculcation sha1 checksum....")
print("Sending checksum to client....")
client_socket.send(calc_sha1_sum(f"server/{file_name}").encode("utf-8"))

client_socket.close()
server_socket.close()