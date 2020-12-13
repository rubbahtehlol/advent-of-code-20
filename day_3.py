with open("./Julekalender/airport.txt", "r") as f:
    # landing = f.read()

    inp = [line.rstrip() for line in f]

    # landing=landing.replace("\n", "")

    # landing = landing[0:121]
    

    # n = 11

    # # landing = [landing[i:i+n] for i in range(0, len(landing), n)]

    # print(landing)
    # rounds = 0
    # for index, value in enumerate(landing):
    def landing_loop(landing):
        for item in range(len(landing)):
            # if len(landing) == 11:
            #     return [item for item in landing]
        
            for num in range(11):
                lines = 0
                rounds = 0
                try:
                    x = landing[num] + landing[num]
                    # landing.pop(num+11)

                    landing[num] = x
                except:
                    break

                # return landing

            # print(landing[num])
            # if rounds == 10:
            #     rounds = 0
            #     lines = 0
            #     # print(landing)
            #     # landing_loop(landing)
            #     if len(landing) == 11:
            #         return [item for item in landing]

            # rounds = rounds + 1

    # while len(landing) < 11:
    # landing_loop(landing) 
    
    lst = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    l = len(inp)

    total = 1

    for steps in lst:
        i = 0
        n = 0
        c = 0
        while n < l:
            if i >= len(inp[n]):
                i -= len(inp[n])        
            if (inp[n][i] == "#"):
                c += 1
            i += steps[0]
            n += steps[1]
        total *= c

    print(f"Count: + {total}")
