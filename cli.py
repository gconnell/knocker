#!/usr/bin/python
#
# Copyright 2012 Graeme Connell
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
  hasher.update(getpass.getpass('Knocker secret').strip())
  hasher.update(struct.pack('>i', t))

  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  print hasher.hexdigest()
  s.sendto(hasher.hexdigest(), (host, 7777))

  time.sleep(0.25)
  os.execlp('/usr/bin/ssh', 'ssh', host, *sys.argv[2:])

if __name__ == '__main__':
  main()
