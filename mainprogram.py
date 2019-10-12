from flask import Flask
import json
from flask_cors import CORS
from flask import Flask, request, render_template
import random
import tweepy
from time import sleep



# -----------４文字
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth)
# -------------
# -------------TLから学ぶ
th = tweepy.OAuthHandler(consumer_key, consumer_secret)
th.set_access_token(access_token_key, access_token_secret)

ai = tweepy.API(th)
# ------------
app = Flask(__name__)
CORS(app)


def tweet(formoji, TL):
    print(formoji + " ::::: " + TL)
    api.update_status(formoji)
    ai.update_status(TL)


def removetext(text):
    start = text.find('@')
    global result
    end = text.find(':')
    if start != -1 and end != -1:
        result = text[start+1:end]
    else:
        result = text
    return result


def TLmanabu():
    for sta in ai.home_timeline(count=1):
        print(sta.text)
        mojityou = len(sta.text)
        print(mojityou)
        Wan = mojityou // 2
        Wan2 = mojityou % 2
        second = Wan + Wan2
        print(Wan)
        print(Wan2)
        global t
        t = sta.text[second:]
        print(t)
    return t
def TLmanabu2():
    for sta in ai.home_timeline(count=1):
        print(sta.text)
        mojityou = len(sta.text)
        print(mojityou)
        Wan = mojityou // 2
        Wan2 = mojityou % 2
        second = Wan + Wan2
        print(Wan)
        print(Wan2)
        global tex
        tex = sta.text[second:]
        print(tex)
    return tex
def TLmanabu3():
    for sta in ai.home_timeline(count=1):
        print(sta.text)
        mojityou = len(sta.text)
        print(mojityou)
        Wan = mojityou // 2
        Wan2 = mojityou % 2
#        second = Wan + Wan2
        print(Wan)
        print(Wan2)
        global ex
#        ex = sta.text[:second]
        ex = sta.text
        print(ex)
    return ex


@app.route('/', methods=['GET', 'POST'])
def index():
    # --------4文字
    a = random.randint(ord('あ'), ord('ん'))
    b = random.randint(ord('あ'), ord('ん'))
    c = random.randint(ord('あ'), ord('ん'))
    d = random.randint(ord('あ'), ord('ん'))
    text = chr(a) + chr(b) + chr(c) + chr(d)
    print(text)
    # -------------TL
  #  TL1 = TLmanabu()
  #  sleep(15)
  #  TL2 = TLmanabu2()
 #   sleep(15)
    TLplus = TLmanabu3()
#    TL3 = TL2 + TL1 + TLplus
    TL4 = removetext(TLplus)
    # ---------------
    tweet(text, TL4)
    return text


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=810)