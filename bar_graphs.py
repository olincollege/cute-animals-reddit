"""
Create a list of total upvotes and total comments for each animal and plots it
in a bar graph.

"""

import ast
import pandas as pd
import matplotlib.pyplot as plt

def find_totals(data_table, animal_sorted):
    '''
    This function finds the total number of upvotes and comments for each
        animal in animal_list.csv.
    Args:
        data_table: A panda with all the data about each post.
        animal_sorted: A string that has a path to a file with
            all the post ids sorted into animals.

    Returns:
        upvotes_total: A list with the total number of upvotes for each animal.
        comments_total: A list with the total number of comments for each
            animal.
        x_axis: A list of all the animals with any upvotes or comments.
    '''
    with open(animal_sorted, 'r',  encoding="utf8") as animals_id:
        animals_dict = ast.literal_eval(str(animals_id.read()))
    x_axis = []
    upvotes_total = []
    comments_total = []
    #For each animal, it adds it to x axis, and find the
    #total number of upvotes and comments.
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


def sort_graph(data, animal_list):
    '''
    Takes data and the x axis associated with it and sorts it in descending
        order.

    Args:
        data: A list with the total where the index is associated with
            an animal in animal_list.
        animal_list: A list with animals where each index is associated
            with a value in data.
    Returns:
        sorted_data: A panda with the sorted x axis and y axis in
             descending order.
    '''
    sorted_data = pd.DataFrame({'x': animal_list, 'y': data})
    sorted_data = sorted_data.sort_values('y')
    sorted_data = sorted_data.iloc[::-1]
    sorted_data = pd.DataFrame(list(zip(sorted_data['y'],\
        sorted_data['x']))).set_index(1)
    return sorted_data


def upvotes_bar_graph():
    """
    Plots and formats the upvotes bar graph. 
    """
    upvote_animals, comments_animals, list_animals = \
    find_totals(pd.read_fwf('data/general_data1.txt'), 'data/animals_posts.txt')
    upvotes_sorted = sort_graph(upvote_animals, list_animals)
    upvote_graph = plt.subplot()
    plt.close()
    upvotes_sorted.plot.bar(width = 0.8, align='center', legend =None,\
        figsize=(12,9))
    plt.title('Upvotes per Animal', fontsize = 35)
    plt.xlabel('Animal', fontsize = 25)
    plt.ylabel('Upvotes',fontsize = 25)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.ticklabel_format(axis="y", style="plain")
    plt.setp(upvote_graph.get_xticklabels(), rotation=70)
    plt.tight_layout()
    plt.savefig('visualizations/upvotes.png')
    plt.show()
def comments_bar_graph():
    """
    Plots and formats the comments bar graph. 
    """
    upvote_animals, comments_animals, list_animals = \
    find_totals(pd.read_fwf('data/general_data1.txt'), 'data/animals_posts.txt')
    comments_sorted = sort_graph(comments_animals, list_animals)
    comment_graph = plt.subplot()
    plt.close()
    comment_graph = comments_sorted.plot.bar(width = 0.8, align='center', legend =None,\
        figsize=(11, 9))
    plt.title('Comments per Animal',fontsize = 35)
    plt.xlabel('Animal',fontsize = 25)
    plt.ylabel('Number of Comments',fontsize = 25)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.setp(comment_graph.get_xticklabels(), rotation=70)
    plt.tight_layout()
    plt.savefig('visualizations/comments.png')
    plt.show()
comments_bar_graph()
upvotes_bar_graph()