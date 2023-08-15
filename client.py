#from tkinter import *
#from tkinter import ttk
import socket
import threading
import pyaudio
global port
global zaman
import time
import sys

# nickname = input("choose")

class Client:
    def __init__(self):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.life = 3

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while 1:
            try:


                self.target_ip = '192.168.1.36'

                self.target_port = 9393
                self.s.connect((self.target_ip, self.target_port))
                self.nickname = input("Nickname:")
                self.ip_of_client = socket.gethostbyname(socket.gethostname())
                self.s.send(f"nickname:{self.nickname}\nClient ip:{self.ip_of_client}\njoined at".encode('utf-8'))

                self.target_port2 = 9292
                self.socket.connect((self.target_ip, self.target_port2))
                self.socket.send(f"nickname:{self.nickname}\nClient ip:{self.ip_of_client}\njoined at".encode('utf-8'))
                break
            except:
                print("Couldn't connect to server")
                time.sleep(3)
                self.life = self.life -1
                if self.life == 0:
                    sys.exit(0)

        chunk_size = 206  # 512
        audio_format = pyaudio.paInt16
        channels = 1
        rate = 20000

        # initialise microphone recording
        self.p = pyaudio.PyAudio()
        self.playing_stream = self.p.open(format=audio_format, channels=channels, rate=rate, output=True,
                                          frames_per_buffer=chunk_size)
        self.recording_stream = self.p.open(format=audio_format, channels=channels, rate=rate, input=True,
                                            frames_per_buffer=chunk_size)

        print("Connected to voice Server")

        # start threads
        threading.Thread(target=self.manage).start()
        receive_thread = threading.Thread(target=self.receive_server_data).start()
        receive_thread = threading.Thread(target=self.receive_server_messages).start()

        self.send_data_to_server()


    def receive_server_data(self):

        while True:
            try:

                data = self.s.recv(1024)
                self.playing_stream.write(data)
            except:
                pass

    def send_data_to_server(self):

        while True:
            try:


                data = self.recording_stream.read(1024)
                self.s.sendall(data)
            except:
                self.s.close()
                time.sleep(3)
                print("Connection lost. Reconnecting...")
                self.life = self.life-1
                if self.life == 0:
                    self.s.close()
                    sys.exit(0)




                while True:
                    try:
                        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        self.s.connect((self.target_ip, self.target_port))
                        self.s.send(f"nickname:{self.nickname} Client ip:{self.ip_of_client} ".encode('utf-8'))
                        print("Reconnected to the server.")
                        self.s.send(f"{self.nickname}".encode('utf-8'))
                        break  # Break the reconnect loop if the connection is successful.
                    except:
                        print("Failed to reconnect. Retrying in a moment...")
                        time.sleep(5)  # Add a random delay between 1 and 5 seconds.



    def manage(self):
        while True:
            choice = input("choice:\n")
            if choice == "message":
                receiver_user = input("receiver user:")
                message = input("your message:")
                self.socket.send(f"{receiver_user} <------ '{message}' from {self.nickname}".encode('utf-8'))

            if choice == "change room":

                self.new_port = int(input("new port:"))
                self.s.close()
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((self.target_ip, self.new_port))
                self.s.send(f"nickname:{self.nickname}\nClient ip:{self.ip_of_client}\njoined at".encode('utf-8'))



    def receive_server_messages(self):
        
        while True:
            try:

                data = self.socket.recv(1024)
                print(data.decode('utf-8'))

            except:
                pass

if __name__ == '__main__':

    c = Client()
