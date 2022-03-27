from sort_data import find_which_animal, find_number_mentions
import pandas as pd

data_table = pd.read_fwf('data/general_data1.txt')
for id in data_table.id:
    counts = find_number_mentions(id)
    post_animal = find_which_animal(counts)
