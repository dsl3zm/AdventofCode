filename = 'input.txt'
with open(filename) as file:
    lines = file.readlines()
    length = len(lines)
    shared_characters = []
    
    for i in range(0, length - 1):
        total_contents = lines[i]
        print(f'Reading line: {i} as {total_contents}')
        median = len(total_contents)/2
        backpack_dictionary = []
        for j in range(len(total_contents)):
            if j < median:
                #less than half way, add initial dictionary contents
                if !(total_contents[j] in backpack_dictionary):
                    backpack_dictionary.append(total_contents[j])
            else:
                if total_contents[j] in backpack_dictionary:
                    shared_characters.append(total_contents[j])
                if
        

#pt1