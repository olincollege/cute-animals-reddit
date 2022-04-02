'''
Tests that functions in time_graph.py work properly.
'''

from time_graph import organize_by_time, get_total, get_proportion
def test_organize_by_time_one_post():
    '''
    Tests that given an animal with only one post, the data is sorted properly.
    '''

    assert (organize_by_time('dog', \
        'data/test_files/test_general_data_time_graph.txt', \
            'data/test_files/test_animals_posts.txt') == \
                ([2016, 2017, 2018, 2019, 2020, 2021, 2022],\
                     [0, 0, 0, 0, 100000, 0, 0], [0, 0, 0, 0, 1000, 0, 0]))
def test_organize_by_time_multiple_posts():
    '''
    Tests that given an animal with more than one post,
        the data is sorted properly.
    '''
    assert organize_by_time('cat', \
        'data/test_files/test_general_data_time_graph.txt',\
             'data/test_files/test_animals_posts_time_graph.txt') ==\
                  ([2016, 2017, 2018, 2019, 2020, 2021, 2022],\
                       [0, 0, 100000, 0, 0, 100000, 0],\
                            [0, 0, 2120, 0, 0, 2120, 0])

def test_organize_by_time_multiple_posts_same_time():
    '''
    Tests that given an animal with posts at the same time are added properly.
    '''
    assert organize_by_time('bird', \
        'data/test_files/test_general_data_time_graph.txt',\
             'data/test_files/test_animals_posts_time_graph.txt') == \
                 ([2016, 2017, 2018, 2019, 2020, 2021, 2022], \
                     [0, 0, 0, 200000, 0, 0, 0], [0, 0, 0, 4240, 0, 0, 0])

def test_get_total_one_animal():
    '''
    Checks that the total comments and upvotes is right when given
        just one animal.
    '''
    assert get_total(['dog'], \
        'data/test_files/test_general_data_time_graph.txt',\
             'data/test_files/test_animals_posts_time_graph.txt')\
              == ([0, 0, 0, 0, 1000, 0, 0], [0, 0, 0, 0, 100000, 0, 0])

def test_get_total_multiple_animals():
    '''
    Checks that the total comments and upvotes is right when given
        multiple animals.
    '''
    assert get_total(['dog', 'cat', 'bird'], \
        'data/test_files/test_general_data_time_graph.txt', \
            'data/test_files/test_animals_posts_time_graph.txt') \
                == ([0, 0, 2120, 4240, 1000, 2120, 0], \
                    [0, 0, 100000, 200000, 100000, 100000, 0])

def test_get_proportion_one_animal():
    '''
    Checks that when given one animal the proportion for every year is 1.0.
    '''
    #running this generates percentage_dog_upvotes and percentage_dog_comments
    upvotes_dict, comments_dict = get_proportion(['dog'], \
        'data/general_data1.txt', 'data/animals_posts.txt')
    assert  [upvotes_dict, comments_dict] == \
        [{'percentage_dog_upvotes': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}, {\
            'percentage_dog_comments': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}]
def test_get_proportions_multiple_animals():
    '''
    Tests that given multiple animals across different years it
     gives the correct proportions.
    '''
    assert get_proportion(['dog', 'cat', 'bird'], \
        'data/test_files/test_general_data_time_graph.txt', \
            'data/test_files/test_animals_posts_time_graph.txt') ==\
                 ({'percentage_dog_upvotes': [0.0, 0.0, 1.0, 0.0], \
                     'percentage_cat_upvotes': [1.0, 0.0, 0.0, 1.0], \
                         'percentage_bird_upvotes': [0.0, 1.0, 0.0, 0.0]}, \
                             {'percentage_dog_comments': [0.0, 0.0, 1.0, 0.0],\
                                  'percentage_cat_comments': \
                                      [1.0, 0.0, 0.0, 1.0], \
                                      'percentage_bird_comments': \
                                          [0.0, 1.0, 0.0, 0.0]})
