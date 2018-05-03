#!/usr/bin/env python
import subprocess
from twython import Twython
import json
import configparser

config = configparser.ConfigParser()
config.read('config_auth.properties')

# Twython authentication
# your twitter consumer and access information goes here
apiKey = config['twitter']['apiKey']
apiSecret = config['twitter']['apiSecret']
accessToken =  config['twitter']['accessToken']
accessTokenSecret = config['twitter']['accessTokenSecret']

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

DMs = api.get_direct_messages(count=1, skip_status='true')

for i in range(0,1):
	if 'IP' in DMs[i]['text']:
		output = subprocess.check_output("ifconfig | grep inet", shell=True)
		api.send_direct_message(screen_name=config['twitter']['receiverTwitterUsername'],text=output)		
		print "DM sent for IP address."
	elif 'ifconfig' in DMs[i]['text']:
		output = subprocess.check_output("ifconfig", shell=True)
		api.send_direct_message(screen_name=config['twitter']['receiverTwitterUsername'],text=output)
		print "DM sent for ifconfig"
	else:
		print "Nothing was asked for. :)"

print "Done"
