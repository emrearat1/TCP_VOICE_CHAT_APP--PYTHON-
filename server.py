#!/usr/bin/python3

import socket
import threading
import time


# main voice chat server
class Server:
    def __init__(self):
        self.nicknames = []
        self.kicks = []
        self.muteds = []
        #method to get local ip adress of computer we use
        self.ip = socket.gethostbyname(socket.gethostname())

        while 1:

            try:
                # self.port = int(input('port no:'))
                #We should stay away from  1-1024 ports. These are used for common apps.
                self.port = 9393
                #it is about protocol. second paramater is about protocols. socket.SOCK_STREAM is used for TCP.
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #It ıs function to bind the server. we bind the server to local ip and with port. And we connected with these ip and port with clients.
                self.s.bind((self.ip, self.port))


                break
            except:
                print("cant connect the port")
        print("server1-voice server")
        print('IP:' + self.ip)
        print('port:' + str(self.port))
        print("------------------------------")



        threading.Thread(target=self.manage).start()
        self.connections = []
        self.accept_connections()


    def accept_connections(self):
        self.s.listen(100)



        while True:

            c, addr = self.s.accept()
            self.connections.append(c)

            a =c.recv(1024)
            b = a.decode('utf-8')

            c_separated1 = str(b).split(" ")

            c_separated2 = c_separated1[0].split("\n")[0]

            if c_separated2[9:] in self.kicks:
                c.close()
                continue

            self.nicknames.append(c_separated2[9:])
            zaman = time.strftime("%d:%m:%Y %H:%M:%S")
            print("----------------------------")
            print(f"{a.decode('utf-8')} {zaman}")

            print("----------------------------")


            # threading.Thread(target=self.manage).start()
            threading.Thread(target=self.handle_client, args=(c, addr)).start()




    def broadcast(self, sock, data):
        for client in self.connections:
            if client != self.s and client != sock:
                try:
                    client.send(data)
                except:
                    pass

    def handle_client(self, c, addr):
        while 1:
            try:
                data = c.recv(1024)
                if c not in self.muteds:
                    self.broadcast(c, data)

            except socket.error:
                c.close()

    def manage(self):
        time.sleep(3)
        while True:
            choice = input("COMMANDS \n 1-kick \n 2-mute someone \n 3-unmmute someone \n 4-mmute all \n 5-unmmute all \n 5-muted list \n choice:\n")
            if choice == "kick":
                name = input("Who do you want to kick:")
                self.kicker(name)

            elif (choice == "mute"):
                name = input("Who do you want to mute:")
                self.mute_someone(name)

            elif (choice == "unmute"):
                name = input("Who do you want to unmute:")
                self.unmute_someone(name)

            elif (choice == "mute all"):
                self.mute_all()
            elif (choice == "unmute all"):
                self.unmute_all()
            elif (choice == "muted list"):
                print(self.muteds)

            else:
                print("wrong command")


    def kicker(self,name):

        if name in self.nicknames:
            name_index = self.nicknames.index(name)
            client_to_kick = self.connections[name_index]
            self.kicks.append(name)
            self.connections.remove(client_to_kick)
            client_to_kick.close()
            self.nicknames.remove(name)
            print(f"{name} kicked")

    def mute_someone(self,name):
        if name in self.nicknames:
            if name not in self.muteds:
                name_index = self.nicknames.index(name)
                self.muteds.append(self.connections[name_index])
                print(f"{name} muted")

    def unmute_someone(self,name):
        if name in self.nicknames:
            name_index = self.nicknames.index(name)
            if self.connections[name_index] in self.muteds:
                self.muteds.remove(self.connections[name_index])
                print(f"{name} unmuted")

    def mute_all(self):
        for x in self.connections:
            if x not in self.muteds:
                self.muteds.append(x)
        print("muted all")


    def unmute_all(self):
        self.muteds.clear()

#chat server

class Server2:
    def __init__(self):
        self.nicknames = []
        #method to get local ip adress of computer we use
        self.ip = socket.gethostbyname(socket.gethostname())

        while 1:

            try:
                # self.port = int(input('port no:'))
                #We should stay away from  1-1024 ports. These are used for common apps.
                self.port2 = 9292
                #it is about protocol. second paramater is about protocols. socket.SOCK_STREAM is used for TCP.
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #It ıs function to bind the server. we bind the server to local ip and with port. And we connected with these ip and port with clients.
                self.socket.bind((self.ip, self.port2))


                break
            except:
                print("cant connect the port")
        print("server2-chat server")
        print('IP:' + self.ip)
        print('port:' + str(self.port2))
        print("------------------------------")

        self.connections = []
        self.accept_connections()

    def accept_connections(self):
        self.socket.listen(100)



        while True:
            #print(Client.nickname)
            client, addr = self.socket.accept()
            self.connections.append(client)

            a =client.recv(1024)
            b = a.decode('utf-8')

            c_separated1 = str(b).split(" ")

            c_separated2 = c_separated1[0].split("\n")[0]


            self.nicknames.append(c_separated2[9:])
            zaman = time.strftime("%d:%m:%Y %H:%M:%S")
            print("----------------------------")
            print(f"{a.decode('utf-8')} chat server also.")

            print("----------------------------")



            threading.Thread(target=self.handle_client, args=(client, addr)).start()


    def broadcast(self, sock, data,receiver_user,user_index):

        for client in self.connections:
            if client == self.connections[user_index]:
                if client != self.socket and client != sock:
                    try:
                        client.send(data)
                    except:
                        pass

    def handle_client(self, client, addr):
        while 1:
            try:
                data = client.recv(1024)

                receiver_user = data.decode('utf-8').split(" ")[0]
                user_index = self.nicknames.index(receiver_user)

                if receiver_user in self.nicknames:
                    self.broadcast(client, data, receiver_user,user_index)




            except socket.error:
                client.close()






            c_separated1 = str(b).split(" ")

            c_separated2 = c_separated1[0].split("\n")[0]


            self.nicknames.append(c_separated2[9:])
            zaman = time.strftime("%d:%m:%Y %H:%M:%S")
            print("----------------------------")
            print(f"{a.decode('utf-8')} {zaman}")

            print("----------------------------")


            threading.Thread(target=self.handle_client, args=(c, addr)).start()




    def broadcast(self, sock, data):
        for client in self.connections:
            if client != self.socket and client != sock:
                try:
                    client.send(data)
                except:
                    pass

    def handle_client(self, c, addr):
        while 1:
            try:
                data = c.recv(1024)
                self.broadcast(c, data)

            except socket.error:
                c.close()


