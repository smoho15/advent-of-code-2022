import pandas as pd

def shape_comparison(elf_move,my_move,outcome_list):
    if elf_move == "A":
        if my_move=="X":
            outcome_list.append(3)
        elif my_move=="Y":
            outcome_list.append(6)
        else:
            outcome_list.append(0)
    elif elf_move=="B":
        if my_move=="Y":
            outcome_list.append(3)
        elif my_move=="Z":
            outcome_list.append(6)
        else:
            outcome_list.append(0)
    else:
        if my_move=="Z":
            outcome_list.append(3)
        elif my_move=="X":
            outcome_list.append(6)
        else:
           outcome_list.append(0) 
    return outcome_list

def shape_comparison2(my_move,elf_move,outcome_list):
    if my_move == "X":
        if elf_move=="A":
            outcome_list.append(3)
        elif elf_move=="B":
            outcome_list.append(1)
        else:
            outcome_list.append(2)
    elif my_move=="Y":
        if elf_move=="A":
            outcome_list.append(1)
        elif elf_move=="B":
            outcome_list.append(2)
        else:
            outcome_list.append(3)
    else:
        if elf_move=="A":
            outcome_list.append(2)
        elif elf_move=="B":
            outcome_list.append(3)
        else:
           outcome_list.append(1) 
    return outcome_list

with open("aoc2.txt","r") as f:
    data=[line.rstrip() for line in f]

matches=[]
for i in data:
    single_elf=list(i)
    matches.append(single_elf)

df=pd.DataFrame(matches,columns=["ElfMove","Delete","MyMove"])
df=df.drop("Delete",axis=1)

# #calculating score based on move chosen
move_chosen_score=[]
for i in matches:
    if i[2]=="X":
        move_chosen_score.append(1)
    elif i[2]=="Y":
        move_chosen_score.append(2)
    else:
        move_chosen_score.append(3)
df["ShapeScore"]=move_chosen_score

#calculating score based on match outcome
outcome_score=[]
for match in matches:
    outcome_score=shape_comparison(match[0],match[2],outcome_score)

df["OutcomeScore"]=outcome_score

df["TotalMatchScore"]=df["ShapeScore"]+df["OutcomeScore"]

print(df.sum())

#question 2

df2=df
#calcuating score based on outcome
outcome_chosen_score=[]
for i in matches:
    if i[2]=="X":
        outcome_chosen_score.append(0)
    elif i[2]=="Y":
        outcome_chosen_score.append(3)
    else:
        outcome_chosen_score.append(6)    
df2["OutcomeScore"]=outcome_chosen_score

#calculating score based on shape chosen
second_shape_score=[]
for match in matches:
    second_shape_score=shape_comparison2(match[2],match[0],second_shape_score)
df2["ShapeScore"]=second_shape_score

df2["TotalMatchScore"]=df2["ShapeScore"]+df2["OutcomeScore"]

print(df2.sum())



