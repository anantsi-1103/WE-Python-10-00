#sum of n natural number 

 # 5

# sum = 0 #0 1 3 6 10 15

# i = 1 # 1 2 3 4 5 6
# while(i<=n): # T T T T T F
#     sum = sum + i
#     # sum = 15
#     i+=1 # u
 

# print(sum)

# fact = 1 #0 1 2 6 24 120

# i = 1 # 1 2 3 4 5 6
# while(i<=n): # T T T T T F
#     fact = fact * i
#     # sum = 
#     i+=1 # u
 

# print(fact)
# count = 0
# if n <= 1:
#     print('not prime')

# # 2 3 4 5 6 7 8 9
# for i in range(2, n+1):
#     if(n % i == 0):
#        count+=1

# if(count == 1):
#     print(f'{n} is a Prime number') 
# else:
#      print(f'{n} is not a Prime number') 

# print(5/2)
# print(5//2)

# n = int(input("Enter your Number \n")) # 345

# temp = n # 345 34 3
# sum = 0 # 0  125 189 216
# # number ko reverse kr ha 

# while(temp != 0): # T T T F
#     #step likhunga ---- repeat 
#     digit = temp % 10 # 3 % 10 == 3
#     sum = sum + digit * digit * digit # 189 + 27 = 216
#     temp = temp // 10 # 34  // 3 // 10 == 0


# if(n == sum):
#     print(f'{n} is a Armstrong Number')
# else:
#     print(f'{n} is not a Armstrong number')

n = int(input("Enter your Number \n")) # 547

# temp = n # 547 54 5 0
# sum = 0 # 0 7 74 745
# # number ko reverse kr ha 

# while(temp != 0): # 
#     #step likhunga ---- repeat 
#     digit = temp % 10 # 5 % 10 = 5
#     sum = sum * 10 + digit #  sum = 74 * 10 + 5 = 745
#     temp = temp // 10 # 5//10 = 0


# # 547 == 745
# if(n == sum):
#     print(f'{n} is a Palindrome Number')
# else:
#     print(f'{n} is not a Palindrome number')

# print("fibonacci series --> ")
# a = 0
# b = 1

# print(a, end=" ")
# print(b, end=" ")

# for i in range(2, n+1):
#     c = a + b
#     print(c,end=" ")

#     a = b
#     b = c

# d = 1 # 1 11 111 1111 11111 111111
# for i in range(1,n+1): # 1 2 3 4 5 6
#     print(d, end=" ") # 1 11 111 1111 11111
#     d = d * 10 + 1 # 111111

# print('after loop')
# print(d)

