import csv 
import pandas as pd

animals = {}
count = {}
data_table = pd.read_fwf('data/general_data1.txt')

with open("animal_list.csv") as csvfile:
    animal_list = csv.reader(csvfile)
    for row in animal_list:
        while('' in row):
            row.remove('')
        count[row[0]] = 0
        animals[row[0]] = row
        

with open(f"data/comments/ldwt5j.txt", "r") as f:
    title = (data_table[data_table['id']=="ldwt5j"]['title'])
    for key in animals.keys():
        for value in animals[key]:
            print(title.count(value))
            #count[key] += (title.count(value)*20)
    comments = f.read()
    comments = comments.lower()
    for key in animals.keys():
        for value in animals[key]:
            count[key] += comments.count(value)
print (count)


    


        
    