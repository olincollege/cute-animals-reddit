# Cute Reddit Animals on r/aww
## Authors: Raiyan Siddique and An Grocki
## Summary

Our project aims to find the cutest animals in the r/aww subreddit by analyzing the top 1000 posts of all time and its comments on the subreddit. We create 3 visualizations to represent our data:
1. Bar graphs to show how many total upvotes and total comments each animal has in the top 1000 posts. This visualization is used to decide the top 4 animals. 
2. Word Clouds that show what words are frequently used in the comments to describe the top 4 animals.
3. Linear Time graphs to show over the years what proportion of upvotes and comments the top 4 animals have.
## Requirements
Our code requires matplotlib, pandas, praw and wordcloud libraries to run correctly. Execute the following commands in the terminal to get those libraries.
```shell
pip install pandas
pip install matplotlib
pip install praw
pip install wordcloud
pip install datetime
```

## Instructions
1. In order to get data from Reddit using praw, you must also create a `config.py` file in the following format:
```python
import praw

reddit = praw.Reddit(client_id='{YOUR_CLIENT_ID}', \
                     client_secret='{YOUR_CLIENT_SECRET}', \
                     user_agent='{YOUR_USER_AGENT}', \
                     username='{YOUR_REDDIT_USERNAME}', \
                     password='{YOUR_REDDIT_PASSWORD}')
```
2. Once the config.py file is created run the `find_data.py` file to get the data for the top 1000 posts on /r/aww subreddit. 

Note: If you want to get more or less posts from the subreddit you change the limit in line 19 in `find_data.py`:
```python
    for post in aww_subreddit.top(limit=1000)
```

3. After getting the data, run the `sort_data.py` file to generate `animal_posts.txt` and `sorted_animals.txt`, which are used to help visualize the data.

4. There are 3 ways to visualize our data:

    1. In order to get the bar graphs for upvotes and comments, run the `bar_graphs.py` file, which generates the bar graphs and saves the files.

    2. In order to get the word clouds, run the `word_clouds.py` file to generate the word clouds for dogs, cats, humans and birds. If you want to generate a word cloud for a different animal just add this line to the bottom of the `word_clouds.py` file:
    ```python
    create_word_cloud(YOUR_ANIMAL_HERE)
    ```
    3. In order to generate the time graphs, run the `time_graph.py` file. If you want to generate a time graph with more animals change the line at the bottom of the file and add the animal name as a string.
    ```python
    time_graph_plot(['dog', 'cat', 'human', 'bird'])
    ```
    Note: If you are taking the data in the future or taking more data than 1000 posts, you may have to add to the `year_list` variable in the `organize_by_time` function in the `time_graph.py` For example:
    ```python
        year_list = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
    ```