# -*- coding: utf-8 -*-

from twitter import *
from time import sleep
import random

def Init():
    consumer_key = "NqZd7EPwl7hlcaonKbvBSmvfW"
    consumer_secret = "7MB3iFrGjY4tPIPd96dbbqd3Rako5fOMsIgOy3GU3LmMe2Pb88"
    token = "1226105854367109120-0n6fqfHjv9H53eKocaxPE7vKOI6XSp"
    token_secret = "ZaC3MitOO17kDGQaTc6njupivxjwG4gpc92MdXhilOn3q"
    
    #premise
    user_name = input("Please enter username: \n")
    maximum = int(input("Please enter the number of user you want to follow(It can to follow until 1000 users now): \n")) #maximum follow

    return Twitter(auth = OAuth(token, token_secret, consumer_key, consumer_secret)), user_name, maximum

def mute(t, user):
    statusUpdate = t.friends.list(screen_name = user, cursor=-1, count= 200)
    users = statusUpdate['users']
    current = 0
    #print(users)
    for follow in users:
        t.mutes.users.create(screen_name=follow['screen_name'])
        current += 1
        print("{0:3d}: @".format(current)+follow['screen_name']+" muted!")

def main(t, user, maximum):
    _cursor = -1 #default
    maximumPages = 5  #the number of page def:1000 users
    _count = 200
    current = 0 #order
    currentPage = 0 # current page
    me = t.account.settings() #own user

    while currentPage < maximumPages:
        statusUpdate = t.followers.list(screen_name= user, cursor=_cursor, count= _count)
        users = statusUpdate['users']
        for follow in users:
            if follow['screen_name'] == me['screen_name']:
                #フォローする対象が自分だった時
                pass
            elif follow['following'] == True:
                #既にフォローしていた時
                pass
            elif follow['follow_request_sent'] == True:
                pass
            else:
                try:
                    t.friendships.create(screen_name= follow['screen_name'])
                    t.mutes.user.create(screen_name= follow['screen_name'])
                    #t.statuses.update(status= "@ririka_124 \n"+str(current))
                    current += 1
                    print("{0:3d}: @".format(current)+follow['screen_name']+" Followed!")
                    if current >= maximum:
                        break
                    sleep(random.randint(3,5))
                except TwitterHTTPError:
                    pass
        if current >= maximum:
           break
        currentPage += 1
        _cursor=statusUpdate['next_cursor']
    print("All users followed successfully.")
    
if __name__ == '__main__':
    t, user, maximum = Init()
    #mute(t,user)
    main(t, user, maximum)
