#!/usr/bin/python3

from hashlib import md5
import ssl
import sys

fname = sys.argv[1]
f = open(fname, "wb")
while True:
	rand = ssl.RAND_pseudo_bytes(256 * 1024)[0]
	dig = md5(rand).digest()
	f.write(rand)
	f.write(dig)
