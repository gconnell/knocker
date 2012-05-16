#!/usr/bin/python

import commands
import hashlib
import os
import pwd
import socket
import struct
import sys
import time

def shas(secret):
  t = time.time()
  t -= t % 60
  for i in [t - 60, t, t + 60]:
    hasher = hashlib.sha1()
    hasher.update(secret)
    hasher.update(struct.pack('>i', t))
    print hasher.hexdigest()
    yield hasher.hexdigest()

def main():
  if len(sys.argv) != 2:
    print 'Usage:  %s <SECRET>' % sys.argv[0]
    sys.exit(1)
  secret = sys.argv[1]
  print 'STARTING'
  print 'Dropping permissions to knocker'
  pw_info = pwd.getpwnam('knocker')
  os.setgid(pw_info.pw_gid)
  os.setuid(pw_info.pw_uid)
  print 'Dropped permissions to UID', os.getuid(), 'GID', os.getgid()

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
    if msg in shas(secret):
      print 'huzzah!'
      status, output = commands.getstatusoutput(
        '/usr/bin/sudo /root/opensesame.sh')
      time.sleep(5)
      status, output = commands.getstatusoutput(
        '/usr/bin/sudo /root/closesesame.sh')


if __name__ == '__main__':
  main()
