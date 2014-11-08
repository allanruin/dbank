# -- coding: UTF-8 
from pyquery import PyQuery as pq
from urlparse import urljoin
import Queue
import urllib
from threading import Thread
import os
import json
import dbank_encry

domain_url = "http://dl.vmall.com/c0p2ca6lwq"

target_page = "http://dl.vmall.com/c0p2ca6lwq"
# d = pq(url=target_page,opener=lambda url, **kw: urllib.urlopen(url).read().decode("utf-8"))
d = pq(url=target_page)

scripttext =  d("script:eq(1)").text()  #globallinkdata是第二个script标签

# var globallinkdata = {"retcode":"0000","data":
# strip of the var ... part and the trailing ';'

scripttext = scripttext[scripttext.find("{"):len(scripttext)-1]
# print scripttext

globallinkdata =  json.loads(scripttext)
# print globallinkdata

encrykey = globallinkdata["data"]["encryKey"]
print encrykey
myfiles = globallinkdata["data"]["resource"]["files"]
encry_direct_links = []
encry_thunder_links = []
for fi in myfiles:
	encry_direct_links.append( fi["downloadurl"] )
	encry_thunder_links.append( fi["xunleiurl"] )

print encry_direct_links
print encry_thunder_links

print "\n"

for link in encry_direct_links:
	print dbank_encry.decrypt(link,encrykey)

for link in encry_thunder_links:
	print dbank_encry.decrypt(link,encrykey)


