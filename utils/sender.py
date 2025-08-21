from socket import socket, AF_INET, SOCK_STREAM
from os import path
from platform import system
from random import randint
from .essential import Essential

pair_code: int = randint(49152,65535)

class ParcelSender(Essential):
    code = pair_code
    def waiting_for_receiver(self):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.settimeout(120)
        sock.listen(1)
        return sock

    def format_size(self, size_bytes):
        return super().format_size(size_bytes)

    def file_details(self, filename, filesize):
        return super().file_details(filename, filesize)

    def connected_to_receiver(self, file: str):
        print(f"Waiting for connection only - {self.waiting_for_receiver().timeout:.0f}'sec")
        print(f"Pairing Code: {pair_code}")
        try:
            conn, _ = self.waiting_for_receiver().accept()
            print(f"\nOK! Connected...\n")
            self.send(file, conn)
            conn.close()
        except TimeoutError:
            print(f"Timeout!. There is no receiver")

    def send(self, file: str, csoc):
        filesize = path.getsize(file)
        csoc.send(f"{file}|{filesize}".encode())
        slash = "/" if not system().lower() == "windows" else "\\"
        filename = file.split(slash)[-1]
        print(self.file_details(filename, filesize))
        with open(file, "rb+") as rfile:
            byte_send = 0
            while (chunk := rfile.read(1024*64)):
                csoc.sendall(chunk)
                byte_send+=len(chunk)
                progress=(byte_send/filesize)*100
                print(f"\rSending: {progress:.2f}%", end="", flush=True)
        rfile.close()
        csoc.close()
        print(f"\n\n📦 :Parcel Sended 🛫")

    def start_send(self, host: str, port: int, file: str):
        self.host, self.port = host, port
        self.connected_to_receiver(file)
