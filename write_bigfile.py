#!/usr/bin/python3 -Bu

from hashlib import md5
import subprocess
import sys

fname = sys.argv[1]
f = open(fname, "wb")
# Both os.urandom and ssl.RAND_pseudo_bytes are slow, so use this monstrosity instead
p = subprocess.Popen('openssl enc -aes-128-ctr -pass "pass:$(dd if=/dev/urandom bs=128 count=1 2>/dev/null | base64)" < /dev/zero', shell=True, stdout=subprocess.PIPE)
while True:
	rand = p.stdout.read(256 * 1024)
	dig = md5(rand).digest()
	f.write(rand)
	f.write(dig)
