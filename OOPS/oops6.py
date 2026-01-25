# print(10+20)# 2 number ko add
# print("10"+"20") # 2 string ko add
# print([10]+[20]) # 2 list ko add

# Method Overloading - compiler time : when u have same function name but diff parameter

class Cal:
    def cal(self,a,b):
        return a+b
    
    def cal(self,a,b,c):
        return a+b+c
    
    def cal(self,a,b,c,d):
        return a+b+c+d
    
    # latest function ko get kr rha hai
    def cal(self,a,b,c,d,e):
        return a+b+c+d+e
    

# c = Cal()

# c.cal(10,20,7,9,56)



# Method Overriding - Run time -> when two diff connected class -> when both call have same 
#function name but diff meaning 

class Father:
    def speak(self):
        print("Speaking from Father")


class Child(Father):
    def eat(self):
        print("eating")

    
    def speak(self):
        print("Speaking from self")

    def __init__(self):
        # super is function which refer to the parent class
        super().speak()
        print("from constructor")

c = Child()
c.speak()