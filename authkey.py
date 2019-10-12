# -*- coding: utf-8 -*-
import os
import json
import sys
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import tweepy
from flask import Flask, session, redirect, render_template, request, make_response, jsonify
from os.path import join, dirname
from flask_cors import CORS,cross_origin
# --------------------------------------------------------------------------

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.secret_key = 'uuparupa'
# --------------------------------------------------------------------------

CONSUMER_KEY =''
CONSUMER_SECRET = ''
#CONSUMER_KEY = "0AFW5lNKgdMPdsauTp4iybggK"
#CONSUMER_SECRET = "4XBxUi8Nbhv4r6klEh63PbBmB8YOPMGRmrNuBr2O9ES9esZU8a"
# --------------------------------------------------------------------------# --------------------------------------------------------------------------
@app.route('/twitter_auth', methods=['GET'])
@cross_origin()
def twitter_auth():
    sys.stderr.write("*** twitter_auth***\n")
    sys.stderr.write(CONSUMER_KEY + "\n")
    sys.stderr.write(CONSUMER_SECRET + "\n")
    redirect_url = ""
    sys.stderr.write("*** twitter_auth *** ccc ***\n")
#
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    sys.stderr.write("*** twitter_auth *** ddd ***\n")

    try:
        redirect_url = auth.get_authorization_url()
        session['request_token'] = auth.request_token
    except Exception as ee:
#   except tweepy.TweepError, e:
        print("ERROR auth")
    sys.stderr.write("*** END AUTH ***\n")
 #   return redirect_url
    return redirect(redirect_url)
# --------------------------------------------------------------------------
def user_timeline():
    token = session.pop('request_token', None)
    verifier = request.args.get('oauth_verifier')
    if token is None or verifier is None:
        return False

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    # Access token, Access token secret を取得．
    auth.request_token = token
    print(token)
    try :
        auth.get_access_token(verifier)
    except Exception as ee:
#    logging.error(str(ee))
        return {}
    api = tweepy.API(auth)
    me = api.me()
    print('AT :' + auth.access_token)
    print('AS :' + auth.access_token_secret)
    print(me.id)
    print(me.screen_name)
    return "me.id"

@app.route('/')
@cross_origin()
def index():
    timeline = user_timeline()
    print(timeline)
    resp = "wei"
#    jsonob = json.loads(timeline)
  # resp.set_cookie('data', timeline, domain=".spmove-a5a1e.web.app")
    return resp

if __name__ == "__main__":
    sys.stderr.write('*** app start! ***\n')
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)