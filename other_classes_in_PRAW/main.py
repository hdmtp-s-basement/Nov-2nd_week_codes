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


def sub_wiki(sub):
    topics = []
    for item in reddit.subreddit(sub).wiki:
        item = str(item)
        topic = (item[len(sub)+1:])
        print(topic)
        topics.append(topic)

    def sub_wiki_detail():
        for i in range(len(topics)):
            print(reddit.subreddit(sub).wiki[topics[i]].content_md)
            print("\n")
    sub_wiki_detail()


sub_wiki("programmerhumor")


