class Father:
    def speak(self):
        print("Speaking from Father class")


class Mother:
    def eat(self):
        print("eating from Mother CLass")


class Child(Father,Mother):
    def study(self):
        print("Self study")


c = Child()

c.speak() # father
c.eat() # mother
c.study() # self