class Node:
      #constructor
    def __init__(self, d, nal, left=None, right=None, root=None):
        self.d = d
        self.Value = nal
        self.Left = left
        self.Right = right
        self.root = root
#function to che
    def hasLeftChild(self):
        return self.Left

    def hasRightChild(self):
        return self.Right

    def isLeftChild(self):
        return self.root and self.root.Left == self

    def isRightChild(self):
        return self.root and self.root.Right == self

    def isRoot(self):
        return not self.root

    def isLeafNode(self):
        return not (self.Right or self.Left)

    def hasAnyChildren(self):
        return self.Right or self.Left

    def hasBothChildren(self):
        return self.Right and self.Left


class BST:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, d, nal):
        if self.root:
            self._put(d, nal, self.root)
        else:
            self.root = Node(d, nal)
        self.size = self.size + 1

    def _put(self, d, nal, currentNode):
        if d < currentNode.d:
            if currentNode.hasLeftChild():
                self._put(d, nal, currentNode.Left)
            else:
                currentNode.Left = Node(d, nal, root=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(d, nal, currentNode.Right)
            else:
                currentNode.Right = Node(d, nal, root=currentNode)

    def __setitem__(self, m, n):
        self.put(m, n)

    def get(self, d):
        if self.root:
            res = self._get(d, self.root)
            if res:

                return res.Value
            else:
                return None
        else:
            return None

    def _get(self, d, currentNode):

        if not currentNode:
            return None
        elif currentNode.d == d:
            return currentNode
        elif d < currentNode.d:
            return self._get(d, currentNode.Left)
        else:
            return self._get(d, currentNode.Right)

    def __getitem__(self, d):
        return self.get(d)

    def __contains__(self, d):
        if self._get(d, self.root):
            return True
        else:
            return False

    def delete(self, d):

        if self.size > 1:

            nodeToRemone = self._get(d, self.root)
            if nodeToRemone:
                self.remone(nodeToRemone)
                self.size = self.size - 1
            else:
                raise KeyError('Error, d not in tree')
        elif self.size == 1 and self.root.d == d:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, d not in tree')

    def __deleteitem__(self, d):

        self.delete(d)

    def splice(self):
        if self.isLeafNode():
            if self.isLeftChild():

                self.root.Left = None
            else:
                self.root.Right = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():

                if self.isLeftChild():

                    self.root.Left = self.Left
                else:

                    self.root.Right = self.Left
                    self.Left.root = self.root
        else:

            if self.isLeftChild():

                self.root.Left = self.Right
            else:
                self.root.Right = self.Right
                self.Right.root = self.root

    def find(self):

        succ = None
        if self.hasRightChild():
            succ = self.Right.findMin()
        else:
            if self.root:

                if self.isLeftChild():

                    succ = self.root
                else:
                    self.root.Right = None
                    succ = self.root.findSuccessor()
                    self.root.Right = self
   

    def findMin(self):

        current = self
        while current.hasLeftChild():
            current = current.Left
        return current

    def remone(self, currentNode):

        if currentNode.isLeafNode():  # leaf
            if currentNode == currentNode.root.Left:
                currentNode.root.Left = None
            else:
                currentNode.root.Right = None
        elif currentNode.hasBothChildren():  # interior

            succ = currentNode.findSuccessor()
            succ.splice()
            currentNode.d = succ.d
            currentNode.Value = succ.Value

        else:  # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.Left.root = currentNode.root
                    currentNode.root.Left = currentNode.Left
                elif currentNode.isRightChild():
                    currentNode.Left.root = currentNode.root
                    currentNode.root.Right = currentNode.Left
                else:

                    currentNode.replaceNodeData(currentNode.Left.d,
                                                currentNode.Left.Value,
                                                currentNode.Left.Left,
                                                currentNode.Left.Right)
            else:

                if currentNode.isLeftChild():
                    currentNode.Right.root = currentNode.root
                    currentNode.root.Left = currentNode.Right
                elif currentNode.isRightChild():
                    currentNode.Right.root = currentNode.root
                    currentNode.root.Right = currentNode.Right
                else:
                    currentNode.replaceNodeData(currentNode.Right.d,currentNode.Right.Value,
                                                currentNode.Right.Left,
                                                currentNode.Right.Right)

  

tree = BST()
tree[3] = "Amagi"
tree[4] = "Umwembe"
tree[6] = "Imboga"
tree[2] = "nyanya"
tree[8] = "Imbwija"

print(tree[2])
print(tree[4])
print(tree[8])
