#!/usr/bin/python3

from hashlib import md5
import os
import sys

fname = sys.argv[1]
try:
	start_at = int(sys.argv[2].replace(",", ""))
except IndexError:
	start_at = 0
f = open(fname, "rb")
f.seek(start_at - (start_at % (256 * 1024 + 16)))
while True:
	block = f.read(256 * 1024)
	written_dig = f.read(16)
	if len(block) < 256 * 1024 or len(written_dig) < 16:
		print("Done")
		break
	now_dig = md5(block).digest()
	if now_dig != written_dig:
		print("Bad checksum at %r" % (f.tell(),))
