import math

with open("aoc11.txt","r") as f:
    raw_data=[line.rstrip() for line in f]

data=[int((value.removeprefix("Monkey ")).removesuffix(":")) if value.startswith("M")==True else value for value in raw_data]
chunked_list=[data[i:i + 7] for i in range(0, len(data), 7)]

#removing trailing white space from list
for i in chunked_list:
    for idx,value in enumerate(i):
        if value=="":
            del i[idx]


monkeys={0:[[59, 74, 65, 86],"*",19,7,6,2,0],
         1:[[62, 84, 72, 91, 68, 78, 51],"+",1,2,2,0,0],
         2:[[78, 84, 96],"+",8,19,6,5,0],
         3:[[97, 86],"*","old",3,1,0,0],
         4:[[50],"+",6,13,3,1,0],
         5:[[73, 65, 69, 65, 51],"*",17,11,4,7,0],
         6:[[69, 82, 97, 93, 82, 84, 58, 63],"+",5,5,5,7,0],
         7:[[81, 78, 82, 76, 79, 80],"+",3,17,3,4,0]
}

for i in range(20):
    for i in range(len(monkeys)):
        monkey=i
        monkeys[monkey][6]+=len(monkeys[monkey][0])
        if monkeys[monkey][2]!="old":
            worry_levels=[value*monkeys[monkey][2] if monkeys[monkey][1]=="*" else value+monkeys[monkey][2] for value in monkeys[monkey][0]]
            for item in worry_levels:
                new_worry=item/monkeys[monkey][3]
                if float(new_worry).is_integer()==True:
                    monkeys[monkeys[monkey][4]][0].append(new_worry)
                else:
                    rounded_worry=math.floor(new_worry)
                    monkeys[monkeys[monkey][5]][0].append(rounded_worry)
            print(monkeys[monkey])
            monkeys[monkey][0]=[]
        else:
            worry_levels=[value*value for value in monkeys[monkey][0]]
            for item in worry_levels:
                new_worry=item/monkeys[monkey][3]
                if float(new_worry).is_integer()==True:
                    monkeys[monkeys[monkey][4]][0].append(new_worry)
                else:
                    rounded_worry=math.floor(new_worry)
                    monkeys[monkeys[monkey][5]][0].append(rounded_worry)
            print(monkeys[monkey])
            monkeys[monkey][0]=[]

for monkey in monkeys:
    print("The number of inspections is",monkeys[monkey][6])
print(186*185)


