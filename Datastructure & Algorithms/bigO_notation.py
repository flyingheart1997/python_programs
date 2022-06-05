# # 1.
# # When time is increase by a linier way then the equation is:
# # time = a * n + b
# # Rule of Onotation is :
# #             1. keep the firsted growing term
# #             2. drop the constant
# # so the equation is : time = a * n
# # now the algorithmic complexcity is : O(n)
# # Example:
# def get_squared_n(n):
#     s_no = []
#     for i in n:
#         s_no.append(i * i)
#     return s_no
#
#
# result = get_squared_n([1, 2, 3, 4])
# print(result)

# -------------------xxxxxxxxxxxxxxxx--------------------------

# # 2.
# # When time is constant then the equation is:
# # time = a
# # Rule of Onotation is :
# #             1. keep the firsted growing term
# #             2. drop the constant
# # so the equation is(we can write as) : time = a * 1
# # now the algorithmic complexcity is : O(1)
# # Example:
# def find_first_pe(price, eps, index):
#     pe = price[index] / eps[index]
#     return pe
#
#
# result = find_first_pe([10, 20, 30, 40], [1, 2, 3, 4], 2)
# print(result)

# -------------------xxxxxxxxxxxxxxxx--------------------------

# # 3.
# # When iteration more then one or (n2) then time is increase by a linier way then the equation is:
# # time = a * n2 + b
# # Rule of Onotation is :
# #             1. keep the firsted growing term
# #             2. drop the constant
# # so the equation is(we can write as) : time = a * n2
# # now the algorithmic complexcity is : O(n2)
# # Example:
# def find_duplicate(n):
#     k = []
#     for i in range(len(n)):
#         for j in range(i+1, len(n)):
#             if n[i] == n[j]:
#                 k.append(n[i])
#     return k
#
#
# result = find_duplicate([1, 2, 3, 2, 4, 5, 6, 7, 8, 6, 9])
# print(result)

# -------------------xxxxxxxxxxxxxxxx--------------------------

# # 4.
# # When iteration more then one or (n2) and iteration (n) then time is increase by a linier way then the equation is:
# # time = a * n2 + b * n + c
# # Rule of Onotation is :
# #             1. keep the firsted growing term
# #             2. drop the constant
# # so the equation is(we can write as) : time = a * n2
# # now the algorithmic complexcity is : O(n2)
# # Example:
#
# n = [1, 2, 3, 2, 4, 5, 6, 7, 8, 6, 9]
# k = []
# c = []
# for i in range(len(n)):
#     for j in range(i+1, len(n)):
#         if n[i] == n[j] and n[i] not in k:
#             k.append(n[i])
# print(k)
# for i in range(len(n)):
#     if n[i] in k:
#         c.append(i)
# print(c)

# -------------------xxxxxxxxxxxxxxxx--------------------------
# Binary Search :-------
# Measuring running time growth:
# time complexcity:
# Measuring space growth:
# space complexcity:
# Example:
#     n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     search for 8
# so 1st iteration: n/2
# then 2nd iteration: (n/2)/2 = n/2^2 (n base 2 power of 2)
# then 3rd iteration: (n/2^2)/2 = n/2^3 (n base 2 power of 3)
# ..........so on...........
# iteration k: n/2^k
# we can write this as : 1 = n/2^k
# then n = 2^k => log2^n = log2^2^k (log n base 2)
#              => log2^n = k*log2^2
#              => k = log n => O(log n)
e = []


def search(n, a):
    d = int(len(n) / 2)
    e.append(d)
    print(n[d])
    if n[d] == a:
        print(f'Get the value ({a}) after:', len(e), 'iteration')
    if a > n[d]:
        c = n[d:]
        print(c)
        search(c, a)
    if a < n[d]:
        b = n[:d]
        print(b)
        search(b, a)


k = [*range(1, 10, 1)]
u = int(input('enter the no : '))
search(k, u)
