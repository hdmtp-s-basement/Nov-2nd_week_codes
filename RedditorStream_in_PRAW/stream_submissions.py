import praw
import os
from os.path import join, dirname
from dotenv import load_dotenv
import time

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def authenticate():
    reddit = praw.Reddit(
        # username=os.environ.get("username"),
        # password=os.environ.get("password"),
        client_id=os.environ.get("id"),
        client_secret=os.environ.get("secret"),
        user_agent='random bullshit go brrr..',
    )
    return reddit

reddit = authenticate()

print(reddit.read_only)

def redditor_stream_posts(user, duration=30):
    stime = time.time()
    etime = 0
    user = str(user)
    for submission in reddit.redditor(user).stream.submissions():
        if (etime >= duration):
            break
        print(submission.title)
        print("\n")
        etime += (int(time.time() - stime))
    
redditor_stream_posts("fish_fucker69",100)

