#!/bin/python
'''Huginn ok Muninn fljúga hverjan dag'''

import time
'''Jörmungrund yfir;'''

timestamp = int(time.time())
'''óumk ek of Hugin, at hann aftr né komi-t,'''

open("/var/streak/_%s"%str(timestamp), 'w')
'''þó sjámk meir of Munin.'''
