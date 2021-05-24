from django.http import HttpResponse
import tweepy
import time
import json

# API CONFIG
configfile = open("config.json")
api = json.load(configfile)
BOT_USERNAME = api['BOT_USERNAME']
CONSUMER_KEY = api['CONSUMER_KEY']
CONSUMER_SECRET = api['CONSUMER_SECRET']
ACCESS_KEY = api['ACCESS_KEY']
ACCESS_SECRET = api['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

last_update_time = time.time()
first_time = True
html = ''

CACHE_SECONDS = 10

def generate_frontend():
    """
    generates html content for frontend
    html is only updated after CACHE_SECOND
    has passed thus reducing api requests
    :return: frontend html   
    """
    global last_update_time
    global first_time
    global html
    if time.time() - last_update_time > CACHE_SECONDS or first_time: # check if CACHE_SECONDS has passed to update site again
        first_time = False
        last_update_time = time.time()
        print('sending api request')
        timeline = api.mentions_timeline() # grabbing all bot mentions

        html = '''<html>
                    <head>
                        <title>''' + BOT_USERNAME + '''</title>
                        <style>
                            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100;300&display=swap');
                            .top {
                                font-size: 2em;
                                font-family:Roboto;
                                padding: 50px;
                                }
                        </style>
                    </head>
                    <body>
                        <center>
                            <div class="top">Mention <span style="color:#1b95e0">''' + BOT_USERNAME + '''</span> To Keep Your Tweets Here</div>'''

        for tweet in timeline:
            html += f'<blockquote class="twitter-tweet"><a href="https://twitter.com/x/status/{tweet.id}"></a></blockquote>'
        html += '<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script></center></body></html>'
        return html # return latest version
    else: 
        print('using cached')
        return html # return cached version

def index(request):
    html = generate_frontend()
    return HttpResponse(html)