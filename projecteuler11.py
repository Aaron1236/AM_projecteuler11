#PROJECT EULER 11. by Aaron McKeown (2/1/17)
#STATUS: COMPLETE
import methods

#calling on matrixstore to populate the list matrix
t = methods.methodstore
matrix = t.matrixstore('self')

#INITIALIZATIONS
position = [0,0]
direction_list = ['vertical', 'horizontal', 'positive_diagonal', 'negative_diagonal']
#variable to save the running highest product
winning = 0

"""
In the 20x 20 grid below, four numbers along a diagonal line have been marked in red.
The product of these numbers is 26x63x78x14 = 1788696

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20 x 20 grid?

PLAN
1.COMPLETE: place matrix txt file into nested array
2. create methods that will inspect four elements in a certain direction. up, down, left, right, diagonally positive, and diagonally negative. The methods will return the prdduct of the four numbers
3. create method that will return the next location to be inspected for any particular direction. an init (constructor) will be used when the object is initialized in order to determine the direction. the method will return the next number location t inspect. each time the object is called, it will return the 'next' location to inspect
    3a. loop through the entire matrix for each direction. if statement to compare and save the running highest product (winning)
"""

#loop through each direction
for n in direction_list:
    #framework for cycling through each position
    for p in range(20):
        for pp in range(20):
            position = [p,pp]
            temp = t.product_of_four(matrix, position, n)
            if  temp > winning:
                winning = temp
print('The answer is', winning)