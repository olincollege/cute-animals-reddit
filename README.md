# Cute Reddit Animals on r/aww

## Requirements
Our code requires matplotlib, pandas, praw and wordcloud libraries to run correctly. Execute the folloiwng commands in the terminal to get those libraries.
```shell
pip install pandas
pip install matplotlib
pip install praw
pip install wordcloud
```
In order to get data from Reddit using praw, you must also create a config.py file in the following format:
```python
import praw

reddit = praw.Reddit(client_id='{YOUR_CLIENT_ID}', \
                     client_secret='{YOUR_CLIENT_SECRET}', \
                     user_agent='{YOUR_USER_AGENT}', \
                     username='{YOUR_REDDIT_USERNAME}', \
                     password='{YOUR_REDDIT_PASSWORD}')
```

## Summary

Our project aims to find the cutest animals in the r/aww subreddit by analyzing the top 1000 posts of all time and its comments on the subreddit. We create 3 visualizations to represent our data:
1. Bar graphs to show how many total upvotes and total comments each animal has in the top 1000 posts. This visualization is used to decide the top 4 animals. 
2. Word Clouds that show what words are frequently in the comments to describe the top 4 animals.
3. Linear Time graphs to show over the years what proportion of upvotes and comments the top 4 animals have.

## Instructions