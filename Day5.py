with open("aoc5.txt","r") as f:
    data=[line.rstrip() for line in f]

starting_stacks=[
    ["[F]","[T]","[C]","[L]","[R]","[P]","[G]","[Q]"],
    ["[N]","[Q]","[H]","[W]","[R]","[F]","[S]","[J]"],
    ["[F]","[B]","[H]","[W]","[P]","[M]","[Q]"],
    ["[V]","[S]","[T]","[D]","[F]"],
    ["[Q]","[L]","[D]","[W]","[V]","[F]","[Z]"],
    ["[Z]","[C]","[L]","[S]"],
    ["[Z]","[B]","[M]","[V]","[D]","[F]"],
    ["[T]","[J]","[B]"],
    ["[Q]","[N]","[B]","[G]","[L]","[S]","[P]","[H]"]
]

#creating list of tuples where first value is count number and second value is list of stacks
stacks_with_count=[]
for count,value in enumerate(starting_stacks):
    stacks_with_count.append((count+1,value))

replace_dict={"move ":","," from ":""," to ":","}

instructions=[]
for line in data:
    new_line=line.replace("move ","").replace(" from ",",").replace(" to ",",")
    instructions.append(new_line)

final_instructions=[i.split(",")for i in instructions]

for move in final_instructions:
    for stack in stacks_with_count:
        if stack[0]==int(move[1]):
            crates_to_move=stack[1][len(stack[1])-(int(move[0])):]
            del stack[1][len(stack[1])-(int(move[0])):]
            for i in (crates_to_move):
                for stack in stacks_with_count:
                    if stack[0]==int(move[2]):
                        stack[1].append(i)

print(stacks_with_count)

for count,value in stacks_with_count:
    print(value[-1])

answer=[value[-1] for count,value in stacks_with_count]
print(answer)

#note that this is currently the solution for part two of the puzzle, the answer to part 1 just requires calling reversed on crates_to_move on line 35