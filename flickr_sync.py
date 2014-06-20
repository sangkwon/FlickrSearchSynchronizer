#!/usr/bin/python
#flickr_sync.py

import os
import sys
import glob
import fileinput
import urllib
import urllib.parse
import urllib.request

#### Function Define ##########



#### Main Loop ###############
if len(sys.argv) <= 3:
	print("Usages:")
	print("\t"+__file__+"<apikey> <keyword> <path>")
	sys.exit(-1)

apikey = sys.argv[1]
keyword = sys.argv[2]
path = sys.argv[3]

params = urllib.parse.urlencode({
	'method': 'flickr.photos.search',
	'api_key': apikey,
	'text': keyword,
	'safe_search': '1',
	'content_type': '1',
	'media': 'photos',
	'per_page': '500',
	'format': 'json',
	'nojsoncallback': '1'
})

url = "https://api.flickr.com/services/rest/"

data = urllib.request.urlopen(url+"?"+params).read()

print(data)

