import tweepy
from time import sleep

consumer_key=''
consumer_secret=''
access_token_key=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

def removetext(text):
    start = text.find( '@' )
    global result
    end = text.find( ':' )
    if start != -1 and end != -1:
        result = text[start+1:end]
    else:
        result = text
    return result

for status in api.home_timeline(count=1):
    print(status.text)
    mojityou = len(status.text)
    print(mojityou)
    Wan = mojityou //2
    Wan2 = mojityou % 2
    second = Wan + Wan2
    print(Wan)
    print(Wan2)
    global text
    text = status.text[second:]
    print(text)
sleep(5)
for status in api.home_timeline(count=1):
    print(status.text)
    mojityou = len(status.text)
    print(mojityou)
    Wan = mojityou //2
    Wan2 = mojityou % 2
    second = Wan + Wan2
    print(Wan)
    print(Wan2)
    global tex
    tex = status.text[:second]
    print(tex)
extt =text + tex
nextt = removetext(extt)
api.update_status(nextt)