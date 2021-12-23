# Solution to advent of code 2021 day 3

filename = 'input.txt'

# with open(filename) as file: #increment loc. Negative means more 0, positive more 1.

    # frequency = [0 for i in range(12)]
    # for line in file:
        # i = 0
        # for bit in line.strip():
            # if bit == '0':
                # frequency[i] -= 1
            # else:
                # frequency[i] += 1
            # i += 1
                
    # gammarate = 0
    # epsirate = 0
    # j = 0
    
    # for i in range(11, -1, -1):
        # if frequency[i] > 0:
            # gammarate += 2 ** j
        # else:
            # epsirate += 2 ** j
        # j += 1
    
    # print(str(epsirate * gammarate))
    
with open(filename) as file:
    lines = file.readlines() 
    for line in lines:
        length = len(line.strip())
        break
    #find oxygenGen
    cont = True
    i = 0
    oxygenrate = ''
    co2rate = ''
    while cont: 
        freq = 0
        list0 = []
        list1 = []
        #loop over
        for line in lines:
            if line[i] == '1':
                freq += 1
                list1.append(line)
            else:
                freq -= 1
                list0.append(line)   
        if freq >= 0:
            lines = list1
        else:
            lines = list0
        i += 1
        if len(lines) == 1:
            oxygenrate = lines[0]
            cont = False
        
    #find co2Scru
    file.seek(0)
    lines = file.readlines()
    cont = True
    i = 0
    while cont: 
        freq = 0
        list0 = []
        list1 = []
        #loop over
        for line in lines:
            if line[i] == '1':
                freq += 1
                list1.append(line)
            else:
                freq -= 1
                list0.append(line)     
        if freq >= 0:
            lines = list0
        else:
            lines = list1
        i += 1
        if len(lines) == 1:
            co2rate = lines[0]
            cont = False
            
            
    #multiply the two numbers together
    c02 = 0
    oxy = 0
    for i in range(length):
        if co2rate[length - i - 1] == '1':
            c02 += 2 ** i
    for i in range(length):
        if oxygenrate[length - i - 1] == '1':
            oxy += 2 ** i
        
    print('co2 ' + str(c02) + ' oxy ' + str(oxy))
        
    print('result is: ' + str(c02 * oxy))