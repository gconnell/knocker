#!/bin/bash

iptables -A INPUT -i eth0 -p tcp --dport 22 -m state --state NEW -j ACCEPT
