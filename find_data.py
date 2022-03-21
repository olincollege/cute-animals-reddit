import praw
from praw.models import MoreComments
import pandas as pd

from config import reddit

posts = []
aww_subreddit = reddit.subreddit('aww')
for post in aww_subreddit.top(limit=100):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
    submission = reddit.submission(id = str(post.id))
    submission.comments.replace_more(limit = 3)
    f = open(f'data/comments/{post.title}.txt', 'w')
    for top_level_comment in submission.comments:
        f.write(str(top_level_comment.body))
    f.close()

posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
f = open(f'data/general_data.txt', 'w')
f.write(str(posts))
f.close()