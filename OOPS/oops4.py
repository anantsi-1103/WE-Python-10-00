class Animal:
    def breathe(self):
        print("Breathing")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def speak(self):
        print("Speaking")


class Cat(Animal):
    def speak(self):
        print("meow")
     
class BabyDog(Dog):
    def sleep(self):
        print("Sleeping")

d = Cat()


d.breathe()
d.eat()
d.speak()