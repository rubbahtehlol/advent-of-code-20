with open("./Julekalender/customs.txt", "r") as f:
    customs_dec = [line.strip() for line in f]

temp_set = set()
temp_lst = []
customs_groups = []
yes = []

for answer in customs_dec:
    if answer != "":
        for char in answer:
            temp_set.add(char)
        temp_lst.append(temp_set)
        temp_set = set()
    else:
        # check_set = temp_lst[0]
        # for group_set in temp_lst:
        #     check_set.union(group_set)

        x = set(temp_lst[0])
        for answer in temp_lst:
            temp = x.intersection(answer)
            x = temp
        count = len(temp)
        yes.append(count)
        temp_set = set()
        temp_lst = []
        # count += count
x = set(temp_lst[0])
for answer in temp_lst:
    y = x.intersection(answer)
count = len(temp)
yes.append(count)

num_total = 0
for num in yes:
    num_total = num + num_total


print(num_total)