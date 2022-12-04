#for question 1 if the length of the intersection set is the same as either set then that is a complete match
#for question 2 if the intersection set is not empty it means there has been at least one match
def common_section_finder(pair_of_ranges,question_number):
    duplicate_number=0
    for i in pair_of_ranges:
        set_a=set(i[0])
        set_b=set(i[1])
        common_sections=set_a.intersection(set_b)
        if question_number==1:
            if len(common_sections)==len(set_a):
                duplicate_number=duplicate_number+1
            elif len(common_sections)==len(set_b):
                duplicate_number=duplicate_number+1
        else:
            if common_sections != set():
                duplicate_number=duplicate_number+1
    return duplicate_number

with open("aoc4.txt","r") as f:
    data=[line.rstrip() for line in f]

#seperatingout sections so that we have a list of lists that contain the pairs
grouped_sections=[i.split(",")for i in data]

#creating list of tuples which contain two lists with each elves sections
fully_seperated_pairs=[]
for pair in grouped_sections:
    first_elf=pair[0].split("-")
    second_elf=pair[1].split("-")
    first_elf_full_range=[num for num in range(int(first_elf[0]),int(first_elf[1])+1)]
    second_elf_full_range=[num for num in range(int(second_elf[0]),int(second_elf[1])+1)]
    fully_seperated_pairs.append((first_elf_full_range,second_elf_full_range))

print("answer to question 1 is",common_section_finder(fully_seperated_pairs,1))
print("answer to question 2 is",common_section_finder(fully_seperated_pairs,2))