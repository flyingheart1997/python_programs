# Insert/Delete element at beginning = O(n)
# Insert/Delete element at end = O(1)
# Insert/Delete element at middle = O(n)
# Array Traversal = O(1)
# Accessing element by value = O(1)

# Array are two types => 1. Static Array and 2. Dynamic Array
# in python only Dynamic array which is list. list is a dynamic array.
# but as our need we can use numpy as static array.

# python array is hetrogenious becaus you can store diffrent type of data like,(int,str,dict,etc..) in the same array.

# static array : in static array first we need to declear a size of arry, then we can add element in this array.
# dynamic array : in dynamic array we did not declear  size of an arry, we can add multiple element.

# store apples's stock price for 5 days and answer...?
# 1. what was the price of day 4 ?
# 2. which day price was 320 ?
# 3. insert new element 500 .
# 4. update new element 520 to 580.
# Example

stock_price = [298, 305, 320, 390, 440, 520]
# we know that 1 byte means 8 bit           => 298 = 100101010
# and storing a int no. mostly use 4 byte.
# like: 298 = 00000000 00000000 00000001 00101010
# so in case of array data will store in memory like this:
# 100(memory location) = 298   => # stock_price[0] => memory location is 100
# 104(memory location) = 305
# 108(memory location) = 320   => # stock_price[2] => memory location is [100 + 2 * sizeof integer (4)] = 108
# 112(memory location) = 390   and so on...


# 1. Ans.........
# 1. what was the price of day 4 ?
print(stock_price[3])  # output => price 390
# in array operation lookup by index is = O(1) because perform time is constant

# 2. on what day price was 320 ?
for i in range(len(stock_price)):
    if stock_price[i] == 320:
        print(i)  # output => day 2
# in array Iteration (Python "for" Loops (Definite Iteration) ·
# Repetitive execution of the same block of code over and over is referred to as iteration.)
# is = O(n) because perform time is not constant

# 3. insert new element 500 .
stock_price.insert(5, 500)
print(stock_price)
# in array insertion time complexcity is also O(n)

# 4. update new element 520 to 580.
stock_price[6] = 580
print(stock_price)

# Exercise :
# 1. Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2130 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
#
# ====>
list_name = [{'january': 2200, 'February': 2350}]
# add element in an array.....
list_name[0]['March'] = 2600
list_name[0]['April'] = 2130
list_name[0]['May'] = 2190
# 1. In Feb, how many dollars you spent extra compare to January?
diffrence = list_name[0]['February'] - list_name[0]['january']
print(f'In Feb, {diffrence} many dollars i spent extra compare to January')

# 2. Find out your total expense in first quarter (first three months) of the year.
sum_of = list_name[0]['january']+list_name[0]['February']+list_name[0]['March']
print(f'Total expense in first quarter (first three months) of the year is : {sum_of}')

# 3. Find out if you spent exactly 2130 dollars in any month
for i in list_name[0].items():
    if i[1] == 2130:
        print(f'In {i[0]} I spent exactly 2130 dollars')

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
list_name[0]['June'] = 1980
print(list_name)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list based on this
expend = list_name[0]['April']
after_refund = expend - 200
print(f'Total expan after getting refund value is {after_refund}')
list_name[0]['April'] = after_refund
print(list_name)

# 2. You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,
#
# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

# ====>
# 1. Length of the list
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
print(len(heros))

# 2. Add 'black panther' at the end of this list
heros.insert(5, 'black panther')
print(heros)

# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
print("After removing 'black panthor' :", heros)
heros.insert(2, 'black panthor')
print("Insert 'black panthor' before hulk : ", heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# heros.remove('thor','hulk')
heros.remove('thor'), heros.remove('hulk'), heros.insert(1, 'doctor strange')  # or heros[1:3] = 'doctor strange'
print(heros)

# 5. Sort the heros list in alphabetical order (Use dir() functions to list down all functions available in list)

heros.sort()
print(heros)

# 3.Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user using input() function
list_of_odd = []
value = int(input('enter max no. : '))
for i in range(1, value):
    if i % 2 != 0:
        list_of_odd.append(i)
print('list of odd number is: ', list_of_odd)
