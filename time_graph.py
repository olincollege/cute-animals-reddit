'''
This file creates the time graphs for the top 4 animals
    in r/aww.
'''
import ast
import datetime
import pandas as pd
import matplotlib.pyplot as plt


def organize_by_time(animal, table_path, sorted_post_path):
    '''
    Finds the total number of upvotes and comments for a specific
        animal for each year within the top 1000 posts in r/aww.
    Args:
        animal: a string that is an animal name.
        table_path: a string that is a path to a txt file with
            a table with information about each post
        sorted_post_path: a string that is the path to a txt file
            with all the posts categorized into animals
    Returns:
        graph_year: a list that is all the years within the top 1000 posts.
        graph_upvotes: a list with total number of upvotes for each year
            for that animal.
        graph_comments: a list with the total number of comments for each year
            for that animal.
    '''
    upvotes_time = {}
    comments_time = {}
    year_list = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
    data_table = pd.read_fwf(table_path)
    with open(sorted_post_path, 'r',  encoding='utf8') as animals_id:
        animals_dict = ast.literal_eval(str(animals_id.read()))
    for post_id in animals_dict[animal]:
        #Converts time stamp into date time.
        timestamp = data_table.loc[data_table['id'] == post_id]\
                ['created']
        temp = datetime.datetime.fromtimestamp(float((timestamp)))
        time = temp.year
        #Adds time.
        if time not in upvotes_time and time not in comments_time:
            upvotes_time[time] = 0
            comments_time[time] = 0
        for year in year_list:
            if year not in upvotes_time:
                upvotes_time[year] = 0
                comments_time[year] = 0
        upvotes_time[time] += int(data_table.loc[data_table['id'] == post_id]\
                ['score'])
        comments_time[time] += int(data_table.loc[data_table['id'] == post_id]\
                ['num_comments'])
    #Sorts upvotes and comments by year.
    upvote = sorted(upvotes_time.items())
    comments = sorted(comments_time.items())
    graph_year = [x[0] for x in upvote]
    graph_upvotes = [x[1] for x in upvote]
    graph_comments = [x[1] for x in comments]
    return graph_year, graph_upvotes, graph_comments

def get_total(top_animals, table_path, sorted_post_path):
    '''
    For a given list of animals, finds the total number of upvotes given
        to all specified animals for each year
    Args:
        top_animals: a list of strings that represents the top
            animals you want to visualize
        table_path: a string that is a path to a txt file with
            a table with information about each post
        sorted_post_path: a string that is the path to a txt file
            with all the posts categorized into animals
    Returns:
        total_comments: a list of the total number of comments for all the
            animals pecified for each year
        total_upvotes: a list of the total number of upvotes for all the
            animals specified for each year
    '''
    for animal in top_animals:
        locals()[animal] = organize_by_time(animal, table_path, sorted_post_path)
    total_upvotes = []
    total_comments = []
    for index, _ in enumerate(locals()[top_animals[0]][0]):
        temp_total_upvotes = 0
        temp_total_comments = 0
        for animal in top_animals:
            temp_total_upvotes += locals()[animal][1][index]
            temp_total_comments+= locals()[animal][2][index]
        total_upvotes.append(temp_total_upvotes)
        total_comments.append(temp_total_comments)
    return total_comments, total_upvotes

def get_proportion(top_animals, table_path, sorted_post_path):
    '''
    Given a list of animals, finds the proportion of upvotes and
        comments each animal had compared to the others for each year.
    Args:
        top_animals: a list of strings that represents the top animals you want
            to find proportions for
        table_path: a string that is a path to a txt file with
            a table with information about each post
        sorted_post_path: a string that is the path to a txt file
            with all the posts categorized into animals
    Returns:
        upvotes_dictionary: a dictionary with all the proportions of upvotes for each animal
            for each year
        comments_dictionary: a dictionary with all the proportions of comments for each animal
            for each year
    '''
    upvotes_dictionary = {}
    comments_dictionary = {}
    total_comments, total_upvotes = get_total(top_animals, table_path, sorted_post_path)
    for animal in top_animals:
        locals()[animal] = organize_by_time(animal, table_path, sorted_post_path)
    for animal in top_animals:
        var_name_upvotes = f'percentage_{animal}_upvotes'
        var_name_comments = f'percentage_{animal}_comments'
        upvotes_dictionary[var_name_upvotes] = [x/total_upvotes[index] for \
            index, x in enumerate(locals()[animal][1]) if total_upvotes[index] != 0]
        comments_dictionary[var_name_comments] = [x/total_comments[index] for \
            index, x in enumerate(locals()[animal][2]) if total_upvotes[index] != 0]
    return upvotes_dictionary, comments_dictionary

def time_graph_plot(top_animals):
    '''
    Plots a time graph for the proportion of upvotes and comments
        each animal had during each year
    Args:
        top_animals: a list of strings that represents the
            top animals you want to plot
    '''
    upvotes_proportions, comments_proportions = get_proportion(top_animals, 'data/general_data1.txt', 'data/animals_posts.txt')
    #Graphs time plot for upvotes of the top 4 animals.
    plt.figure()
    plt.title('Time Graph of Upvotes Proportion on Top 1000 Posts')
    plt.xlabel('Year')
    plt.ylabel('Proportion of Upvotes')
    for animal in top_animals:
        plt.plot(organize_by_time(animal, 'data/general_data1.txt', 'data/animals_posts.txt')[0],upvotes_proportions\
            [f'percentage_{animal}_upvotes'], label= animal.capitalize())
    plt.legend()
    plt.savefig('visualizations/time_graph_upvotes.png')
    #Graphs time plot for comments of the top 4 animals.
    plt.figure()
    plt.title('Time Graph of Comment Proportion on Top 1000 Posts')
    plt.xlabel('Years')
    plt.ylabel('Proportion of Comments')
    for animal in top_animals:
        plt.plot(organize_by_time(animal, 'data/general_data1.txt', 'data/animals_posts.txt')[0],comments_proportions\
            [f'percentage_{animal}_comments'], label= animal.capitalize())
    plt.legend()
    plt.savefig('visualizations/time_graph_comments.png')

time_graph_plot(['dog', 'cat', 'human', 'bird'])
