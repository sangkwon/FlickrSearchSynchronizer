#!/usr/bin/python
#flickr_sync.py

import os
import sys
import urllib
import urllib.parse
import urllib.request
import json

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

url = "https://api.flickr.com/services/rest/" + "?" + params
#print(url)

data = urllib.request.urlopen(url).read()
#TODO error handling

j = json.loads(data.decode('utf-8'))

total = j['photos']['total']
photos = j['photos']['photo']

for photo in photos:
	print(photo['title'])

