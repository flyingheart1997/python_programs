
# Binary search tree or BST. Every node has at most 2 child nodes.
# In Binary search tree every left node is small then parent node and every right node is greater then parent node.
# Every iteration we reduce search space by 1/2
# lenngth of list = 8    8-> 4-> 2-> 1
# 3 iterations
# log2^8
# search complexcity is = 0(log n)
# insert complexcity is = 0(log n)
# insert complexcity is = 0(log n)

# in Binary tree iteration have two way :
#       1. Breadth first search.
#       2. Depth first search.
#            a. in order traversal ==> in this case 1st visit left sub tree then root then right sub tree.
#               Ex==>[7,12,14,15,20 23,27,88], here 15 is root.
#            b. pre order traversal ==> in this case 1st visit root then left sub tree then right sub tree.
#               Ex==>[15,12,7,14,27,20,23,88], here 15 is root.
#            c. post order traversal ==> in this case 1st visit left sub tree then right sub tree then root.
#               Ex==>[7,14,12,23,20,88,27,15], here 15 is root.

# # Example ==>

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  # node already exist
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traval(self):
        elements = []
        # visit left sub_tree
        if self.left:
            left_elements = self.left.in_order_traval()
            elements += left_elements
        elements.append(self.data)
        # visit right sub_tree
        if self.right:
            right_elements = self.right.in_order_traval()
            elements += right_elements
        return elements

    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def remove(self, value):
        if value < self.data:
            if self.left:
                self.left.remove(value)

        elif value > self.data:
            if self.right:
                self.right.remove(value)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.remove(min_val)
        return self

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()


def build_tree(element):
    print('Building tree with:', element)
    root = BinarySearchTree(element[0])
    for i in range(1, len(element)):
        root.add_child(element[i])
    return root


if __name__ == '__main__':
    # n = [15, 12, 7, 14, 27, 20, 23, 88]
    # n = [17, 4, 1, 20, 9, 23, 18, 34]
    n = [2, 0, 1, 0, 2]
    roott = build_tree(n)
    print(roott.in_order_traval())
    # print(roott.search(27))
    # roott.add_child(11)
    # print(roott.in_order_traval())
    # roott.remove(17)
    # print(roott.in_order_traval())
