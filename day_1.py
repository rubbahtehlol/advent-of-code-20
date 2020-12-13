with open("1977.txt", "r") as f:

    entries_list = f.read()

    num_list = [int(s) for s in entries_list.split("\n")]

    answer = [x for x in num_list for y in num_list for z in num_list if x+y+z == 2020]

    print(answer)

    # def christmas(num_list):
    #     print(num_list)
    #     for num in num_list:
    #         num_1 = num
    #         for num in num_list:
    #             num_2 = num                   
    #             for num in num_list:
    #                 num_3 = num
    #                 if (num_1 + num_2 + num_3) == 2020:
    #                     print(f"{num_1} + {num_2} + {num_3}")
    #                     print(num_1*num_2*num_3)
    #                     return
    #                 else:
    #                     continue
    # christmas(num_list)
    

                



    # print(num_list)
