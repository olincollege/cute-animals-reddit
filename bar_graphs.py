"""
Create a list of total upvotes and total comments for each animal and plots it
in a bar graph.

"""

import ast
import pandas as pd
import matplotlib.pyplot as plt

def find_totals():
    with open('data/animals_posts.txt', 'r',  encoding="utf8") as animals_id:
        animals_dict = ast.literal_eval(str(animals_id.read()))
    x_axis = []
    upvotes_total = []
    comments_total = []
    data_table = pd.read_fwf('data/general_data1.txt')
    for key in animals_dict.keys():
        if animals_dict[key] != []:
            x_axis.append(key)
            total_upvotes = 0
            total_comments = 0
            for post_id in animals_dict[key]:
                total_upvotes += int(data_table.loc[data_table['id'] == post_id]\
                    ['score'])
                total_comments += int(data_table.loc[data_table['id'] == post_id]\
                    ['num_comments'])
            upvotes_total.append(total_upvotes)
            comments_total.append(total_comments)
    return upvotes_total, comments_total, x_axis

upvotes_total, comments_total, x_axis = find_totals()
plt.figure()
upvote_graph = plt.subplot()
plt.bar(x_axis,upvotes_total, width = 0.8)
plt.title('Upvotes per Animal')
plt.xlabel('Animal')
plt.ylabel('Upvotes')
plt.setp(upvote_graph.get_xticklabels(), rotation=70)
plt.savefig('visualizations/upvotes.png')

plt.figure()
comment_graph = plt.subplot()
plt.bar(x_axis,comments_total, width = 0.8)
plt.title('Comments per Animal')
plt.xlabel('Animal')
plt.ylabel('Number of Comments')

plt.setp(comment_graph.get_xticklabels(), rotation=70)
plt.savefig('visualizations/comments.png')
