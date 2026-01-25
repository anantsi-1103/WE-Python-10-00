class Car:
    # brand, model , engine
    # brandName = newname
    # modelName = nName
    # engineName = Ename
    #Setter method -> to set the value 
    # def setBrandName(self,newname):
    #     self.brandName = newname

    # def setModelName(self,mName):
    #     self.modelName = mName

    # def setengineName(self,Ename):
    #     self.engineName = Ename

    # constructor
    # def __init__(self):
    #     print("Constructor is called")

    # constructor 2 
    def __init__(self,bname,mname,ename):
        self.brandName = bname
        self.modelName = mname
        self.engineName = ename

    
    #getter method
    def getData(self):
        print(f"Your Brand name is '{self.brandName}' " 
              f"and model name is '{self.modelName}' "
              f"and engine name '{self.engineName}'")


brandname = input("Enter your brand name \n") 
modelname = input("Enter your model name \n") 
enginename = input("Enter your engine name \n") 

c1 = Car(brandname, modelname ,enginename ) # object -> 
c1.getData()
