                                                          TCP_VOICE_CHAT_APP ON LOCAL SERVER--PYTHON-
                                                          TCP_VOICE_CHAT_APP (WITH PRIVATE CHAT )

TCP Voice chat application  with Python. There are also extra TCP message chat server that clients connect it simultaneously at the same time with main voice server connection. Also server1(main voice chat server) has 
kicking someone , muting someone , unmuting someone, mute all , unmute all, show muted list methods. 

When we run the server.py file, we get a screen like this. On server.py output we see Server1(main voice chat server) , server2(private message chat server) , room1(private voice chat room) , room2(private voice chat room) ip and port knowledges. 

![1](https://github.com/emrearat1/TCP_VOICE_CHAT_APP--PYTHON-/assets/69716092/6759b529-23b0-4bff-892d-d081871ffbf4)

If a client connects to main server, client informations can seen  on the server.py output.

![2](https://github.com/emrearat1/TCP_VOICE_CHAT_APP--PYTHON-/assets/69716092/2d4e97b7-3a83-47cf-acad-643c127ea829)


                                                          USAGE
Run server.py. When It starts to run ip addresses and ports of server1 , server2, room1 and room2 servers are seen on the output.(Server.py gets your ip adress automaticly). 
Now it is time to connect server. Before the run client.py change this code with your local ip adress. self.target_ip = '#put here your local ip adress of your main server (you can learn it from output of your server.py)'. Now run client.py. Client.py asks your nickname. After the nickname is given ,client connects to main voice chat server and  private chat server. If any problem happens to connect server , client tries to connect server every 5 second. After the third try client, shut itselfs down.
                                                          
![3](https://github.com/emrearat1/TCP_VOICE_CHAT_APP--PYTHON-/assets/69716092/a729d82f-02c5-466a-8402-83ee1e8aad01)

Client can do 2 things , first one is messaging someone(privately). If you write message after that program is going to ask you who do you want to message.

![4](https://github.com/emrearat1/TCP_VOICE_CHAT_APP--PYTHON-/assets/69716092/463ed047-4290-4a81-a476-d6591fc843f0)
![5](https://github.com/emrearat1/TCP_VOICE_CHAT_APP--PYTHON-/assets/69716092/5208ba6b-0811-423e-a7cb-987f8fc5a81e)

Other choice is changing room. If you write change room then program is going to ask you port of the room you want to join.
![6](https://github.com/emrearat1/TCP_VOICE_CHAT_APP--PYTHON-/assets/69716092/1d041d99-b2c0-44b1-873e-9012233f92c3)

Now it is time to functions of server.py. There is few commands to choice on server. Lets mute someone.

![7](https://github.com/emrearat1/TCP_VOICE_CHAT_APP--PYTHON-/assets/69716092/4996ce94-2f8a-4ae4-9526-b2d2268f3765)
![9](https://github.com/emrearat1/TCP_VOICE_CHAT_APP--PYTHON-/assets/69716092/0a08d8ad-faca-4445-8bc6-9138c1bbacc4)

