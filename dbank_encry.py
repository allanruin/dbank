# -- coding: UTF-8 
import base64
import hashlib


def cfunc(h,l):
	k = []
	e = 0
	d = ""
	g = ""

	k = [f for f in xrange(256)]
	for f in xrange(256):
		e = (e +k[f] + ord(h[f % len(h)])) % 256
		d = k[f]
		k[f] = k[e]
		k[e] = d
		g += chr(ord(l[m]) ^ k[ (k[f]+k[e]) % 256] )

	return g

def bfunc(d,e):
	g=""
	k=len(e)
	f=len(d)
	for h in xrange(f):
		j=ord(d[h]) ^ ord(e[h%k])
		g += chr(j)

	return g



def decrypt(g,e):
	g = base64.b64decode(g)
	f = e[0:2]
	d = ""
	if f=="ea":
		d = g
	elif f=="eb":
		d = bfunc(g, cfunc(e,e))
	elif f=="ed":
		m = hashlib.md5()
		m.update(e)
		d = bfunc(g, m.hexdigest())
	else:
		d = g

	return d


if __name__ == '__main__':
	# test
	encryKey = "ed41664556"
	url = "TVEUX1AAFAobGzBkf1tUeTdEeQsBRGxyFUEFWwNQWiJOTDgDDREqAmZCBQMMR1IDI1h6U3tEUgc0TTBhA09zVmBALVt1ECljBV0FZlVHanJVAnsIXkBkWTR5NXUHDlk9eBY7WwUPK3h1TTgDfAZSeQFLfA9SC3tmOFsxYncIdTFsCS9lUx0odGVZBVsJAX1bBgF4NlVYeXY4BTFie0B1MnNQLHVhUSxdWEMxZXxNfUhRB3khDQZ7ZlYGL3VoT2gxYAsrXEwSB2dlDStfa15gZSBebzpvQmxxUlkDfn8BbwlWBA=="
	print decrypt(url,encryKey)
	#thunder://QUFodHRwOi8vZGwudm1hbGwuY29tL2Rvd25sb2FkL1Bvd2VyQW1wK3YyLjAuOS1idWlsZC01MjgrRlVMTC56aXA/Zj1jMHAyY2E2bHdxJmk9MSZoPTE0MTU0NTgxNDQmdj05Mjc2NTljOCZ1PTIxMWJiMDU4JmlwPTEyMy44OC44MS42NCZwPTY2JmxwaWQ9JnRjPTEmYXVpZD0mbHM9Wlo=
