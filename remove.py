# -*- coding: utf-8 -*-

from twitter import *
from time import sleep
import random

def Init():
    token = "3324372194-Vp2CFzyLxXgiTifG5EAvhbUBh0CkUZVYV9KboVY"
    token_secret = "kCFAIRyla7UtGlX01jyjAXxVilx9DaqFwwYqZ3psF7CPA"
    consumer_key = "iFhgBRALkDgJFpCJRBijMXhRb"
    consumer_secret = "KNk5OS6fqA3ZOip8uNeuGNeGQ3sVYBJNREhPbunLWR5JJ2WQjl"
    
    #premise
    user_name = input("Please enter username: \n")
    maximum = int(input("Please enter the  number of user you want to follow(It can to follow until 1000 users now): \n")) #maximum remove

    return Twitter(auth = OAuth(token, token_secret, consumer_key, consumer_secret)), user_name, maximum
        
def main(t, user, maximum):
    current = 0
    _cursor = -1
    _count = 200
    num = 0
    currentPage = 0
    maximumPage = 2 #400
    _list = list()

    while current < 7:
        #フォロワーのリスト 200 // 7*200= 1400 users
        friends = t.friends.list(screen_name= user, cursor=_cursor, count= _count)
        current += 1
        for friend in friends['users']:
            _list.append(friend['screen_name'])
            if len(_list) == 100:
                #friendships.lookup関数の引数は100までのため
                destroy(_list, num)
                _list = []
                continue
        _cursor = friends['next_cursor_str']

#        for x in _list:
#            try:

def destroy(_list, num):
    #片思いを自動でリムーブ
    tmp = _list.copy()
    ids = ','.join(tmp)
    connects = t.friendships.lookup(screen_name= ids) 
    for connect in connects:
        if "followed_by" in connect['connections']:
            pass
        else:
            t.friendships.destroy(screen_name= connect['screen_name'])
            num += 1
            print("{0:03d}: @".format(num) + connect['screen_name'] +" removed!")
            sleep(random.randint(3,5))

if __name__ == '__main__':
    t, user, maximum = Init()
    main(t, user, maximum)

