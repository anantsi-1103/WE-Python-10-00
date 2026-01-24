# function create 
def hello():
    print("hello function")

# arguments 
def countHello(n):
    # loop 
    for i in range(1, n+1):
        print("hello ",i)


def cal(b , c ,a=10):
    print(a+b+c)


# function as a template -> 
def sum(a,b):
    print(a+b)

#return int function
def sum_int(a,b):
    return a+b


def check_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def agree(n):
    if n >= 18:
        return "Allowed"
    else:
        return "Not Allowed"


# sum of n natural number -> 


def sum_natural(n):
    sum = 0
    i = 1  # intialization
    while(i<=n):  #  n 
        sum = sum + i # i + sum se 
        i+=1  # increment 
    return sum 


def factorial(n):
    fact = 1 #0 1 2 6 24 120
    i = 1 # 1 2 3 4 5 6
    while(i<=n): # T T T T T F
        fact = fact * i
        # sum = 
        i+=1 # u
    return fact


print(factorial(5))
print(factorial(6))
print(factorial(2))
print(factorial(8))

# normal  -> function + value + logic + display 
# , return(int -> function + value + logic -> return(int)
#  , return(boolean) -> boolean -> True/False -> return true/false
# , return(String) -> String -> return -> " "

# print(type(agree(34)))
# print(type(check_even(34)))
# print(type(sum_int(34,45)))
# print(type(sum(34,45)))



# print(check_even(10))
# print(check_even(45))
# print(check_even(76))
# print(check_even(23))
# print(check_even(3))

# result = agree(34)

# print(type(result)) 

# code reusability ko increase krdeta hai
# sum(10,20)
# sum(140,270)
# sum(10,20)
# sum(10,207)
# sum(140,20)
# sum(110,20)
# sum(10,290)
# sum(190,20)
# sum(10,260)

# function call 
# function ke an
# dr display -> call krthe smaay display krne ki koi need nhi hai
# hello()
# function ko call krthe ho - call krthe samay value dete ho -> parameter

