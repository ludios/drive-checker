from hashlib import md5
import os
import sys

fname = sys.argv[1]
try:
	start_at = long(sys.argv[2].replace(",", ""))
except IndexError:
	start_at = 0
f = open(fname, "rb")
f.seek(start_at - (start_at % (64 * 1024 + 128/8)))
while True:
	block = f.read(64 * 1024)
	written_dig = f.read(128/8)
	if len(block) < 64 * 1024 or len(written_dig) < 128/8:
		print "Done"
		break
	now_dig = md5(block).digest()
	if now_dig != written_dig:
		print "Bad checksum at %r" % (f.tell(),)
	#print ".",
