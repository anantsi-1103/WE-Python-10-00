# from abc import ABC, abstractmethod


# #abstract class
# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass

# abstract class ko import -> python
from abc import ABC, abstractmethod

#abstract class -- blueprint 
class Vehicle(ABC):

# class k blueprint -> name use krega -> 
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Start")


    def stop(self):
        print("Car Stop")


class Bike(Vehicle):

    def start(self):
        print("Bike Start")


    def stop(self):
        print("Bike Stop")



c =Car()
c.start()
c.stop()