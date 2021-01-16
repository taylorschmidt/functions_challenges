# Write a function named sum_to() that takes a number parameter n and returns the sum of the numbers from 1 to n. For example:
# sum_to(6)  # returns 21
# sum_to(10) # returns 55
​
def sum_to(n):
    #this iterates from 0 to the 7th index which would be 6
    #sum is a built in python function
    return sum(range(n+1))
​
#alternate solution
#     def sum_to(num):
#       sum = 0
#   for i in range(num + 1):
#     sum += i
#   return sum
​
print(sum_to(6))
print(sum_to(10))
​
# Write a function named largest() that takes a list parameter and returns the largest element in that list. You can assume the list contents are all positive numbers. For example:
# largest([10, 4, 2, 231, 91, 54])  # returns 231
# largest([1,2,3,4,0])  # returns 4
​
def largest(list):
    return max(list)
​
#alternative solution
# def largest(list):
#     largestNum = 0
#     for i in list:
#         if i > largestNum:
#             largestNum = i
#     return largestNum
​
print(largest([10, 4, 2, 231, 91, 54]))
​
# Write a function named occurances() that takes two string parameters and counts the number of occurrances of the second string inside the first string. For example:
# occurances('fleep floop', 'e')   # returns 2
# occurances('fleep floop', 'p')   # returns 2
# occurances('fleep floop', 'ee')  # returns 1
# occurances('fleep floop', 'fe')  # returns 0
​
def occurances(str1, str2):
    str1Split = str1.split(str2)
    return(len(str1Split)-1)
print(occurances('fleep floop', 'e'))
​
# def occurances(str, str2):
#       mismatch = False
#   count = 0
#   # Check to see if the str2 exists in the string at all
#   if str2 in str:
#     # If it does, start looking through the string
#     for i in range( len(str) ):
#       # If the string character matches the first char in str2...
#       if str[i] == str2[0]:
#         # Loop through str2 to see if the rest of the chars match
#         for j in range( len(str2) ):
#           if str2[j] != str[i + j]:
#             # If they ever don't match along the length of the str2, then mark a mismatch
#             mismatch = True
#             break;
#         # If there were no mismatches, we can up the occurance count by 1
#         if not mismatch:
#           count += 1
#   # Finally return the count
#   return count
​
# Write a function named product() that takes an arbitrary number of parameters, multiplies them all together, and returns the product. (HINT: Review your notes on *args).
​
def product(*args):
    product = 1
    for i in args:
        product *= i
    return product
​
print(product(3,4))