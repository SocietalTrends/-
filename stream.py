# -*- coding: utf-8 -*-

from twitter import *
from time import sleep

#JSONファイルの出力のため
import json


consumer_key = "NqZd7EPwl7hlcaonKbvBSmvfW"
consumer_secret = "7MB3iFrGjY4tPIPd96dbbqd3Rako5fOMsIgOy3GU3LmMe2Pb88"
token = "1226105854367109120-0n6fqfHjv9H53eKocaxPE7vKOI6XSp"
token_secret = "ZaC3MitOO17kDGQaTc6njupivxjwG4gpc92MdXhilOn3q"
username = "conybrownbrown"

t = Twitter(auth = OAuth(token, token_secret, consumer_key, consumer_secret))

"""
ln = t.statuses.home_timeline()
with open('./test_new.json', 'w', encoding='utf-8') as f:
    json.dump(ln, f, indent=2, ensure_ascii=False)
"""
auth = OAuth(
    consumer_key = "NqZd7EPwl7hlcaonKbvBSmvfW",
    consumer_secret = "7MB3iFrGjY4tPIPd96dbbqd3Rako5fOMsIgOy3GU3LmMe2Pb88",
    token = "1226105854367109120-0n6fqfHjv9H53eKocaxPE7vKOI6XSp",
    token_secret = "ZaC3MitOO17kDGQaTc6njupivxjwG4gpc92MdXhilOn3q"
)
t_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')
for msgs in t_userstream.user():
        print(msg)
"""
    for msg in msgs:
        if "event" == msg:
            notification = msgs
            if notification['event'] == 'favorite':
                user = notification['target']
                user2 = notification['source']
                try:
                    if user['screen_name'] == username:
                        #followの場合は関係ない
                        #favoriteのみ ふぁぼされる度に発生
                        t.statuses.update(status= "@{}\nありがとう！".format(user2['screen_name']))
                        print("I sent a reply!")
                        sleep(1)
                except TwitterHTTPError:
                    pass
"""