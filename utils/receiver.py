from socket import socket, AF_INET, SOCK_STREAM
from .essential import Essential
from os import path, mkdir
from platform import system
import time

class ParcelReceiver(Essential):
    def connect_to_sender(self):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((self.host, self.port))
        self.receive(sock)
        sock.close()

    def file_details(self, filename, filesize):
        return super().file_details(filename, filesize)

    def createparcelfolder(self, folder_name: str):
        return super().createparcelfolder(folder_name)

    def receive(self, sock):
        receive_data:bytes  = sock.recv(1024)
        filename, filesizeinstr = receive_data.decode().split("|")
        slash:str="/" if "/" in filename else "\\"
        filename = filename.split(slash)[-1]
        filesize = int(filesizeinstr)
        print(self.file_details(filename, filesize))
        with open(f"{self.check_exist(self.createparcelfolder('Parcel'), filename)}", "wb+") as wfile:
            byte_received = 0
            while byte_received < filesize:
                chunk = sock.recv(1024*64)
                if not chunk:
                    break
                wfile.write(chunk)
                byte_received+=len(chunk)
                progress=(byte_received/filesize)*100
                print(f"\rReceiving: {progress:.2f}%", end="", flush=True)
        wfile.close()
        sock.close()
        com_text="🛬 Parcel Received: 📦"
        print("\n")
        for _ in range(len(com_text)):
            print(f"\r{com_text[:_+1]}", flush=True, end="")
            time.sleep(.050)
        print()

    def start_receive(self, host:str, port:int):
        self.host, self.port = host, port
        try:
            self.connect_to_sender()
        except ConnectionRefusedError:
            print("Invalid Port Number!")

    def check_exist(self, parcel_path: str, filename: str):
        slash = "/" if not system().lower() == "windows" else "\\"
        if not path.exists(parcel_path):
            mkdir(parcel_path)
            return parcel_path+slash+filename
        return parcel_path+slash+filename
