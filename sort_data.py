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
        based on the name of the animal and its alternate names. It also checks
        for variations by looking for keywords within words used to name an animal.
        
    Args:
        post_id: A string that contains the id of a post.
        data_table: A panda that contains data about the post,
                    such as title, upvotes and number of comments.
    Returns:
        counts: A dictionary containing each animal and number of
                times it is mentioned in a post comments and title.

    '''
    animals = {}
    initial_count = {}
    with open('animal_list.csv', encoding='utf8') as csvfile:
        animal_list = csv.reader(csvfile)
        #Creates a dictionary with all the animals as keys and remove empty
        # values.
        for row in animal_list:
            while'' in row:
                row.remove('')
            initial_count[row[0]] = 0
            animals[row[0]] = row
        #Read each file and make every character lowercase, then counts each
        #time an animal is mentioned in the title and comments.
        counts = initial_count
        with open(f'data/comments/{post_id}.txt', 'r', encoding='utf8')\
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
        is about.
    Args:
        counts: a dictionary that has each animal as a key that has a value
                that represents how many times it is mentioned in a posts
                comments or title.
    Returns:
        found_animals: a list that has the animal/animals that are in the post.
    '''
    total = 0
    found_animals = []
    for key, _ in counts.items():
        total += counts[key]
    for key, _ in counts.items():
        #Decided that threshold is 30% of all mentions and
        #must be mentioned 5 times.
        if counts[key]/total > .3 and counts[key] > 5:
            found_animals.append(key)
    if not found_animals:
        return ['undefined']
    return found_animals

def sort_posts(animal_csv):
    '''
    Takes in a csv where each row is all the potential names a pet
        can be called and sorts each post into which animal it is
    Args:
        animal_csv: a string that is the path for a csv file
            where each row is all the potential names an animal
            can be called.
    Returns:
        post_sorted: A dictionary where each key is an id and
            each value is a list of all the animals associated
            with the post.
        animals_id: A dictionary where each key is an animal
            and each value is a list of post ids that have that
            animal in it.
    '''
    post_sorted = {}
    animals_id = {}
    data = pd.read_fwf('data/general_data1.txt')
    with open(animal_csv, encoding='utf8') as list_animals:
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
    return post_sorted, animals_id
#Sorts all the posts based on our list of animal names
all_posts_sorted, all_ids_sorted = sort_posts('animal_list.csv')
with open('data/sorted_animals.txt', 'w', encoding='utf8') as sorted_animals:
    sorted_animals.write(str(all_posts_sorted))
with open('data/animals_posts.txt', 'w', encoding='utf8') as animals_posts:
    animals_posts.write(str(all_ids_sorted))
