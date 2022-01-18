#!/usr/bin/env python3 
import socket
import sys
from termcolor import cprint

from common import calc_sha1_sum


host = '127.0.0.1'
port = 50001

BUFFER = 1024
SEPARATOR = "<SEPARATOR>"

args = sys.argv[1:]

if len(args) == 0:
    cprint("File name not provided as script argument.", 'red')
    sys.exit()

file_name = args[0]

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

cprint(f"Sending file name {file_name} to the server", "green")
client_socket.send(f"{file_name}{SEPARATOR}".encode())

with open(file_name, "rb") as f:
    while True:
        data = f.read(BUFFER)
        if not data:
            break
        print("Sending...")
        client_socket.send(data)

cprint("File sending completed", "green")
client_socket.shutdown(socket.SOCK_STREAM)

print("Received checksum from server....")
sha_from_server = client_socket.recv(BUFFER).decode("utf-8")

print("Checking checksum match....")

if sha_from_server == calc_sha1_sum(file_name):
    cprint("SHA1 checksum matches. OK!", "green")
else:
    cprint("Error checksum doesn't match.", "red")

