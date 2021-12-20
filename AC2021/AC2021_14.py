#Advent of Code 2021 day 14 solution
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self, data):
        if self.data:
            if data < self.data
                

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
    
    #perform the ten steps, keeping track of frequencies
    for i in range(2):
        temp = ""
        for j in range(len(inputstring)):
            
        