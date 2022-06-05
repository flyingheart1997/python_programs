# 3 steps of recursion :
#     1. Divide big problem into small and simple problem,
#     2. Find a base condition with a simple ans,
#     3. Return and roll back answer for base condition to solve sub problem.
# # Simple Example :
# def find_sum():
#     s = 0
#     n = int(input('enter no: '))
#     for i in range(1, (n + 1)):
#         s += i
#         print(s)
#
#
# if __name__ == '__main__':
#     find_sum()


# # Recursion Example :
# def find_sum(n):
#     if n <= 0:
#         return "Enter a valid input"
#     if n == 1:
#         return 1
#     return n + find_sum(n - 1)
#
#
# if __name__ == '__main__':
#     n = int(input('enter no: '))
#     print(find_sum(n))


# # Recursion using Fibonaci series Example:
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(6))
