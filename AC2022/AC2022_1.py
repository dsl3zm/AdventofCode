filename = 'input.txt'
with open(filename) as file:
    lines = file.readlines()
    length = len(lines)
    listnums = []
    i = 0
    temp = 0
    count = 0
    while True:
        if i > length - 1:
            break
        if lines[i] != '\n':
            temp += int(lines[i])
            i += 1
            print(f' -- checking line {i} on elf {count} who is currently carrying {temp} calories')
        else:
            count += 1
            listnums.append(temp)
            i += 1
            print(f'adding elf {count} who carrying {temp} calories')
            temp = 0

#pt1
# result = max(listnums)

#pt2
sorted = listnums.sort(reverse=True)
result = listnums[0] + listnums[1] + listnums[2]

print(f'The result is: {result}')
print(f'There were {len(listnums)} elves')