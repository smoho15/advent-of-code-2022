from itertools import takewhile

with open("aoc7.txt","r") as f:
    data=[line.rstrip() for line in f]



folder_sizes={}
folder_path=[]
for line in data:
    commands = line.split()
    if commands[0] == "$":
        if commands[1] == "cd":
            if commands[2] == "..":
                folder_path = folder_path[:-1]
            elif commands[2] == "/":
                folder_path = ["/"]
            else:
                folder_path.append(commands[2])
    else:
        if commands[0] != "dir":
            current_path = ""
            for folder in folder_path:
                if current_path != "/" and folder != "/":
                    current_path += "/"
                current_path += folder
                folder_sizes[current_path] = folder_sizes.get(current_path, 0) + int(commands[0])

# print(folder_path)
# print(folder_sizes)


pathway=[]
pathway_with_size={}

for line in data:
    split_line=line.split()
    if split_line[0]=="$":
        if split_line[1] == "cd":
            if split_line[2]=="/":
                pathway = ["/"]
            elif split_line[2]=="..":
                pathway = pathway[:-1]
            else:
                pathway.append(split_line[2])
    else:
        if split_line[0] != "dir":
            current_folder=""
            print(split_line)
            for path in pathway:
                pathway_with_size[path]=int(split_line[0])
print(pathway)
print(pathway_with_size)

# small_folders=[folder[0] for folder in pathway_with_size if folder[0]<=100000]

# print(sum(small_folders))
# for paths in pathway_with_size:
#     if paths[0]<=100000
print(sum(value for name, value in folder_sizes.items() if value < 100000))