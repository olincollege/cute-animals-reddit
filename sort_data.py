import csv
import pandas as pd

def find_number_mentions(id, data_table):
    animals = {}
    initial_count = {}
    with open('animal_list.csv') as csvfile:
        animal_list = csv.reader(csvfile)
        for row in animal_list:
            while'' in row:
                row.remove('')
            initial_count[row[0]] = 0
            animals[row[0]] = row
                
        counts = initial_count
        with open(f'data/comments/{id}.txt', 'r') as f:
            titles = str(data_table[data_table['id']==id]['title'])
            for key in animals.keys():
                for value in animals[key]:
                    titles = titles.lower()
                    counts[key] += titles.count(value)

            comments = f.read()
            comments = comments.lower()
            for key in animals.keys():
                for value in animals[key]:
                    counts[key] += comments.count(' '+ value)
        f.close()
        return counts
def find_which_animal(counts):
    total = 0
    found_animals = []
    for key in counts.keys():
        total += counts[key]
    for key in counts.keys():
        if counts[key]/total > .3 and counts[key] > 5:
            found_animals.append(key)
    if found_animals == []:
        return ['undefined']
    return found_animals

post_sorted = {}
animals_id = {}
data_table = pd.read_fwf('data/general_data1.txt')
with open('animal_list.csv') as csvfile:
    animal_list = csv.reader(csvfile)
    for row in animal_list:
        while '' in row:
            row.remove('')
        animals_id[row[0]] = []

for post_id in data_table.id:
    counts = find_number_mentions(post_id, data_table)
    post_animal = find_which_animal(counts)
    for animal in post_animal:
        if animal != 'undefined':
            animals_id[animal].append(post_id)
    post_sorted[post_id] = post_animal
f = open(f'data/sorted_animals.txt', 'w')
f.write(str(post_sorted))
f.close()
f = open(f'data/animals_posts.txt', 'w')
f.write(str(animals_id))
f.close()
