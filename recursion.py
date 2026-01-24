def sum_loop(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum +i
    return sum

def sum_recu(n):
    #base case
    if(n == 1):
        return n
    # kaam
    return n +  sum_recu(n-1)

def fact(n):
    #base case
    if(n == 1):
        return n
    # kaam
    return n *  fact(n-1)

# 0 1 1 2 3 5 8 13 21 34 55
def fibo(n):
    if n == 0 or n == 1: 
        return n
    return fibo(n-1) + fibo(n-2)

def count(si,ei): # 2 , 10
    if si == ei+1: # 11 == 11
        return 
    
    print(si) # 1 2 3 4 5 6 7 8 9 10 11
    return count(si + 1  , ei) # 3 , 10




count(1,10)
