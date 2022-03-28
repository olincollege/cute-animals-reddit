import datetime
import pandas as pd
import ast
import matplotlib.pyplot as plt


def organize_by_time(animal):
    upvotes_time = {}
    comments_time = {}
    data_table = pd.read_fwf('data/general_data1.txt')
    with open('data/animals_posts.txt', 'r',  encoding="utf8") as animals_id:
        animals_dict = ast.literal_eval(str(animals_id.read()))
    for post_id in animals_dict[animal]:
        timestamp = data_table.loc[data_table['id'] == post_id]\
                ['created']
        temp = datetime.datetime.fromtimestamp(float((timestamp)))
        time = temp.year
        if time not in upvotes_time.keys() and time not in comments_time.keys():
            upvotes_time[time] = 0
            comments_time[time] = 0
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



plt.plot(organize_by_time('dog')[0],organize_by_time('dog')[1], label= 'Dog')
plt.plot(organize_by_time('cat')[0],organize_by_time('cat')[1], label= 'Cat')
plt.plot(organize_by_time('human')[0],organize_by_time('human')[1], label= 'Human')
plt.legend()
plt.show()