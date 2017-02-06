# -*- coding: utf-8 -*-

from twitter import *
from time import sleep
import random

def Init():
    token = ""
    token_secret = ""
    consumer_key = ""
    consumer_secret = ""
    
    #premise
    user_name = input("Please enter username: \n")
    maximum = int(input("Please enter the  number of user you want to follow(It can to follow until 1000 users now): \n")) #maximum follow

    return Twitter(auth = OAuth(token, token_secret, consumer_key, consumer_secret)), user_name, maximum

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
                    current += 1
                    print("{0:3d}: @".format(current)+follow['screen_name']+" Followed!")
                    if current >= maximum:
                        break
                    sleep(random.randint(2,4))
                except TwitterHTTPError:
                    pass
        if current >= maximum:
           break
        currentPage += 1
        _cursor=statusUpdate['next_cursor']
    print("All users followed successfully.")
    
if __name__ == '__main__':
    t, user, maximum = Init()
    main(t, user, maximum)
