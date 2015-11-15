import oauth2 as oauth
import urllib
import simplejson as json

# Go to https://apps.twitter.com/ to setup a project
consumer_key='xxx'
consumer_secret='xxx'
access_token_key='xxx'
access_token_secret='xxx'
consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
token = oauth.Token(key=access_token_key, secret=access_token_secret)
client = oauth.Client(consumer, token)
q = "xxx" # what you are querying
lat = "xx.xxx" # latitude 
lng = "xx.xxx" # longitude 
r = "xx" # radius 
url = """https://api.twitter.com/1.1/search/tweets.json?q=%s&include_entities=true&result_type=recent&geocode=%s,%s,%smi""" % (q,lat,lng,r)

header, fhand = client.request(url, method="GET")
jDoc = json.loads(fhand, encoding='utf8')
for tweet in jDoc['statuses']:
  # prettify output
	print(json.dumps(tweet, sort_keys=True, indent=4 * ' '))
