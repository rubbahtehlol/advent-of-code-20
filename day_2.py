with open("password_policy.txt", "r") as f:
    lst = f.read()

    lst = lst.split("\n")

    valid = 0       
    def find_colon():
        for index in range(len(item)):
            if ":" == item[index]:
                letter = item[index - 1]
                if index - 1 == 4:
                    x = item[0]
                    y = item[2]
                    position_x = 7 + int(x)
                    position_y = 7 + int(y)
                    check = item[7:]
                    if check.count(letter) >= int(x):
                        if check.count(letter) <= int(y):
                            return 1
                        else:
                            return 0
                    else:
                        return 0

                if index - 1 == 5:
                    x = item[0]
                    yx = item[2:4]
                    check = item[8:]
                    if check.count(letter) >= int(x):
                        if check.count(letter) <= int(yx):
                            return 1
                        else:
                            return 0
                    else:
                        return 0

                if index - 1 == 6:
                    xy = item[0:2]
                    yx = item[3:5]
                    check = item[9:]
                    if check.count(letter) >= int(xy):
                        if check.count(letter) <= int(yx):
                            return 1
                        else:
                            return 0
                    else:
                        return 0
               
    # for item in lst:
    #     valid = valid + find_colon()

    # print(valid)

    def find_pos():
        for index in range(len(item)):
            if ":" == item[index]:
                letter = item[index - 1]
                if index - 1 == 4:
                    x = item[0]
                    y = item[2]
                    position_x = 7 + int(x) - 1
                    position_y = 7 + int(y) - 1
                    if letter == item[position_x] or letter == item[position_y]:
                        if item[position_x] != item[position_y]:
                            return 1
                        else:
                            return 0
                    else:
                        return 0
  
                if index - 1 == 5:
                    x = item[0]
                    yx = item[2:4]
                    position_x = 8 + int(x) - 1
                    position_y = 8 + int(yx) - 1
                    if letter == item[position_x] or letter == item[position_y]:
                        if item[position_x] != item[position_y]:
                            return 1
                        else:
                            return 0
                    else:
                        return 0

                if index - 1 == 6:
                    xy = item[0:2]
                    yx = item[3:5]
                    position_x = 9 + int(xy) - 1
                    position_y = 9 + int(yx) - 1
                    if letter == item[position_x] or letter == item[position_y]:
                        if item[position_x] != item[position_y]:
                            return 1
                        else:
                            return 0
                    else:
                        return 0

    for item in lst:
        valid = valid + find_pos()

    print(valid)