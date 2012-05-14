#!/usr/bin/python

import getpass
import hashlib
import os
import socket
import struct
import sys
import time

def main():
  try:
    host = sys.argv[1]
  except IndexError:
    print 'Usage:  %s <hostname>' % sys.argv[0]
    return
  t = int(time.time())
  t -= t % 60
  hasher = hashlib.sha1()
  hasher.update(getpass.getpass().strip())
  hasher.update(struct.pack('>i', t))
  
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  print hasher.hexdigest()
  s.sendto(hasher.hexdigest(), (host, 7777))

  time.sleep(0.25)
  os.execlp('/usr/bin/ssh', 'ssh', host, *sys.argv[2:])

if __name__ == '__main__':
  main()
