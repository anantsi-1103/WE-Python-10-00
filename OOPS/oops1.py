class Student:
    def setName(self,Newname , Newage):
        self.name = Newname
        self.age = Newage

    def getName(self):
        return f"Your name is {self.name} and your age is {self.age}"
    

s1 = Student()
s1.setName("Aman" , 29)
print(s1.getName())



s2 = Student()
s2.setName("Ayush" , 23)
print(s2.getName())