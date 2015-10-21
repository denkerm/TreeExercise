
# define node struct
class Node(object):
    def __init__(self,value, l_child, r_child):
        self.l_child = l_child;
        self.r_child = r_child;

## If we work downwards, one row at a time, we can store the previous row as a list
## where the elements are in order left to right
def main(num_rows):
	cur_row = [] # a row of nodes - starts out empty
	while (num_rows > 0):
		cur_row = makeNextRow(cur_row); # Creates and returns the next row in the tree given the current row

# this will let us use that previous row to create the next row, creating the children
# to be the correct value based on the index of the parent and the indexp of parent + or - 1 depending on if it's
# the left or right child.
def makeCurrentRow(cur_row):
	next_row = [];
	if (len(cur_row) == 0):
		return 