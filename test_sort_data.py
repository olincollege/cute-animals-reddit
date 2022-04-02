'''
Tests that functions in sort_data.py work properly.
'''
import pandas as pd
from sort_data import find_number_mentions, find_which_animal, sort_posts

def test_find_number_mentions_only_dog():
    '''
    Tests that a test file with only dog mentions and dog title has
     the correct number of dog mentions.
    '''

    assert find_number_mentions('00000a', pd.read_fwf\
        ('data/test_files/test_general_data.txt')) == {'dog': 9, 'rabbit': 0,\
        'bird': 0, 'cat': 0, 'hamster': 0, 'cow': 0, 'shrimp': 0, 'pig': 0, \
        'crab': 0, 'deer': 0, 'sheep': 0, 'fish': 0, 'squirrel': 0, 'panda': 0\
        ,'mouse': 0, 'goat': 0, 'horse': 0, 'monkey': 0, 'koala': 0, \
        'mole': 0, 'giraffe': 0, 'camel': 0, 'starfish': 0, \
        'alligator': 0, 'bear': 0, 'coyote': 0, 'chimpanzee': 0,\
        'raccoon': 0,'crocodile': 0, 'dolphin': 0, 'elephant': 0,\
        'snake': 0, 'kangaroo': 0, 'hippopotamus': 0, \
        'elk': 0, 'fox': 0, 'gorilla': 0, 'bat': 0, 'frog': 0,\
        'badger': 0, 'lizard': 0, 'hedgehog': 0,'otter': 0, 'reindeer': 0,\
        'seal': 0, 'octopus': 0, 'shark': 0, 'seahorse': 0, 'walrus': 0,\
        'whale': 0, 'jellyfish': 0, 'squid': 0, 'lobster': 0, 'clams': 0,\
        'seagull': 0, 'sea urchin': 0,'sea anemone': 0, 'turtle': 0, \
            'sea lion': 0, 'human': 0, 'orangutans': 0, 'unidentified': 0}

def test_find_number_mentions_multiple_animals():
    '''
    Tests that a test file with mentions of more than one animal counts
     all the animals properly.
    '''
    assert find_number_mentions('00000b', \
        pd.read_fwf('data/test_files/test_general_data.txt')) == \
            {'dog': 1, 'rabbit': 1, 'bird': 0, 'cat': 6, 'hamster': 0,\
            'cow': 0, 'shrimp': 0, 'pig': 0, 'crab': 0, 'deer': 0,\
            'sheep': 0, 'fish': 0, 'squirrel': 0, 'panda': 0,\
            'mouse': 0, 'goat': 0, 'horse': 0, 'monkey': 0,\
            'koala': 0, 'mole': 0, 'giraffe': 0, 'camel': 0, \
            'starfish': 0, 'alligator': 0, 'bear': 0, 'coyote': 0, \
            'chimpanzee': 0, 'raccoon': 0, 'crocodile': 0, 'dolphin': 0, \
            'elephant': 0, 'snake': 0, 'kangaroo': 0, 'hippopotamus': 0, \
            'elk': 0, 'fox': 0, 'gorilla': 0, 'bat': 0, 'frog': 0, 'badger':\
            0, 'lizard': 0, 'hedgehog': 0, 'otter': 0, 'reindeer': 0, 'seal':\
           0,'octopus': 0, 'shark': 0, 'seahorse': 0, 'walrus': 0, 'whale': 0,\
           'jellyfish': 0, 'squid': 0, 'lobster': 0, 'clams': 0, 'seagull': 0,\
            'sea urchin': 0, 'sea anemone': 0, 'turtle': 0, 'sea lion': 0,\
            'human': 0, 'orangutans': 0, 'unidentified': 0}

