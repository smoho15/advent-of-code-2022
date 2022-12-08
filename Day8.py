import pandas as pd
import numpy as np
from itertools import takewhile

with open("aoc8.txt","r") as f:
    raw_data=[line.rstrip() for line in f]

data=[[*value] for value in raw_data] #data in the format list of lists where each list is a row

flat_list = [int(item) for sublist in data for item in sublist] #data as one flat list

id_assignment=[*enumerate(flat_list)] #assigning each tree a unique id starting at 0

trees_with_ids = [id_assignment[i:i + 99] for i in range(0, len(id_assignment), 99)] #each sublist now contains a tuple of unique id plus tree height

df=pd.DataFrame(trees_with_ids)


#function for looking left and right along rows
def lrchecker(row,direction):
    tall_enough_trees=[]
    if direction == "l":
        for idx,tree in enumerate(row):
            taller_than_trees=[]
            previous_trees = row[:idx]
            for previous_tree in previous_trees:
                if tree[1] > previous_tree[1]:
                    taller_than_trees.append(tree)
            if len(taller_than_trees)==len(previous_trees):
                tall_enough_trees.append(tree)
    if direction == "r":
        reversed_row=row[::-1]  
        for idx,tree in enumerate(reversed_row):
            taller_than_trees=[]
            previous_trees = reversed_row[:idx]
            for previous_tree in previous_trees:
                if tree[1] > previous_tree[1]:
                    taller_than_trees.append(tree)
            if len(taller_than_trees)==len(previous_trees):
                tall_enough_trees.append(tree)
    return tall_enough_trees

big_tree_ids=[] #this is currently a list of all the (id,treesize) tuples from checking left, final answer will require this be unpacked into one big list and turned into set
for row in trees_with_ids:
    trees_from_left=lrchecker(row,"l")
    big_tree_ids.append(trees_from_left)

for row in trees_with_ids:
    trees_from_right=lrchecker(row,"r")
    big_tree_ids.append(trees_from_right)

for col in df:
    col_as_row=df[col].tolist()
    trees_from_top=lrchecker(col_as_row,"l")
    big_tree_ids.append(trees_from_top)

for col in df:
    col_as_row=df[col].tolist()
    trees_from_top=lrchecker(col_as_row,"r")
    big_tree_ids.append(trees_from_top)

flat_big_tree_ids = [item for sublist in big_tree_ids for item in sublist]
part1answer=len(set(flat_big_tree_ids))


#starting part 2 below this point
    
array_data=np.array(data)
array_data=array_data.astype("int")

def scenic_calc(row,column):
    tree=array_data[row,column]
    trees_before=array_data[row, :column]
    seen_trees_before=[]
    for i in trees_before[::-1]:
        if i <tree:
            seen_trees_before.append(i)
        elif i >=tree:
            seen_trees_before.append(i)
            break   
    number_of_trees_before=len(seen_trees_before)
    trees_up=array_data[:row,column]
    seen_trees_up=[]
    for i in trees_up[::-1]:
        if i <tree:
            seen_trees_up.append(i)
        elif i >=tree:
            seen_trees_up.append(i)
            break
    number_of_trees_up=len(seen_trees_up)
    trees_down=array_data[row+1:,column]
    seen_trees_down=[]
    for i in trees_down:
        if i <tree:
            seen_trees_down.append(i)
        elif i >=tree:
            seen_trees_down.append(i)
            break
    number_of_trees_down=len(seen_trees_down)
    trees_after=array_data[row, column+1:]
    seen_trees_after=[]
    for i in trees_after:
        if i <tree:
            seen_trees_after.append(i)
        elif i >=tree:
            seen_trees_after.append(i)
            break
    number_of_trees_after=len(seen_trees_after)
        # for i in seen_trees_after:
        #     summed_seen_trees_after.append(len(i))       
    return number_of_trees_after,number_of_trees_down,number_of_trees_before,number_of_trees_up

testlist=[]
for row in range(len(data)):
    for column in range(len(data)):
        q2test=scenic_calc(row,column)
        testlist.append(q2test)
print(testlist)

scenic_scores=[tree[0]*tree[1]*tree[2]*tree[3] for tree in testlist]
print((max(scenic_scores)))
