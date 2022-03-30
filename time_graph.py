'''
This file creates the time graphs for the top 5 animals
    in r/aww.
'''
import ast
import datetime
import pandas as pd
import matplotlib.pyplot as plt


def organize_by_time(animal):
    '''
    Finds the total number of upvotes and comments for a specific
        animal for each year within the top 1000 posts in r/aww
    Args:
        animal: a string that is an animal name

    Returns:
        graph_year: a list that is all the years within the top 1000 posts
        graph_upvotes: a list with total number of upvotes for each year
            for that animal
        graph_comments: a list with the total number of comments for each year
            for that animal
    '''
    upvotes_time = {}
    comments_time = {}
    data_table = pd.read_fwf('data/general_data1.txt')
    with open('data/animals_posts.txt', 'r',  encoding='utf8') as animals_id:
        animals_dict = ast.literal_eval(str(animals_id.read()))
    for post_id in animals_dict[animal]:
        timestamp = data_table.loc[data_table['id'] == post_id]\
                ['created']
        temp = datetime.datetime.fromtimestamp(float((timestamp)))
        time = temp.year
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
    upvote = sorted(upvotes_time.items())
    comments = sorted(comments_time.items())
    graph_year = [x[0] for x in upvote]
    graph_upvotes = [x[1] for x in upvote]
    graph_comments = [x[1] for x in comments]
    return graph_year, graph_upvotes, graph_comments

dogs = organize_by_time('dog')
cats = organize_by_time('cat')
humans = organize_by_time('human')
birds = organize_by_time('bird')
total_upvotes = []
total_comments = []
for index, _ in enumerate(dogs[0]):
    total_upvotes.append(dogs[1][index] + cats[1][index] + \
        humans[1][index] + birds[1][index])
    total_comments.append(dogs[2][index] + cats[2][index] + \
        humans[2][index] + birds[2][index])

percentage_dogs_upvotes = [x/total_upvotes[index] for \
    index, x in enumerate(dogs[1])]
percentage_cats_upvotes = [x/total_upvotes[index] for \
    index, x in enumerate(cats[1])]
percentage_humans_upvotes = [x/total_upvotes[index] for \
    index, x in enumerate(humans[1])]
percentage_birds_upvotes = [x/total_upvotes[index] for \
    index, x in enumerate(birds[1])]

percentage_dogs_comments = [x/total_comments[index] for \
    index, x in enumerate(dogs[2])]
percentage_cats_comments = [x/total_comments[index] for \
    index, x in enumerate(cats[2])]
percentage_humans_comments = [x/total_comments[index] for \
    index, x in enumerate(humans[2])]
percentage_birds_comments = [x/total_comments[index] for \
    index, x in enumerate(birds[2])]

plt.figure()
plt.title('Time Graph of Upvotes Proportion on Top 1000 Posts')
plt.xlabel('Year')
plt.ylabel('Proportion of Upvotes')
plt.plot(organize_by_time('dog')[0],percentage_dogs_upvotes, label= 'Dog')
plt.plot(organize_by_time('cat')[0],percentage_cats_upvotes, label= 'Cat')
plt.plot(organize_by_time('human')[0],percentage_humans_upvotes, label= 'Human')
plt.plot(organize_by_time('bird')[0],percentage_birds_upvotes, label= 'Birds')
plt.legend()
plt.savefig('visualizations/time_graph_upvotes.png')

plt.figure()
plt.title('Time Graph of Comment Proportion on Top 1000 Posts')
plt.xlabel('Years')
plt.ylabel('Proportion of Comments')
plt.plot(organize_by_time('dog')[0],percentage_dogs_comments, label= 'Dog')
plt.plot(organize_by_time('cat')[0],percentage_cats_comments, label= 'Cat')
plt.plot(organize_by_time('human')[0],percentage_humans_comments,\
     label= 'Human')
plt.plot(organize_by_time('bird')[0],percentage_birds_comments, label= 'Birds')
plt.legend()
plt.savefig('visualizations/time_graph_comments.png')
