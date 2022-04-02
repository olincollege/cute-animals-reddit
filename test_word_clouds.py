'''
Tests that functions in word_clouds.py work properly.
'''

from word_clouds import add_comments

def test_add_comments_dog():
    '''
    Tests that when given a singular file with just animals the
         comments are added properly.
    '''
    assert add_comments('dog', 'data/test_files/test_animals_posts.txt') ==\
         ' dog \n pupper \n lab \n wolf \n doggo \n doggie '

def test_add_comments_multiple_files():
    '''
    Tests that when there a multiple files for an animal the
        comments are added properly.
    '''
    assert add_comments('cat', 'data/test_files/test_animals_posts.txt')\
         == ''' Cat
 kitty
 kittens
 dog
 rabbit
 cat
 cat
 cat
 kitty
 Kittens
 Cat
 cat
 I am raiyan siddique'''