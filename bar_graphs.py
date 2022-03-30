"""
Create a list of total upvotes and total comments for each animal and plots it
in a bar graph.

"""

import ast
import pandas as pd
import matplotlib.pyplot as plt

def find_totals():
    '''
    This function finds the total number of upvotes and comments for each
        animal in animal_list.csv

    Returns:
        upvotes_total: a list with the total number of upvotes for each animal
        comments_total: a list with the total number of comments for each
            animal
        x_axis: a list of all the animals with any upvotes or comments
    '''
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
                total_upvotes += int(data_table.loc[data_table['id']\
                     == post_id]['score'])
                total_comments += int(data_table.loc[data_table['id']\
                     == post_id]['num_comments'])
            upvotes_total.append(total_upvotes)
            comments_total.append(total_comments)
    return upvotes_total, comments_total, x_axis



upvotes_animals, comments_animals, animal_list = find_totals()
upvotes_sorted = pd.DataFrame({'x': animal_list, 'y': upvotes_animals})
upvotes_sorted = upvotes_sorted.sort_values('y')
upvotes_sorted = upvotes_sorted.iloc[::-1]
upvotes_sorted = pd.DataFrame(list(zip(upvotes_sorted['y'],\
     upvotes_sorted['x']))).set_index(1)

comments_sorted = pd.DataFrame({'x': animal_list, 'y':\
     comments_animals})
comments_sorted = comments_sorted.sort_values('y')
comments_sorted = comments_sorted.iloc[::-1]
comments_sorted = pd.DataFrame(list(zip(comments_sorted['y'],\
     comments_sorted['x']))).set_index(1)

plt.figure()
upvote_graph = plt.subplot()
upvotes_sorted.plot.bar(width = 0.8, align='center', legend =None,\
     figsize=(11, 9))
plt.title('Upvotes per Animal')
plt.xlabel('Animal')
plt.ylabel('Upvotes')
plt.setp(upvote_graph.get_xticklabels(), rotation=70)
plt.savefig('visualizations/upvotes.png')

plt.figure(figsize=(11, 9), dpi=80)
comment_graph = plt.subplot()
comments_sorted.plot.bar(width = 0.8, align='center', legend =None,\
     figsize=(11, 9))
plt.title('Comments per Animal')
plt.xlabel('Animal')
plt.ylabel('Number of Comments')

plt.setp(comment_graph.get_xticklabels(), rotation=70)
plt.savefig('visualizations/comments.png')
