with open("aoc6.txt","r") as f:
    data=[line.rstrip() for line in f]

data="".join(data)
list_of_chars=[data[i] for i in range(len(data)-1)]

answer_positions=[]
complete_sets=[]
for idx,value in enumerate(list_of_chars):
    sublist=list_of_chars[idx-3:idx+1]
    subset=set(sublist)
    if len(subset)==len(sublist):
        complete_sets.append(sublist)
        answer_positions.append(idx)
print(answer_positions)

answer2_positions=[]
complete2_sets=[]
for idx,value in enumerate(list_of_chars):
    sublist=list_of_chars[idx-13:idx+1]
    subset=set(sublist)
    if len(subset)==len(sublist):
        complete2_sets.append(sublist)
        answer2_positions.append(idx)
print(answer2_positions)

#answer positions spits out all of the index positions, to find the actual answer look for the first position which is greater than the length of the subsets of interest ie 4 and 14, and add 1 to the value as index positions start from 0