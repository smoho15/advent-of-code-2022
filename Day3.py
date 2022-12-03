def rucksack_splitter(rucksack_list):
    split_rucksacks=[]
    for i in rucksack_list:
        rucksack_length=len(i)
        split_point=int((rucksack_length/2))
        a=i[:split_point]
        b=i[split_point:]
        both_rucksack=(a,b)
        split_rucksacks.append(both_rucksack)
    return split_rucksacks

def common_item_finder(split_rucksack):
    common_items=[]
    for i in split_rucksack:
        item_a=i[0]
        item_b=i[1]
        list_a=[*item_a]
        list_b=[*item_b]
        set_a=set(list_a)
        set_b=set(list_b)
        common_item=set_a.intersection(set_b)
        common_item=list(common_item)
        common_items.append(common_item[0])
    return common_items

def common_badge_finder(elves):
    common_badges=[]
    for i in elves:
        item_a=i[0]
        item_b=i[1]
        item_c=i[2]
        list_a=[*item_a]
        list_b=[*item_b]
        list_c=[*item_c]
        set_a=set(list_a)
        set_b=set(list_b)
        set_c=set(list_c)
        common_item=set_a.intersection(set_b,set_c)
        common_item=list(common_item)
        common_badges.append(common_item[0])
    return common_badges

with open("aoc3.txt","r") as f:
    data=[line.rstrip() for line in f]

both_compartments=rucksack_splitter(data)
extra_items=common_item_finder(both_compartments)
print(extra_items)

extra_items_values_uppercase=[ord(letter)-38 for letter in extra_items if letter.isupper()==True]
extra_items_values_lowercase=[ord(letter)-96 for letter in extra_items if letter.isupper()==False]
print(extra_items_values_uppercase)
print(extra_items_values_lowercase)

answer=sum(extra_items_values_lowercase)+sum(extra_items_values_uppercase)
print(answer)

elf_sets = [data[idx:idx+3] for idx in range(0, len(data), 3)]
print(elf_sets)
badges=common_badge_finder(elf_sets)
print(badges)
badge_values_uppercase=[ord(letter)-38 for letter in badges if letter.isupper()==True]
badge_values_lowercase=[ord(letter)-96 for letter in extra_items if letter.isupper()==False]
q2answer=sum(badge_values_lowercase)+sum(badge_values_uppercase)
print(q2answer)