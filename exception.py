
# if x ==5:
#     print(x)

# print(10/0)

# list = [1,2,3,4]
# print(list[100])


# a = ""
# print(len(a))

# f = open("demo.txt")
# print(f)

# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("Ordering service")
# try:
#     # risky code 
#     print(Demo)
# except: # try wale m error aaya toh except chala dunga
#     print("Except Caught")
# else: # try m error nhi aaya toh m else ko chala dunga
#     print("All okay no error")

# finally: # always gonna run 
#     print("Always Executed")

# print("payment service")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")

# try:
#     a = int(input("Enter your number \n"))
#     b = 10//a
#     print(b)

# # aagr 0 
# except ZeroDivisionError:
#     print("Apne A ki value ko 0 diya hai toh kuch nhi hoga")

# # value hi nhi di ya ek improper type ki di
# except ValueError:
#     print("Apne A ki value hi nhi di toh kese kaam hoga")

# # universal
# except:
#     print("galti kuch alag hi hai")

# else: print("All Okay")

# print(5/2)
# print(5//2)

# age = int(input("Enter your age \n"))

# if age < 18:
#     raise SyntaxError("18 se neche wali value allowed nhi hai")
# else:
#     print("Access Granted")


class AgeError(Exception):
    pass

print("Machine start")
try:
    print("Service one enter")
    age = int(input("Enter your age \n"))
    if age < 18:
        raise AgeError("Age error aaya hai yaha pr")
except AgeError as e:
    # print(e)
    print("exception caught ",e)

print("Rest of the services")

# file handling, multi- threading , lambda expression 