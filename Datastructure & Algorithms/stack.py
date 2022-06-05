# Stack is a container of objects that are inserted and removed according to the last-in first-out (LIFO) principle.
# # Use case for stack:
# 1. Function callig in any programming language is managed using stack.
# 2. Undo (Ctrl+Z) functionality in any editor uses stack to track down last of operations
# # Push/Pop element: 0(1) it is constent time like, when get value using index like, k[1]
# # Search element by value: 0(n) is not perform on constent time, when get value using for loop like, for i in ___.
# Example of Stack in Python : list, collections.deque, queue.LifoQueue
# # Example ======>


class Stack:
    def __init__(self):
        self.s = []

    def store(self):
        n = int(input('How many times you want to store: '))
        for i in range(0, n):
            k = input('Enter, that you want to store: ')
            self.s.append(k)
        print(self.s)
        d = input('Do you want to store more elements (Y/N): ')
        if d == 'Y' or d == 'y':
            self.store()
        else:
            return

    def view_list(self):
        if len(self.s) == 0:
            print('No elements are in the list')
            return
        else:
            print('Your list is here', self.s)

    def peek(self):
        if len(self.s) == 0:
            print('No elements are in the list')
            return
        else:
            print(self.s)
        n = int(input('for peekinging an element enter valid index no: '))
        if n > len(self.s) or n <= 0:
            print('Index out of renge enter valid index.')
            return self.peek()
        else:
            k = self.s[n-1]
            print('your peeked :', k)

    def remove(self):
        if len(self.s) == 0:
            print('No elements are in the list')
            return
        else:
            print(self.s)
        n = int(input('for removing enter index no: '))
        if n > len(self.s) or n <= 0:
            print('Index out of renge enter valid index no.')
            return self.remove()
        else:
            k = []
            k.append(self.s[n-1])
            print(f'remove {k[0]} from the list')
            self.s.pop(n-1)

        print(self.s)

    def clear(self):
        if len(self.s) == 0:
            print('No elements are in the list')
            return
        else:
            print(self.s)
            n = input('Do you want to clear all the element (Y/N): ')
            if n == 'Y' or n == 'y':
                print('removing all the elements..')
                self.s.clear()
                print()
                print('Clear all the elements, now you have to ready for create a new Stack.')
            else:
                return


if __name__ == '__main__':
    j = Stack()
    while True:
        f = int(input('''
        1. store
        2. view_list
        3. peek
        4. remove
        5. clear
        6. exit
        Enter your value : '''))
        if f == 1:
            j.store()
        elif f == 2:
            j.view_list()
        elif f == 3:
            j.peek()
        elif f == 4:
            j.remove()
        elif f == 5:
            j.clear()
        elif f > 6:
            print('Enter a valid input')
        else:
            break
