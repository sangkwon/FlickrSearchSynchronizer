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

#print('keyword', keyword)

url_type = 'url_l'
params = urllib.parse.urlencode({
	'method': 'flickr.photos.search',
	'api_key': apikey,
	'text': keyword,
	'safe_search': '1',
	'content_type': '1',
	'media': 'photos',
	'min_taken_date':1367048429,
	'per_page': '100',
	'format': 'json',
	'extras': 'date_taken,'+url_type,
	'nojsoncallback': '1'
})

url = "https://api.flickr.com/services/rest/" + "?" + params
#print(url)

data = urllib.request.urlopen(url).read()
#TODO error handling

j = json.loads(data.decode('utf-8'))
#print(j)

total = j['photos']['total']
photos = j['photos']['photo']

exit();

cnt = 0
for photo in photos:
	if url_type in photo:
		url_o = photo.get(url_type)
		image_path = path+"/pic"+str(cnt)+".jpg"
		print(url_o+" retriving... to " + image_path)
		urllib.request.urlretrieve(url_o, image_path)
		cnt = cnt + 1
