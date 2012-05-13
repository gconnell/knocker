knocker
=======

Port knocker client/server.
The server opens up the SSH server on receipt of a UDP packet.
Server drops permissions on startup, sudoers file allows the
users to just run the open/close scripts which add and remove
a firewall hole.
