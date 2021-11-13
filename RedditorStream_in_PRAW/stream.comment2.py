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

def redditor_stream_comnts(user, duration=30):
    user = str(user)
    i = 0
    for comment in reddit.redditor(user).stream.comments():
        if comment is None:
            break
        print(comment.body)
        print("\n")
        i += 1
    print(i)
    
# redditor_stream_comnts("CamogapA113")
# redditor_stream_comnts("drdoge64")



subreddit = reddit.subreddit("hdmtp645466")
for comment in subreddit.stream.comments(pause_after=0):
    if comment is None:
        continue
    print(comment.body)