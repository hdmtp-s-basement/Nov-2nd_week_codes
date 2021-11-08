import praw
import os
from os.path import join, dirname
from dotenv import load_dotenv

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
'''
for comment in authenticate().subreddit("iama").stream.comments():
    # print(comment)
    pass
'''

subreddit = reddit.subreddit("programmerhumor")
for comment in subreddit.stream.comments(skip_existing=True):
    # print(comment)
    # print(comment.author)
    print("\n"+comment.body)
    # pass

'''
for submission in reddit.subreddit("memes").stream.submissions():
    # print(submission)
    print("\n"+submission.title)

'''