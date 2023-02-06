Compilation:
python sock_server [port number]

For each client:
nc -u 127.0.0.1 [port number]

Design:
I designed my server application based on the specifications. I also
changed a few things to create a better user experience, such as
only sending messages to other clients and not yourself so it doesn't
post every message twice if you are the sender.
When you use /list, it prints all information of every client including IP, port, and nickname. Sharing IP and port may not be the best idea but I designed it this way just to give the most information possible.
/quit also notifies every user in the chatroom that the specific user has quit so it's less jarring when someone quits randomly.
