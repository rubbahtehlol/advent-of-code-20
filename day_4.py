with open("./Julekalender/passport.txt", "r") as f:
    # input = [line.rstrip() for line in f]
    input = f.readlines()

    data = []
    data_small = []

    for item in input:
        if item != "\n":
            x = item.split()
            data_small.extend(x)
        else:
            data.append(data_small)
            data_small = []

    data_dict = {}

    valid = 0
    persons = 0

    def validation(key, value):
        if key == "byr":
            value = int(value)
            if value >= 1920 and value <= 2002:
                return True
            else:
                print(f"invalid birth year {value}")
                return False

        if key == "iyr":
            value = int(value)
            if value >= 2010 and value <= 2020:
                return True
            else:
                print(f"invalid issued year {value}")
                return False

        if key == "eyr":
            value = int(value)
            if value >= 2020 and value <= 2030:
                return True
            else:
                print(f"invalid exp year {value}")
                return False

        if key == "hgt":
            if value[-2:] == "cm":
                value = int(value[:-2])
                if value >= 150 and value <= 193:
                    return True
                else:
                    print(f"invalid lenght {value}")
                    return False
            elif value[-2:] == "in":
                value = int(value[:-2])
                if value >= 59 and value <= 76:
                    return True
                else:
                    print(f"invalid lenght {value}")
                    return False
            else:
                print(f"invalid height {value}")
                return False
        
        if key == "hcl":
            if value[0] == "#" and len(value) == 7:
                x = 1
                while True:
                    for letter in value[1:-1]:
                        if x == 6:
                            return True
                        letters = "0123456789abcdef"
                        try:
                            letters.find(letter)
                            x += 1
                            continue
                        except:
                            print(f"invalid hcl_value {value}")
                            return False
            else:
                print(f"invalid hcl_value {value}")
                return False

        if key == "ecl":
            ecl_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if ecl_list.count(value):
                return True
            else:
                print(f"invalid color {value}")
                return False
        
        if key == "pid":
            if len(value) == 9:
                return True
            else:
                print(f"invalid passport ID {value}")
                return False


    for person in data:
        persons += 1
        data_keys = []
        for value in person:
            # for index, letter in enumerate(value):
            #     x, y = index, letter
            key = value[0:3]
            value = value[4:]

            data_dict.update([(key, value)])

            if key == "cid":
                continue
            else:
                if validation(key, value) == True:
                    data_keys.append(key)
                    continue
                else:
                    continue

        data_dict_keys = []
        for keys in data_dict.keys():
            if keys == "cid":
                continue
            else:
                data_dict_keys.append(keys)


        data_keys.sort()
        
        data_dict_keys.sort()

        if data_dict_keys == data_keys:
            valid += 1

    print(f"Number of passports: {persons}")
    print(f"Number of valid passports: {valid}")