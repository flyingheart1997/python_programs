# # Look up by key is O(1) Average
# # Insertion/Deletion is O(1) Average
# # Example : Dictionary internally use HashTable in Python

# def get_ord(key):
#     sum_of = 0
#     for c in key:
#         sum_of += ord(c)
#     return sum_of % 10


# class HashTable:
#     def __init__(self):
#         self.Max = 10
#         self.arr = [None]*self.Max
#
#     def get_ord(self, key):
#         sum_of = 0
#         for c in key:
#             sum_of += ord(c)
#         return sum_of % self.Max
#
#     def __setitem__(self, key, value):
#         o = self.get_ord(key)
#         self.arr[o] = value
#
#     def __getitem__(self, key):
#         o = self.get_ord(key)
#         return self.arr[o]
#
#     def __delitem__(self, key):
#         o = self.get_ord(key)
#         self.arr[o] = None
#
#
# h = HashTable()
# h['march 6'] = 302
# print(h.arr)
# h['march 17'] = 320
# print(h.arr)
# h['march 11'] = 120
# print(h.arr)
# del h['march 11']
# print(h.arr)


# # Collision handling :
class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]

    def get_ord(self, key):
        sum_of = 0
        for c in key:
            sum_of += ord(c)
        return sum_of % self.Max

    def __setitem__(self, key, value):
        k = self.get_ord(key)
        found = False
        for i, element in enumerate(self.arr[k]):
            if len(element) == 2 and element[0] == key:
                self.arr[k][i] = (key, value)
                found = True
        if not found:
            self.arr[k].append((key, value))

    def getitem(self):
        key = input('enter your key: ')
        o = self.get_ord(key)
        for k in self.arr[o]:
            if k[0] == key:
                # return k[1]
                print(f"value of {key} is: ", k[1])

    def delitem(self):
        key = input("Enter your key: ")
        o = self.get_ord(key)
        for i, k in enumerate(self.arr[o]):
            if k[0] == key:
                print(f"Deleting {k} at arr of [{o}][{i}] Index")
                del self.arr[o][i]


#
h = HashTable()
print(h.arr)
h['march 6'] = 302
print(h.arr)
h['march 17'] = 320
print(h.arr)
h['march 11'] = 120
print(h.arr)
h.getitem()
h.delitem()
print(h.arr)
# h['march 6'] = 30
# print(h.arr)
