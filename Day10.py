with open("aoc10.txt","r") as f:
    raw_data=[line.rstrip() for line in f]

data=["noop" if value=="noop" else int(value.removeprefix("addx ")) for value in raw_data ]

cycle_with_x=[]
x_count=1
cycle_count=0

#this loop results in cycle_with_x containing tuples which display the value of x at the end of the cycle stated
for v in data:
    cycle_count+=1
    if v == "noop":
        cycle_with_x.append((cycle_count,x_count))
    else:
        cycle_with_x.append((cycle_count,x_count))
        x_count+=v
        cycle_count+=1
        cycle_with_x.append((cycle_count,x_count))

print(cycle_with_x)


every_20th=[]
for idx,v in enumerate(cycle_with_x):
    if v[0]%20==0:
        every_20th.append(cycle_with_x[idx-1])
print(every_20th)

every_20th_signals=[]
for v in every_20th:
    strength=(v[0]+1)*v[1]
    every_20th_signals.append(strength)

every_40_signals=[]
for idx,v in enumerate(every_20th_signals):
    if idx%2 == 0:
        every_40_signals.append(v)

print(sum(every_40_signals)) #this is the answer to part 1

#breaking data into chunks of 40 for part 2
chunked_list=[cycle_with_x[i:i + 40] for i in range(0, len(cycle_with_x), 40)]
print(chunked_list)

# def sprite_placement(chunk):
#     sprite_positioning=["." for i in range(len(chunk))]
#     print(sprite_positioning)
#     for i in chunk:
#         sprite_positioning[i[1]]="#"
#         sprite_positioning[(i[1]-1)]="#"
#         if i[1] < len(chunked_list):
#             sprite_positioning[(i[1]+1)]="#"
#     return sprite_positioning

# for i in chunked_list:
#     print(sprite_placement(i))

test_list=[(1, 1), (2, 2), (3, 2), (4, 2), (5, 31), (6, 31), (7, 7), (8, 7), (9, 11), (10, 11), (11, 14), (12, 14), (13, 12), (14, 12), (15, 15), (16, 15), (17, 16), (18, 16), (19, 21), (20, 21), (21, 24), (22, 24), (23, 22), (24, 22), (25, 24), (26, 24), (27, 24), (28, 24), (29, 31), (30, 31), (31, 31), (32, 31), (33, 31), (34, 36), (35, 36), (36, 37), (37, 37), (38, 37), (39, -1), (40, -1)]

sprite_positioning=["."for i in range(len(test_list))]
crt_count=1
crt=["." for value in range(len(test_list))]
for i in test_list:
    sprite_positioning[i[1]]="#"
    sprite_positioning[(i[1]-1)]="#"
    sprite_positioning[(i[1]+1)]="#"
    print(sprite_positioning)
    if sprite_positioning[crt_count]=="#":
        crt[crt_count]="#"
    if sprite_positioning[crt_count-1]=="#":
        crt[crt_count]="#"
    if sprite_positioning[crt_count+1]=="#":
        crt[crt_count]="#"
    crt_count+=1
#print(crt)



