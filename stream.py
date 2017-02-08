# -*- coding: utf-8 -*-

from twitter import *
from time import sleep

token = ""
token_secret = ""
consumer_key = ""
consumer_secret = ""
    
t = Twitter(auth = OAuth(token, token_secret, consumer_key, consumer_secret))

t_userstream = TwitterStream(auth = OAuth(token, token_secret, consumer_key, consumer_secret), domain='userstream.twitter.com')

for msgs in t_userstream.user():
    for msg in msgs:
        if "event" == msg:
            notification = msgs
            if notification['event'] == 'favorite':
                user = notification['target']
                user2 = notification['source']
                try:
                    if user['screen_name'] == "SocietalTrends":
                        #followの場合は関係ない
                        #favoriteのみ ふぁぼされる度に発生
                        t.statuses.update(status= "@{}\nありがとう！".format(user2['screen_name']))
                        print("I sent a reply!")
                        sleep(1)
                except TwitterHTTPError:
                    pass

