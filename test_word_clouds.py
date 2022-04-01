import ast
from wordcloud import WordCloud
import pytest
from word_clouds import add_comments

def test_add_comments_dog():
    '''
    Tests that when given a singular file with just animals the comments are added properly
    '''
    assert(add_comments('dog', 'data/test_animals_posts.txt') == ' dog \n pupper \n lab \n wolf \n doggo \n doggie ')

def test_add_comments_multiple_files():
    '''
    Tests that when there a multiple files for an animal the comments are added properly
    '''
    assert(add_comments('cat', 'data/test_animals_posts.txt') == ' Cat\n kitty\n kittens\n dog\n rabbit\n cat\n cat\n cat\n kitty\n Kittens\n Cat\n cat\n I am raiyan siddique')