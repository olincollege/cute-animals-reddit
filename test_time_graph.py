import ast
import datetime
import pandas as pd
import pytest
from time_graph import organize_by_time, get_total, get_proportion
def test_organize_by_time_one_post():
    '''
    Tests that given an animal with only one post, the data is sorted properly
    '''

    assert(organize_by_time('dog', 'data/test_file/test_general_data_time_graph.txt', 'data/test_file/test_animals_posts.txt') == ([2016, 2020, 2022], [0, 100000, 0], [0, 1000, 0]))

def test_organize_by_time_multiple_posts():
    '''
    Tests that given an animal with more than one post, the data is sorted properly
    '''
    assert(organize_by_time('cat', 'data/test_files/test_general_data_time_graph.txt', 'data/test_file/test_animals_posts.txt') == ([2016, 2018, 2021, 2022], [0, 100000, 100000, 0], [0, 2120, 2120, 0]))

def test_get_proportion_one_animal():
    '''
    Checks that when given one animal the proportion for every year is 1.0
    '''
    #running this generates percentage_dog_upvotes and percentage_dog_comments
    upvotes_dict, comments_dict = get_proportion(['dog'], 'data/general_data1.txt', 'data/animals_posts.txt')
    assert  [upvotes_dict, comments_dict] == [{'percentage_dog_upvotes': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}, {'percentage_dog_comments': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}]

#def test_get_proportion_one_animal_each_year():
    '''
    '''
#(get_proportion(['dog', 'cat', 'bird'], 'data/test_general_data.txt', 'data/test_animals_posts.txt'))


