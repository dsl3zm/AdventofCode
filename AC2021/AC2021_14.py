#Advent of Code 2021 day 14 solution

def str_append_list_join(s, n):
    l1 = []
    i = 0
    while i < n:
        l1.append(s)
        i += 1
    return ''.join(l1)

filename = "input.txt"

with open(filename) as file:
    #process input -- initial string, and insertion rules
    first = True
    inputstring = ""
    insertionrules = {}
    for line in file:
        line = line.strip()
        if first:
            inputstring = line
            first = False
        elif len(line) > 1:
            print(line)
            insertionrules[line[0:2]] = line[6]   
    print(f"The insertion rules are as follows: {insertionrules} ")
    
    #perform the ten steps to get final string
    print(f"template: {inputstring}")
    for i in range(40):
        temp = ""
        for j in range(len(inputstring) - 1):
            temp = temp + inputstring[j]
            temp = temp + insertionrules[inputstring[j:j+2]]
            if j == len(inputstring) - 2:
                temp = temp + inputstring[j + 1]
        inputstring = temp.upper()
        print(f"step {i + 1}")
        
    #cycle through the final string, calculating the frequencies. sort and subtract after.
    uniquechars = []
    frequencies = []    
    for i in range(len(inputstring)):
        
        exists = uniquechars.count(inputstring[i])
        if exists > 0:
            frequencies[uniquechars.index(inputstring[i])] += 1
        else:
            uniquechars.append(inputstring[i])
            frequencies.append(1)
         
    print(f"List of chars: {uniquechars} \nList of frequencies: {frequencies}")
    
    frequencies.sort()
    
    print(f"After sorting, the solution to largestfrequency - smallestfrequency is: {frequencies[len(frequencies) - 1] - frequencies[0]}")