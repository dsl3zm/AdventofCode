filename = 'input.txt'
with open(filename) as file:
    lines = file.readlines() 
    listnums = []
    for i in range(len(lines) - 2):
        temp = 0
        for j in range(3):
            temp += int(lines[i + j])
            if j == 2:
                listnums.append(temp)
     
first = True
count = 0
for i in range (1, len(listnums)):
    print(str(listnums[i - 1]))
    if listnums[i - 1] < listnums[i]:
        count += 1;
print("The result is: " + str(count))