'''
Scrapes Reddit to get all the top level comments and other associated data
    from the top 1000 posts in /r/awww.
'''
import pandas as pd
from config import reddit

def get_data():
    '''
    This function finds the top 1000 posts in r/aww and
        finds information, such as number of upvotes,
        number of comments and date created, and puts
        all the top level comments for each post in a
        txt file.
    '''
    posts = []
    aww_subreddit = reddit.subreddit('aww')
    #Adds data on each post and writes it into a txt file.
    for post in aww_subreddit.top(limit=1000):
        posts.append([post.title, post.score, post.id, post.subreddit, \
            post.url, post.num_comments, post.selftext, post.created])
        submission = reddit.submission(id = str(post.id))
        submission.comments.replace_more(limit = 5)
        with open(f'data/comments/{post.id}.txt', 'w', encoding='utf8')\
             as post_comment:
            for top_level_comment in submission.comments:
                post_comment.write(str(top_level_comment.body) + '\n')

    posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit',\
        'url', 'num_comments', 'body', 'created'])
    posts = posts.to_string()
    with open('data/general_data1.txt', 'w', encoding='utf8') as general_data:
        general_data.write(str(posts))
get_data()
