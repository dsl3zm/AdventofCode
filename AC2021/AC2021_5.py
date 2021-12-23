# Solution to advent of code 2021 day 6

filename = 'input.txt'

# once zero, fish add one every 6 iterations.
# new fish added initially start at 8, then go to 6

with open(filename) as file:
    inputlength = 0
    lanternfishstore = []
    listfish = [0 for i in range(9)]
    for line in file:
        for num in line.strip().split(','):
            lanternfishstore.append(int(num))
        inputlength = len(lanternfishstore)
        for i in range(9):
            listfish[i] = lanternfishstore.count(i)
        
        for i in range(256):
            listfish2 = [0 for i in range(9)]
            for j in range(9):
                if j == 0:
                    inputlength += listfish[j]
                    listfish2[6] += listfish[j]
                    listfish2[8] += listfish[j]
                else:
                    listfish2[j - 1] += listfish[j]
            listfish = listfish2
                    
        print(str(lanternfishstore))
        print('initial number of lanternfish: ' + str(len(lanternfishstore)))

        print('The final number of lanternfish is: ' + str(inputlength))