# f = open("filehandling/demo.txt" , "r")
# inserting a data
# w -> file exist? "okay" : "file created"
# w -> data nhi hai toh add hojaega or data hai toh next data jo ap
# insert kroge woh apka apply hojaega
# f.write("and also today we will do multithreading")
# print("data stored")
# read() -> full data
# readline() -> only first line 
# readlines() -> data ko list m convert krdeta hai
# data = f.readlines()
# print(data)

with open("filehandling/demo.txt","a") as f:
    f.write("\npython")
#     print(f.read())