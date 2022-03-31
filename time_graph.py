'''
This file creates the time graphs for the top 4 animals
    in r/aww.
'''
import ast
import datetime
import pandas as pd
import matplotlib.pyplot as plt


def organize_by_time(animal):
    '''
    Finds the total number of upvotes and comments for a specific
        animal for each year within the top 1000 posts in r/aww.
    Args:
        animal: a string that is an animal name.

    Returns:
        graph_year: a list that is all the years within the top 1000 posts.
        graph_upvotes: a list with total number of upvotes for each year
            for that animal.
        graph_comments: a list with the total number of comments for each year
            for that animal.
    '''
    upvotes_time = {}
    comments_time = {}
    data_table = pd.read_fwf('data/general_data1.txt')
    with open('data/animals_posts.txt', 'r',  encoding='utf8') as animals_id:
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
        if 2016 not in upvotes_time:
            upvotes_time[2016] = 0
            comments_time[2016] = 0
        if 2022 not in upvotes_time:
            upvotes_time[2022] = 0
            comments_time[2022] = 0
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

def get_total(top_animals):
    '''
    For a given list of animals, finds the total number of upvotes given
        to all specified animals for each year
    Args:
        top_animals: a list of strings that represents the top
            animals you want to visualize
    Returns:
        total_comments: a list of the total number of comments for all the
            sanimals pecified for each year
        total_upvotes: a list of the total number of upvotes for all the
            animals specified for each year
    '''
    for animal in top_animals:
        globals()[animal] = organize_by_time(animal)
    total_upvotes = []
    total_comments = []
    for index, _ in enumerate(globals()[top_animals[0]][0]):
        temp_total_upvotes = 0
        temp_total_comments = 0
        for animal in top_animals:
            temp_total_upvotes += globals()[animal][1][index]
            temp_total_comments+= globals()[animal][2][index]
        total_upvotes.append(temp_total_upvotes)
        total_comments.append(temp_total_comments)
    return total_comments, total_upvotes

def get_proportion(top_animals):
    '''
    Given a list of animals, finds the proportion of upvotes and
        comments each animal had compared to the others for each year.
    Args:
        top_animals: a list of strings that represents the top animals you want
            to find proportions for
    Returns:
        globals(): returns a dictionary with  global variables created
            within the function.
            Specifically, percentage_{animal}_upvotes returns a list of the
            proportion of how many upvotes that animal had during each year.
            percentage_{animal}_comments returns a list of the proportion of
            comments that animal had for each year.
    '''
    total_comments, total_upvotes = get_total(top_animals)
    for animal in top_animals:
        locals()[animal] = organize_by_time(animal)
    for animal in top_animals:
        var_name_upvotes = f'percentage_{animal}_upvotes'
        var_name_comments = f'percentage_{animal}_comments'
        globals()[var_name_upvotes] = [x/total_upvotes[index] for \
            index, x in enumerate(locals()[animal][1])]
        globals()[var_name_comments] = [x/total_comments[index] for \
            index, x in enumerate(locals()[animal][2])]
    return globals()

def time_graph_plot(top_animals):
    '''
    Plots a time graph for the proportion of upvotes and comments
        each animal had during each year
    Args:
        top_animals: a list of strings that represents the
            top animals you want to plot
    '''
    get_proportion(top_animals)
    #Graphs time plot for upvotes of the top 4 animals.
    plt.figure()
    plt.title('Time Graph of Upvotes Proportion on Top 1000 Posts')
    plt.xlabel('Year')
    plt.ylabel('Proportion of Upvotes')
    for animal in top_animals:
        plt.plot(organize_by_time(animal)[0],globals()\
            [f'percentage_{animal}_upvotes'], label= animal.capitalize())
    plt.legend()
    plt.savefig('visualizations/time_graph_upvotes.png')
    #Graphs time plot for comments of the top 4 animals.
    plt.figure()
    plt.title('Time Graph of Comment Proportion on Top 1000 Posts')
    plt.xlabel('Years')
    plt.ylabel('Proportion of Comments')
    for animal in top_animals:
        plt.plot(organize_by_time(animal)[0],globals()\
            [f'percentage_{animal}_comments'], label= animal.capitalize())
    plt.legend()
    plt.savefig('visualizations/time_graph_comments.png')

time_graph_plot(['dog', 'cat', 'human', 'bird'])
