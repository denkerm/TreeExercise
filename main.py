
# A Node is either a Node or a Leaf.  If Leaf, it's just define as None in code
# else its a node struct
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
		# need some way to print each row - probably makes sense to do it as you go?

# this will let us use that previous row to create the next row, creating the children
# to be the correct value based on the index of the parent and the indexp of parent + or - 1 depending on if it's
# the left or right child.
def makeCurrentRow(cur_row):
	next_row = [];
	if (len(cur_row) == 0):
		return root = Node(1, None, None)

	else:
		x = 0;
		while x < len(cur_row):

			# sets up left child of current element and adds it to the next_row
			#could abstract out some of this in future if it makes sense
			left_value = cur_row[x]  # sets the value to the parent to start
			if (x > 0): # if there's a left neighbor of parent, add that to the value of left child
				left_value = cur_row[x] + cur_row[x - 1]	

			cur_row[x].l_child = Node(left_value, None, None) # updates the actual parent node to have that child
			next_row.append(cur_row[x].l_child)


			# sets up right child
			right_value = cur_row[x]  # sets the value to the parent to start
			if (x < len(cur_row - 1)): # if there's a right neighbor of parent, add that to the value of right child
				right_value = cur_row[x] + cur_row[x + 1]	

			cur_row[x].r_child = Node(right_value, None, None) # updates the actual parent node to have that child
			next_row.append(cur_row[x].r_child)


	return next_row;
		
