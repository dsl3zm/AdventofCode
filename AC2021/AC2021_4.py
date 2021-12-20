#Solution to AdventofCode 2021 day 4

#given a matrix, loop through all 5x5 boards and return winning board number. returns -1 if no winner
# def find_winner(matrix, numboards):
    # print('find winner has been called')
    # print(str(matrix))
    # for i in range(numboards):
        #check horizontal
        # for j in range(5):
            # nummarked = 0
            # for k in range(5):
                # if int(matrix[5*i + j][k]) < 0:
                    # nummarked += 1
                # else:
                    # break
            # if nummarked == 5:
                # return i
        #check vertical
        # for j in range(5):
            # nummarked = 0
            # for k in range(5):
                # if int(matrix[5*i + k][j]) < 0:
                    # nummarked += 1
                # else:
                    # break
            # if nummarked == 5:
                # return i
    # return -1

# filename = 'input.txt'

# with open(filename) as file:
    #First line stores a list of numbers which are the entries.
    #one number is drawn at a time until a winner is found, at which point process stops
    #plan is to keep cycling through all the entries until a winner is found
    
    #store entry numbers
    # winningnums = []
    # first = True
    
    #store arrays into big fat 2d array
    # matrix = []
    # temp = [0 for i in range(5)]
    
    # numboards = 0 
    # i = 0
    # count = 0
    # for line in file:
        #read entry nums
        # if first:
            # for num in line.strip().split(","):
                # winningnums.append(num)
            # first = False
        #read 5x5 boards
        # else:
            # if len(line) > 1:
                # for num in line.split():
                    # temp[i] = num
                    # i += 1
                # matrix.append([])
                # for j in range(i):
                    # matrix[count].append(temp[j])
                # count += 1
                # i = 0
                # if count % 5 == 0 and count != 0:
                    # numboards += 1
                    
    # print(str(winningnums))
    # print('The matrix is as follows: ' + str(matrix))
    # print('num boards: ' + str(numboards))
    
    #iterate through numbers, marking five first time, and one each time after that. Call get winner after each iter
    # winner = False
    # winningboard = 0
    # first = True
    # numindex = 0
    # while winner != True:
        #if first iteration, mark first five numbers. Else, mark only one
        # if first:
            # firstnums = []
            # for i in range(5):
                # firstnums.append(winningnums[i])
            # numindex = 4
            # for i in range(numboards * 5):
                # for j in range(5):
                    # print('we are at iteration: ' + str(i) + ', ' + str(j))
                    # if firstnums.count(matrix[i][j]) > 0:
                        # print('we have a match: ' + str(matrix[i][j]))
                        # matrix[i][j] = -1
            #now check if winner
            # winningboard = find_winner(matrix, numboards)
            # if winningboard > 0:
                # winner = True
                # print('we have a winner! ' + str(winningboard))
            # first = False
        # else:
            # print('was not first. marking num: ' + winningnums[numindex])
            # for i in range(numboards * 5):
                # for j in range(5):
                    # if winningnums[numindex] == (matrix[i][j]):
                        # print('we have a match: ' + str(matrix[i][j]))
                        # matrix[i][j] = -1
            #check if winner
            # winningboard = find_winner(matrix, numboards)
            # if winningboard > 0:
                # winner = True
                # print('we have a winner! ' + str(winningboard) + ' with number ' + str(winningnums[numindex]))
            # else:
                # numindex += 1
    
    #now that we have a winner, time to calculate the score: 
    # scoresum = 0
    
    # for i in range(5):
        # for j in range(5):
            # if int(matrix[5*winningboard + i][j]) > 0:
                # scoresum += int(matrix[5* winningboard + i][j])
    # print('sum: ' + str(scoresum) + ', winning num: ' + winningnums[numindex])
    # result = 0
    # result += scoresum * int(winningnums[numindex])
    # print('the result is: ' + str(result))
    
    
def find_winner(matrix, numboards, listofwinners):
    print('find winner has been called')
    numwinners = 0
    print(str(matrix))
    for i in range(numboards):
        # check horizontal
        for j in range(5):
            nummarked = 0
            for k in range(5):
                if int(matrix[5*i + j][k]) < 0:
                    nummarked += 1
                else:
                    break
            if nummarked == 5:
                numwinners += 1
                if listofwinners.count(i) == 0:
                    listofwinners.append(i)
                break
        # check vertical
        for j in range(5):
            nummarked = 0
            for k in range(5):
                if int(matrix[5*i + k][j]) < 0:
                    nummarked += 1
                else:
                    break
            if nummarked == 5:
                numwinners += 1
                if listofwinners.count(i) == 0:
                    listofwinners.append(i)
                break
    return listofwinners

filename = 'input.txt'

with open(filename) as file:
    #First line stores a list of numbers which are the entries.
    # one number is drawn at a time until a winner is found, at which point process stops
    # plan is to keep cycling through all the entries until a winner is found
    
    # store entry numbers
    winningnums = []
    first = True
    
    # store arrays into big fat 2d array
    matrix = []
    temp = [0 for i in range(5)]
    
    numboards = 0 
    i = 0
    count = 0
    for line in file:
        # read entry nums
        if first:
            for num in line.strip().split(","):
                winningnums.append(num)
            first = False
        # read 5x5 boards
        else:
            if len(line) > 1:
                for num in line.split():
                    temp[i] = num
                    i += 1
                matrix.append([])
                for j in range(i):
                    matrix[count].append(temp[j])
                count += 1
                i = 0
                if count % 5 == 0 and count != 0:
                    numboards += 1
                    
    #print(str(winningnums))
    print('The matrix is as follows: ' + str(matrix))
    print('num boards: ' + str(numboards))
    
    #iterate through numbers, marking five first time, and one each time after that. Call get winner after each iter
    winner = False
    winningboard = 0
    first = True
    numindex = 0
    listofwinners = []
    while winner != True:
        # if first iteration, mark first five numbers. Else, mark only one
        if first:
            firstnums = []
            for i in range(5):
                firstnums.append(winningnums[i])
            numindex = 4
            for i in range(numboards * 5):
                for j in range(5):
                    print('we are at iteration: ' + str(i) + ', ' + str(j))
                    if firstnums.count(matrix[i][j]) > 0:
                        print('we have a match: ' + str(matrix[i][j]))
                        matrix[i][j] = -1
            #now check if winner
            listofwinners = find_winner(matrix, numboards, listofwinners)
            if winningboard > 0:
                winner = True
                print('we have a winner! ' + str(winningboard))
            first = False
        else:
            print('was not first. marking num: ' + winningnums[numindex])
            for i in range(numboards * 5):
                for j in range(5):
                    if winningnums[numindex] == (matrix[i][j]):
                        print('we have a match: ' + str(matrix[i][j]))
                        matrix[i][j] = -1
            #check if winner
            listofwinners = find_winner(matrix, numboards, listofwinners)
            if len(listofwinners) == numboards:
                winner = True
                winningboard = listofwinners[numboards - 1]
                print('we have a winner! ' + str(winningboard) + ' with number ' + str(winningnums[numindex]))
            else:
                numindex += 1
    
    #now that we have a winner, time to calculate the score: 
    scoresum = 0
    
    for i in range(5):
        for j in range(5):
            if int(matrix[5*winningboard + i][j]) > 0:
                scoresum += int(matrix[5* winningboard + i][j])
    print('sum: ' + str(scoresum) + ', winning num: ' + winningnums[numindex])
    result = 0
    result += scoresum * int(winningnums[numindex])
    print('the result is: ' + str(result))