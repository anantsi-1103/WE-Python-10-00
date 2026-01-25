class login:

    def setusername(self,uname):
        self.userName = uname


    def setPassword(self, passW):
        self.__password = passW
        #private rhete hai -> 

    def getpass(self):
        print(f"{self.__password}")


l1 = login()

l1.setusername("admin")
l1.setPassword(123456)

print(l1.userName)
l1.getpass()
# print(l1.__password)