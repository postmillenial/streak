#!/bin/python

import os

#when it fires, it lists _#.py

import time

timestamp = int(time.time())

f = open("/var/streak/_%s"%str(timestamp), 'w')

