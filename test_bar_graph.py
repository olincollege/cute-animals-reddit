'''
Tests that functions in bar_graph.py work properly.
'''
import pandas as pd
from bar_graphs import find_totals, sort_graph

def test_find_totals():
    '''
    Tests that find_totals calculates the correct sums for upvotes and
        comments for each animal.
    '''
    assert (find_totals(pd.read_fwf('data/test_files/test_general_data.txt'),\
         'data/test_files/test_animals_posts.txt'))== ([100000, 100000, 200000]\
              ,[1000, 2120, 4240], ['dog', 'bird', 'cat'])
def test_sorted_graph_reverse_ordered():
    '''
    Tests that a data that is ordered in the opposite order is
        rearranged to descending order.
    '''
    test_pd = pd.DataFrame({'x': ['3', '2', '1'], 'y': [3, 2, 1]})
    test_pd  = pd.DataFrame(list(zip(test_pd['y'],\
        test_pd['x']))).set_index(1)
    assert test_pd.equals((sort_graph([1, 2, 3], ['1', '2', '3'])))
def test_sorted_graph_ordered():
    '''
    Tests that a data that is ordered stays the same.
    '''
    test_pd = pd.DataFrame({'x': ['3', '2', '1'], 'y': [3, 2, 1]})
    test_pd  = pd.DataFrame(list(zip(test_pd['y'],\
        test_pd['x']))).set_index(1)
    assert test_pd.equals((sort_graph([3, 2, 1], ['3', '2', '1'])))
def test_sorted_graph_disorganized():
    '''
    Tests that a data that is ordered stays the same.
    '''
    test_pd = pd.DataFrame({'x': ['3', '2', '1'], 'y': [3, 2, 1]})
    test_pd  = pd.DataFrame(list(zip(test_pd['y'],\
        test_pd['x']))).set_index(1)
    assert test_pd.equals((sort_graph([2, 3, 1], ['2', '3', '1'])))
