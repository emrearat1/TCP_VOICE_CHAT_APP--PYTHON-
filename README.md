                                                          TCP_VOICE_CHAT_APP ON LOCAL SERVER--PYTHON-
                                                          TCP_VOICE_CHAT_APP (WITH PRIVATE CHAT )

TCP Voice chat application  with Python. There are also extra TCP message chat server that clients connect it simultaneously at the same time with main voice server connection. Also server1(main voice chat server) has 
kicking someone , muting someone , unmuting someone, mute all , unmute all, show muted list methods. 

When we run the server.py file, we get a screen like this. On server.py output we see Server1(main voice chat server) , server2(private message chat server) , room1(private voice chat room) , room2(private voice chat room) ip and port knowledges. 
![1](https://github.com/emrearat1/TCP_VOICE_CHAT_APP--PYTHON-/assets/69716092/fd1a7acf-d0cd-4043-b851-2a45c0fbcc6e)



If a client connects to main server, client informations can seen  on the server.py output.

![2](https://github.com/emrearat1/TCP_VOICE_CHAT_APP--PYTHON-/assets/69716092/54ee6c2a-6732-468b-9022-cd3f41f3a918)





                                                          USAGE
Run server.py. When It starts to run ip addresses and ports of server1 , server2, room1 and room2 servers are seen on the output.(Server.py gets your ip adress automaticly). 
Now it is time to connect server. Before the run client.py change this code with your local ip adress. self.target_ip = '#put here your local ip adress of your main server (you can learn it from output of your server.py)'. Now run client.py. Client.py asks your nickname. After the nickname is given ,client connects to main voice chat server and  private chat server. If any problem happens to connect server , client tries to connect server every 5 second. After the third try client, shut itselfs down.
                                                          
![3](https://github.com/emrearat1/TCP_VOICE_CHAT_APP--PYTHON-/assets/69716092/3a99bf0e-8c9e-4382-8432-0c2804dd024b)


Client can do 2 things , first one is messaging someone(privately). If you write message after that program is going to ask you who do you want to message.
![4](https://github.com/emrearat1/TCP_VOICE_CHAT_APP--PYTHON-/assets/69716092/c2607b22-5482-4094-8ab3-3598438cc925)
![5](https://github.com/emrearat1/TCP_VOICE_CHAT_APP--PYTHON-/assets/69716092/29b74ef2-7ca9-44ec-a8a3-f5fea1ca77dc)


Other choice is changing room. If you write change room then program is going to ask you port of the room you want to join.
![6](https://github.com/emrearat1/TCP_VOICE_CHAT_APP--PYTHON-/assets/69716092/c99c715b-f3db-44f0-b108-0b174c70aa18)


Now it is time to functions of server.py. There is few commands to choice on server. Lets mute someone.

![7](https://github.com/emrearat1/TCP_VOICE_CHAT_APP--PYTHON-/assets/69716092/a5cdf30b-2fd8-48a5-95e1-8d8e8d82be69)
![9](https://github.com/emrearat1/TCP_VOICE_CHAT_APP--PYTHON-/assets/69716092/0d1ba8d2-c36f-40dc-932b-f711869f12a2)


