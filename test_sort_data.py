import pytest
import pandas as pd
from sort_data import find_number_mentions, find_which_animal, sort_posts

def test_find_number_mentions_only_dog():
    '''
    Tests that a test file with only dog mentions and dog title has the correct number of dog mentions
    '''

    assert(find_number_mentions('000001', pd.read_fwf('data/test_general_data.txt')) == {'dog': 10, 'rabbit': 0,\
        'bird': 0, 'cat': 0, 'hamster': 0, 'cow': 0, 'shrimp': 0, 'pig': 0, \
        'crab': 0, 'deer': 0, 'sheep': 0, 'fish': 0, 'squirrel': 0, 'panda': 0, 'mouse': 0,\
            'goat': 0, 'horse': 0, 'monkey': 0, 'koala': 0, 'mole': 0, 'giraffe': 0, 'camel': 0,\
                'starfish': 0, 'alligator': 0, 'bear': 0, 'coyote': 0, 'chimpanzee': 0, 'raccoon': 0,\
                        'crocodile': 0, 'dolphin': 0, 'elephant': 0, 'snake': 0, 'kangaroo': 0, 'hippopotamus': 0, \
                            'elk': 0, 'fox': 0, 'gorilla': 0, 'bat': 0, 'frog': 0, 'badger': 0, 'lizard': 0, 'hedgehog': 0,\
                                'otter': 0, 'reindeer': 0, 'seal': 0, 'octopus': 0, 'shark': 0, 'seahorse': 0, 'walrus': 0,\
                                    'whale': 0, 'jellyfish': 0, 'squid': 0, 'lobster': 0, 'clams': 0, 'seagull': 0, 'sea urchin': 0,\
                                        'sea anemone': 0, 'turtle': 0, 'sea lion': 0, 'human': 0, 'orangutans': 0, 'unidentified': 0})


def test_find_which_animal_only_dog():
    '''
    Tests that a count with only dogs correctly sorts the post as a dog
    '''
    assert(find_which_animal({'dog': 10, 'cat': 0}) == ['dog'])

def test_find_which_animal_cat_mixed():
    '''
    Tests that given a mixed count with a majority cat still sorts a post as cat
    '''
    assert(find_which_animal({'dog': 1, 'cat': 9}) == ['cat'])

def test_find_which_animal_two():
    '''
    Tests that when there are two animals in a post mentioned a lot both are outputted
    '''
    assert(find_which_animal({'dog': 9, 'cat': 9}) == ['dog', 'cat'])

def test_find_which_animal_undefined():
    '''
    Tests that when given less than 5 mentions of any animal the post is undefined
    '''
    assert(find_which_animal({'dog': 2, 'cat': 2}) == ['undefined'])
