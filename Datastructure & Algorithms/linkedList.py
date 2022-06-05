# # Insert/Delete element at beginning = O(1)
# # Insert/Delete element at end = O(n)
# # Insert/Delete element at middle = O(n)
# # Linked list Traversal = O(n)
# # Accessing element by value = O(n)
#
# # Linked list has two main benefits over an array,
#           1. You don't need to preallocate space.
#           2. Insertion is easier.

# Example :

class Node:
    def __init__(self, data=None, next_data=None):  # Constractor
        self.data = data
        self.next = next_data


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self):  # Method
        data = int(input('Enter the value to insert at begining : '))
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self):  # Method
        data = int(input('Enter the value to insert at end : '))
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def insert_at(self):  # Method
        index = int(input('Enter the index number to insert a value in a specific position : '))
        data = int(input('Enter the value : '))
        if index < 0:
            raise Exception('Index no. out of range')
        if index > self.get_length():
            self.insert_at_end()
        if index == 0:
            self.insert_at_start()
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self):  # Method
        index = int(input('Enter the index number to remove a value in a specific position : '))
        if index < 0 or index > self.get_length():
            raise Exception('Index no. out of range')
        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr.next:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def display(self):
        itr = self.head
        linklist_str = ''
        while itr:
            suffix = ''
            if itr.next:
                suffix = '--->'
            linklist_str += str(itr.data) + suffix
            itr = itr.next
        print(linklist_str)


if __name__ == '__main__':
    root = LinkedList()
    root.insert_at_start()
    root.insert_at_start()
    root.insert_at_start()
    root.insert_at_end()
    root.insert_at_end()
    root.insert_at_end()
    root.insert_at()
    root.insert_at()
    root.insert_at()
    root.display()
    root.remove_at()
    root.display()
    # print(root.get_length())
