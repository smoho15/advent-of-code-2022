with open("aoc1.txt","r") as f:
    data = [line.rstrip() for line in f]

#Question 1
elf_totals=[]
individual_elf=0

for value in data:
    if value == "":
        elf_totals.append(individual_elf)
        individual_elf=0      
    else:
        individual_elf=individual_elf+int(value) 

max_elf=max(elf_totals)
print("Elf carrying the most is carrying",max_elf,"calories")

#Question 2
top_three_elves=[]
elf_totals_copy=elf_totals
for i in range(3):
    top_three_elves.append(max(elf_totals_copy))
    elf_totals.remove(max(elf_totals_copy))

top_three_elves_total=sum(top_three_elves)
print("Three elves carrying the most are carrying",top_three_elves_total,"calories")