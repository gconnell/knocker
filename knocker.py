#!/usr/bin/python

import commands
import hashlib
import os
import socket
import struct
import time

SECRET = None
UID = 1001
GID = 1001

def shas():
  assert SECRET is not None
  t = time.time()
  t -= t % 60
  for i in [t - 60, t, t + 60]:
    hasher = hashlib.sha1()
    hasher.update(SECRET)
    hasher.update(struct.pack('>i', t))
    print hasher.hexdigest()
    yield hasher.hexdigest()

def main():
  global SECRET
  if len(sys.argv) != 2:
    print 'Usage:  %s <SECRET>' % sys.argv[0]
    sys.exit(1)
  SECRET = sys.argv[1]
  print 'STARTING'
  print 'Dropping permissions to knocker'
  os.setgid(GID)
  os.setuid(UID)
  print os.getuid(), os.getgid()

  print 'Forking'
  if os.fork():
    print 'Main thread exiting'
    return
  print 'Background thread running'

  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind(('', 7777))
  while True:
    msg, sender = s.recvfrom(1024)
    print msg
    if msg in shas():
      print 'huzzah!'
      status, output = commands.getstatusoutput(
        '/usr/bin/sudo /root/opensesame.sh')
      time.sleep(5)
      status, output = commands.getstatusoutput(
        '/usr/bin/sudo /root/closesesame.sh')


if __name__ == '__main__':
  main()
