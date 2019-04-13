#!/usr/bin/env python
import subprocess
from twython import Twython
import configparser


def read_twitter_bot_config():
    try:
        config = configparser.ConfigParser()
        config.read('config_auth.properties')

        # Twython authentication
        # your twitter consumer and access information goes here
        apiKey = config['twitter']['apiKey']
        apiSecret = config['twitter']['apiSecret']
        accessToken = config['twitter']['accessToken']
        accessTokenSecret = config['twitter']['accessTokenSecret']
        receiverTwitterId = config['twitter']['receiverTwitterId']
        return apiKey, apiSecret, accessToken, accessTokenSecret, receiverTwitterId
    except Exception as e:
        print(str(e))
        print('Could not find the required config_auth.properties file with proper values. Kindly go through Readme.md!')
        raise ValueError('Could not get config!')


def get_formatted_data(receiverTwitterId, textMessage):
    return {
        'event': {
            'type': 'message_create',
            'message_create': {
                'target': {'recipient_id': receiverTwitterId, },
                'message_data': {
                    'text': textMessage,
                }
            }
        }
    }


def check_dm_and_respond():
    # get configs
    apiKey, apiSecret, accessToken, accessTokenSecret, receiverTwitterId = read_twitter_bot_config()

    # initialise Twython
    api = Twython(apiKey, apiSecret, accessToken, accessTokenSecret)

    # Get the last DM
    DMs = api.get_direct_messages(count=1, skip_status='true')

    if 'events' in DMs and len(DMs['events']) > 0:
        msg = DMs['events'][0]
        if 'message_create' in msg and 'message_data' in msg['message_create'] and 'text' in msg['message_create'][
            'message_data']:
            text = msg['message_create']['message_data']['text']
            text = text.lower()
            print('Received DM : {}'.format(text))

            if 'ip' in text:
                output = subprocess.check_output("ifconfig | grep inet", shell=True)
                event_data = get_formatted_data(receiverTwitterId, output)
                api.send_direct_message(**event_data)
                print('Sent IP address')

            if 'ifconfig' in text:
                output = subprocess.check_output("ifconfig", shell=True)
                event_data = get_formatted_data(receiverTwitterId, output)
                api.send_direct_message(**event_data)
                print('Sent ifconfig')

            if 'wifi' in text or 'iwconfig' in text:
                output = subprocess.check_output("iwconfig", shell=True)
                event_data = get_formatted_data(receiverTwitterId, output)
                api.send_direct_message(**event_data)

            else:
                print("Don't know how to handle this text")

    print("Done")


if __name__ == "__main__":
    check_dm_and_respond()