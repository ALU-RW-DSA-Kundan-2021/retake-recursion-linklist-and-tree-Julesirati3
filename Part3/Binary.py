tree = [None] * 10
 
 
def root(key):
    if tree[0] != None:
        print("root is available")
    else:
        tree[0] = key
 
 
def set_left(key, parent):
    if tree[parent] == None:
        print("It is not possible", (parent * 2) + 1, ", parent can't be found")
    else:
        tree[(parent * 2) + 1] = key
 
 
def set_right(key, parent):
    if tree[parent] == None:
        print("it is not possible", (parent * 2) + 2, ", parent can't be found")
    else:
        tree[(parent * 2) + 2] = key
 
 
def print_tree():
    for i in range(10):
        if tree[i] != None:
            print(tree[i], end="")
        else:
            print("-", end="")
    print()
 
 
# Driver Code
root('A')
set_right('W', 0)
set_left('D', 1)
set_right('E', 1)
set_right('A', 2)
print_tree()