class Room1:
    def __init__(self):
        self.nicknames = []

        #method to get local ip adress of computer we use
        self.ip = socket.gethostbyname(socket.gethostname())

        while 1:

            try:
                # self.port = int(input('port no:'))
                #We should stay away from  1-1024 ports. These are used for common apps.
                self.port = 9101
                #it is about protocol. second paramater is about protocols. socket.SOCK_STREAM is used for TCP.
                self.room1_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #It ıs function to bind the server. we bind the server to local ip and with port. And we connected with these ip and port with clients.
                self.room1_socket.bind((self.ip, self.port))


                break
            except:
                print("cant connect the port")
        print("room1-voice server")
        print('IP:' + self.ip)
        print('port:' + str(self.port))
        print("------------------------------")




        self.connections = []
        self.accept_connections()


    def accept_connections(self):
        self.room1_socket.listen(100)




        while True:

            c, addr = self.room1_socket.accept()
            self.connections.append(c)

            a =c.recv(1024)
            b = a.decode('utf-8')

            c_separated1 = str(b).split(" ")
            c_separated2 = c_separated1[0].split("\n")[0]



            self.nicknames.append(c_separated2[9:])
            zaman = time.strftime("%d:%m:%Y %H:%M:%S")
            print("----------------------------")
            print(f"{a.decode('utf-8')} {zaman} to room1")

            print("----------------------------")



            threading.Thread(target=self.handle_client, args=(c, addr)).start()




    def broadcast(self, sock, data):
        for client in self.connections:
            if client != self.room1_socket and client != sock:
                try:
                    client.send(data)
                except:
                    pass

    def handle_client(self, c, addr):
        while 1:
            try:
                data = c.recv(1024)
                self.broadcast(c, data)

            except socket.error:
                c.close()


class Room2:
    def __init__(self):
        self.nicknames = []

        #method to get local ip adress of computer we use
        self.ip = socket.gethostbyname(socket.gethostname())

        while 1:

            try:
                # self.port = int(input('port no:'))
                #We should stay away from  1-1024 ports. These are used for common apps.
                self.port = 9102
                #it is about protocol. second paramater is about protocols. socket.SOCK_STREAM is used for TCP.
                self.room2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #It ıs function to bind the server. we bind the server to local ip and with port. And we connected with these ip and port with clients.
                self.room2_socket.bind((self.ip, self.port))




                break
            except:
                print("cant connect the port")
        print("room2-voice server")
        print('IP:' + self.ip)
        print('port:' + str(self.port))
        print("------------------------------")




        self.connections = []
        self.accept_connections()


    def accept_connections(self):
        self.room2_socket.listen(100)




        while True:

            c, addr = self.room2_socket.accept()
            self.connections.append(c)

            a =c.recv(1024)
            b = a.decode('utf-8')

            c_separated1 = str(b).split(" ")
            c_separated2 = c_separated1[0].split("\n")[0]



            self.nicknames.append(c_separated2[9:])
            zaman = time.strftime("%d:%m:%Y %H:%M:%S")
            print("----------------------------")
            print(f"{a.decode('utf-8')} {zaman} to room2")

            print("----------------------------")


            # threading.Thread(target=self.manage).start()
            threading.Thread(target=self.handle_client, args=(c, addr)).start()




    def broadcast(self, sock, data):
        for client in self.connections:
            if client != self.room2_socket and client != sock:
                try:
                    client.send(data)
                except:
                    pass

    def handle_client(self, c, addr):
        while 1:
            try:
                data = c.recv(1024)
                self.broadcast(c, data)

            except socket.error:
                c.close()











if __name__ == "__main__":
    # server = Server()



    def creat_server1():
        server = Server()
    def creat_server2():
        server = Server2()
    def creat_room1():
        room1 = Room1()
    def creat_room2():
        room1 = Room2()


    # creat_server2()
    threading.Thread(target=creat_server2).start()
    time.sleep(0.5)
    # creat_server1()
    threading.Thread(target=creat_server1).start()
    time.sleep(0.5)
    #creat_room1()
    threading.Thread(target=creat_room1).start()

    time.sleep(0.5)
    # creat_room1()
    threading.Thread(target=creat_room2).start()

    # # server.start()
