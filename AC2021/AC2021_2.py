# Solution to advent of code 2021 day 2

filename = input("Welcome to the calculator. Please enter the filename containing your input and we will continue: ")

filename = 'input.txt'

# for line in map(str.rstrip, path):
    # print(line)
    
horizontal = 0
vertical = 0 # 1690020
aim = 0

with open(filename) as file:
    for line in file:
        words = line.split()
        change = int(words[1])
        if 'p' in words[0]: #move horizontally n units
            aim -= change
        elif 'f' in words[0]:
            vertical += aim * change
            horizontal += change
        else:
            aim += change
          

print("The result is: " + str(horizontal * vertical))