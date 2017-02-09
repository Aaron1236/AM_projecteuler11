class methodstore:

    def product_of_four(the_matrix, the_position, the_direction):
        #INITIALIZATIONS
        answer = 1
        #create list to store all the position variables
        if the_direction is 'vertical':
            position_list = [the_position, [the_position[0] + 1,the_position[1]], [the_position[0] + 2,the_position[1]], [the_position[0] + 3,the_position[1]]]
            #print(position_list)
        if the_direction is 'horizontal':
            position_list = [the_position, [the_position[0], the_position[1] + 1],[the_position[0], the_position[1] + 2], [the_position[0], the_position[1] + 3]]
            #print(position_list)
        if the_direction is 'positive_diagonal':
            position_list = [the_position, [the_position[0] - 1, the_position[1] + 1],[the_position[0] - 2, the_position[1] + 2], [the_position[0] - 3, the_position[1] + 3]]
            #print(position_list)
        if the_direction is 'negative_diagonal':
            position_list = [the_position, [the_position[0] + 1, the_position[1] + 1],[the_position[0] + 2, the_position[1] + 2], [the_position[0] + 3, the_position[1] + 3]]
            #print(position_list)

        #Check all values in position list. if any value is less than 0 or greater than 19, then return 0
        for e in range(len(position_list)):#for loop to run through rows of position_list
            for ee in range(len(position_list[0])):#for loop to run through columns of position_list
                if position_list[e][ee] > 19 or position_list[e][ee] < 0:#if x is greater than 19 or less than 0
                    return 0#return 0

        #collect the values of the numbers in the three adjacent positions
        for q in range(len(position_list)): #for each row in the position_list
            answer = answer * the_matrix[position_list[q][0]][position_list[q][1]]#find the matrix value of each position  # multiply the matrix value to a running product
        return answer #return the product of all four values

##################################

    def matrixstore(self):  # This method will extract the number matrix from matrix.txt and store all int values in a nested list
        """
        PLAN:
        #1a. open file and place content into string variable (text)

        #1.save location of all spaces and \n into a list
        #for loop through all characters in the matrix.txt file
            #if character is a space or \n
                #then save character location in a list (loc_list)
        #2. extract all numbers between spaces and \n and place into a nested list. convert to ints
        #for loop 1 to length of loc_list
            #extract string from locations n to n+1 of loc_list.
            #convert string to int
            #append to nested matrix list (matrix_list)
        #3. close file fr.close()

        """
        #INITIALIZATIONS
        j = 0
        jj = 0
        k = 0
        p = 0
        #matrix = [[0 for _ in range(20)] for _ in range(20)]
        matrix_temp = [[] for _ in range(20)]
        #print(matrix_temp)
        space_save = [] #saves location or all spaces and \n
        i = 0 # counter to track location of for loop inside matrix
        fr = open('matrix.txt', 'r')  # 1a. open file and place content into string variable (text)
        text = fr.read()
        # 1.save location of all spaces and \n into a list
        for x in text:# for x in range(len(text)+1)# for loop through all characters in the matrix.txt file
            if x is  ' ': # if character is a space or \n
                space_save.append(i)# then save character location in a list (loc_list)
            if x is '\n':
                space_save.append(i)
            i += 1
        # 2. extract all numbers between spaces and \n and place into a nested list. convert to ints
        for y in range(len(space_save)-1):# for loop 1 to length of loc_list
            matrix_temp[p].append(int(text[space_save[y]+1:space_save[y + 1]]))# extract string from locations n to n+1 of loc_list.
            k +=1
            if k is 20:
                p += 1
                k = 0
        #print(matrix_temp)
        return(matrix_temp)