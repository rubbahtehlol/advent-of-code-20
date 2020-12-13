customs_dec = ['rluz', 'zlwruq', "", 'zlur', 'rzu']


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
        # continue
        x = set(temp_lst[0])
        for answer in temp_lst:
            y = x.intersection(answer)
        count = len(y)
        yes.append(count)
        temp_set = set()
        temp_lst = []
        # count += count
x = set(temp_lst[0])
for answer in temp_lst:
    y = x.intersection(answer)
count = len(y)
yes.append(count)


# for group in customs_groups:


print(yes)