knocker
=======

Port knocker client/server.
The server opens up the SSH server on receipt of a UDP packet.
Server drops permissions on startup, sudoers file allows the
users to just run the open/close scripts which add and remove
a firewall hole.

NOTES
-----

1. This is not meant for any type of production use.  It is a very simple
script.  I set it up specifically because I am paranoid and do not want a
standard service (SSH) open on a standard port (22).
2. It currently opens up blanket access to port 22 when port knocking has
completed successfully.  This could be pretty easily changed to open up specific
access to the knocking client, and I will probably do that soon.
