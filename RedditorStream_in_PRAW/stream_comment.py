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
    stime = time.time()
    etime = 0
    user = str(user)
    i = 0
    for comment in reddit.redditor(user).stream.comments():
        if (etime >= duration):
            break
        print(comment.body)
        print("\n")
        etime += (int(time.time() - stime))
        i += 1
    print(i)
    
# redditor_stream_comnts("CamogapA113", 50)
redditor_stream_comnts("drdoge64",15)

'''
there's a bug in 28-33 line that blunts the purpose
of that loop by about 80%. It need to be resolved quickly.

EDIT: its unavoidable ¯\_(ツ)_/¯
'''