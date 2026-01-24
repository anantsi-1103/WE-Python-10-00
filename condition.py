# age = 14

# 18+ = adult , 13 - 17 -> teenager , 13 -> not adult 

#if elif 

# if age >= 18:
#     print("Adult")
# elif age>=13:
#     print("Teenager")
# else:
#     print("Not Adult")

# user - 3 input -> greatest of 3 number 

# a = int(input("Enter your First Number \n"))
# b = int(input("Enter your Second Number \n"))
# c = int(input("Enter your Third Number \n"))

# # a = 34 , b = 75 , c = 23
# if ((a>b) and (a>c)): # 
#     print("A is greatest")
# elif((b>a) and (b>c)):
#      print("B is greatest") # exit 

# else:
#       print("C is greatest")


# marks = 78

# if marks >= 33:
#     # pass
#     if marks >= 90:
#         print('90+')
#     else:
#         print('greater than 33 but less than 90')


# else:
#     print("FAIL")

# age = int(input("Enter your Age \n"))


# if(age>= 18):
#     print('Eligible By Age')
#     dl = input("if u have DL (Say Yes or No) \n")

#     if(dl == 'Yes'):
#         print('yes u can Drive')
#     else:
#         print('You can drive but first apply for DL')

# else:
#     print('Not Eligible')

# a = int(input("Enter your Number \n"))

# if a % 2 == 0:
#     print('Even')

# else:
#     print('Odd')


# result = "even" if a % 2 ==0 else "Odd" 

# print(result)

# a = int(input("Enter your First Number \n"))
# b = int(input("Enter your Second Number \n"))
# c = int(input("Enter your Third Number \n"))


# result = 'A'if (a>b) and (a>c) else 'B' if (b>a) and (b>c) else 'C'
# print(result)


leap = int(input("Enter your year \n"))


if leap % 4 == 0 and leap % 100 != 0 or leap % 400 == 0:
    print('Leap year')
else:
    print('Not a Leap Year')