def test_find_number_mentions_with_words():
    '''
    Tests that a test file with many non-animal words still
        counts animals correctly.
    '''
    assert find_number_mentions('00000c', \
        pd.read_fwf('data/test_files/test_general_data.txt')) \
            == {'dog': 2, 'rabbit': 0,\
        'bird': 7, 'cat': 1, 'hamster': 0, 'cow': 0, 'shrimp': 0, 'pig': 0,\
        'crab': 0, 'deer': 0, 'sheep': 0, 'fish': 0, 'squirrel': 0, \
        'panda': 0, 'mouse': 0, 'goat': 0, 'horse': 0, 'monkey': 0,\
        'koala': 0, 'mole': 0, 'giraffe': 0, 'camel': 0, 'starfish': 0,\
        'alligator': 0, 'bear': 0, 'coyote': 0, 'chimpanzee': 0,\
        'raccoon': 0, 'crocodile': 0, 'dolphin': 0, 'elephant': 0,\
        'snake': 0, 'kangaroo': 0, 'hippopotamus': 0, 'elk': 0,\
        'fox': 0, 'gorilla': 0, 'bat': 0, 'frog': 0, 'badger': 0,\
        'lizard': 0, 'hedgehog': 0, 'otter': 0, 'reindeer': 0,\
        'seal': 0, 'octopus': 0, 'shark': 0, 'seahorse': 0,\
        'walrus': 0, 'whale': 0, 'jellyfish': 0, 'squid': 0,\
        'lobster': 0, 'clams': 0, 'seagull': 0, 'sea urchin': 0,\
        'sea anemone': 0, 'turtle': 0, 'sea lion': 0, 'human': 0,\
        'orangutans': 0, 'unidentified': 0}
def test_find_which_animal_only_dog():
    '''
    Tests that a count with only dogs correctly sorts the post as a dog.
    '''
    assert find_which_animal({'dog': 10, 'cat': 0}) == ['dog']

def test_find_which_animal_cat_mixed():
    '''
    Tests that given a mixed count with a majority cat still sorts
         a post as cat.
    '''
    assert find_which_animal({'dog': 1, 'cat': 9}) == ['cat']

def test_find_which_animal_two():
    '''
    Tests that when there are two animals in a post mentioned a lot
        both are outputted.
    '''
    assert find_which_animal({'dog': 9, 'cat': 9}) == ['dog', 'cat']

def test_find_which_animal_undefined():
    '''
    Tests that when given less than 5 mentions of any animal the post is
        undefined.
    '''
    assert find_which_animal({'dog': 2, 'cat': 2}) == ['undefined']

def test_sort_posts():
    '''
    Tests overall sorting for the 3 test files.
    '''
    assert sort_posts('animal_list.csv', \
        pd.read_fwf('data/test_files/test_general_data.txt'))\
        == ({'00000a': ['dog'], '00000b': ['cat'], \
        '00000c': ['bird'], '00000d': ['cat']}, {'dog': \
        ['00000a'], 'rabbit': [], 'bird': ['00000c'], 'cat': \
        ['00000b', '00000d'], 'hamster': [], 'cow': [], 'shrimp': [], 'pig': \
        [], 'crab': [], 'deer': [], 'sheep': [], 'fish': [], 'squirrel':\
        [], 'panda': [], 'mouse': [], 'goat': [], 'horse': [], 'monkey': [],\
        'koala': [], 'mole': [], 'giraffe': [], 'camel': [], 'starfish': [], \
        'alligator': [], 'bear': [], 'coyote': [], 'chimpanzee': [], \
        'raccoon': [], 'crocodile': [], 'dolphin': [], 'elephant': [], \
        'snake': [], 'kangaroo': [], 'hippopotamus': [], 'elk': [], 'fox': \
        [], 'gorilla': [], 'bat': [], 'frog': [], 'badger': [], 'lizard': [],\
        'hedgehog': [], 'otter': [], 'reindeer': [], 'seal': [], 'octopus': [],\
        'shark': [], 'seahorse': [], 'walrus': [], 'whale': [], 'jellyfish':\
        [], 'squid': [], 'lobster': [], 'clams': [], 'seagull': [], \
        'sea urchin': [], 'sea anemone': [], 'turtle': [], 'sea lion':\
         [], 'human': [], 'orangutans': [], 'unidentified': []})
