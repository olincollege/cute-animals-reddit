import csv
from itertools import count
import pandas as pd
import ast
import matplotlib.pyplot as plt

'''
with open("animal_list.csv") as csvfile:
        animal_count = {} 
        animal_list = csv.reader(csvfile)
        for row in animal_list:
            while('' in row):
                row.remove('')
            animal_count[row[0]] = 0
        sorted = pd.read_fwf('data/sorted_animals.txt')
        for animal in animal_count:
            for value in sorted:
                print(sorted[value])
                if animal in sorted[value]:
                    animal_count[animal] = animal_count[animal] + 1
        print(animal_count)
'''

with open('data/animals_posts.txt', 'r') as animals_id:
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
upvote_graph = plt.subplot()
plt.bar(x_axis,upvotes_total, width = 0.8)
plt.title('Upvotes per Animal')
plt.xlabel('Animal')
plt.ylabel('Upvotes')
plt.setp(upvote_graph.get_xticklabels(), rotation=70)
plt.savefig('visualizations/upvotes.png')

#This needs to be fixed
comment_graph = plt.subplot()
plt.bar(x_axis,comments_total, width = 0.8)
plt.title('Comments per Animal')
plt.xlabel('Animal')
plt.ylabel('Number of Comments')

plt.setp(upvote_graph.get_xticklabels(), rotation=70)
plt.savefig('visualizations/comments.png')