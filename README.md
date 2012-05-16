knocker
=======

Port knocker client/server.
The server opens up the SSH server on receipt of a UDP packet.
Server drops permissions on startup, sudoers file allows the
users to just run the open/close scripts which add and remove
a firewall hole.

USAGE
-----

The server can be installed by running the install.sh script.

To connect to the server over SSH, run the cli.py script with the hostname
you are connecting to.  Example:

  ./cli.py my.host.com

You will be prompted for a knocker secret.  Enter the secret you configured your
server with in the /etc/init/knocker.conf file created by the install script.
If the server accepts your secret, it will open up the SSH port on your
machine for a short period of time (5 seconds).  The ./cli.py script will then
attempt to execute an SSH connection against the host.  If it succeeds, you will
get a prompt on your remote server.

NOTES
-----

1. This is not meant for any type of production use.  It is a very simple
script.  I set it up specifically because I am paranoid and do not want a
standard service (SSH) open on a standard port (22).
2. It currently opens up blanket access to port 22 when port knocking has
completed successfully.  This could be pretty easily changed to open up specific
access to the knocking client, and I will probably do that soon.
