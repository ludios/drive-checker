#!/usr/bin/python

from hashlib import md5
import os
import sys

fname = sys.argv[1]
f = open(fname, "wb")
while True:
	rand = os.urandom(64 * 1024)
	dig = md5(rand).digest()
	f.write(rand)
	f.write(dig)
