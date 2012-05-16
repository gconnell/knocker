#!/bin/bash
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

# Installs knocker on a server.

set -e
cd $(dirname $0)
echo "Installing from directory $(pwd)"
sudo cp opensesame.sh /root/opensesame.sh
sudo cp closesesame.sh /root/closesesame.sh
sudo cp knocker.conf /etc/init/knocker.conf
sudo cp knocker.py /root/knocker.py
sudo ln -s /lib/init/upstart-job /etc/init.d/knocker
echo 'ADD THE FOLLOWING TO YOUR /etc/sudoers FILE:'
cat sudoers
