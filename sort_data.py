'''
Identifies which animals each post represents using the comments and titles
    and creates files containing which posts are with each animal and which
    animals are with each post
'''
import csv
import pandas as pd

def find_number_mentions(post_id, data_table):
    '''
    Takes in the id of a post and a data table, which must contain the
        title based on id and counts how many times each animal is
        mentioned.

    This function counts how many times each animal is mentioned in the comments
        based on the name of the animal and its alternate names.
    Args:
        post_id: A string that contains the id of a post
        data_table: A panda that contains data about the post,
                    such as title, upvotes and number of comments
    Returns:
        counts: A dictionary containing each animal and number of
                times it is mentioned in a post comments and title

    '''
    animals = {}
    initial_count = {}
    with open('animal_list.csv', encoding="utf8") as csvfile:
        animal_list = csv.reader(csvfile)
        for row in animal_list:
            while'' in row:
                row.remove('')
            initial_count[row[0]] = 0
            animals[row[0]] = row
        counts = initial_count
        with open(f'data/comments/{post_id}.txt', 'r', encoding="utf8")\
             as comments:
            titles = str(data_table[data_table['id']==post_id]['title'])
            for key, value in animals.items():
                for item in value:
                    titles = titles.lower()
                    counts[key] += titles.count(item)

            comments = comments.read()
            comments = comments.lower()
            for key, value in animals.items():
                for item in value:
                    counts[key] += comments.count(' '+ item)
        return counts
def find_which_animal(counts):
    '''
    Takes in a dictionary that has the number of times an animal is mentioned
        in a post's comments and titles and determines which animals the post
        is about
    Args:
        counts: a dictionary that has each animal as a key that has a value
                that represents how many times it is mentioned in a posts
                comments or title
    Returns:
        found_animals: a list that has the animal/animals that are in the post
    '''
    total = 0
    found_animals = []
    for key, _ in counts.items():
        total += counts[key]
    for key, _ in counts.items():
        if counts[key]/total > .3 and counts[key] > 5:
            found_animals.append(key)
    if not found_animals:
        return ['undefined']
    return found_animals

post_sorted = {}
animals_id = {}
data = pd.read_fwf('data/general_data1.txt')
with open('animal_list.csv', encoding="utf8") as list_animals:
    list_animals = csv.reader(list_animals)
    for animal_names in list_animals:
        while '' in animal_names :
            animal_names .remove('')
        animals_id[animal_names[0]] = []

for ids in data.id:
    count = find_number_mentions(ids, data)
    post_animal = find_which_animal(count)
    for animal in post_animal:
        if animal != 'undefined':
            animals_id[animal].append(ids)
    post_sorted[ids] = post_animal
with open('data/sorted_animals.txt', 'w', encoding="utf8") as sorted_animals:
    sorted_animals.write(str(post_sorted))
with open('data/animals_posts.txt', 'w', encoding="utf8") as animals_posts:
    animals_posts.write(str(animals_id))
