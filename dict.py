mydict = {
    "name" : "Aman",
    "age":19,
    "marks": {
        "Math":90,
        "Hindi":78,
        "Bio":67
    }
}

print(mydict)
mydict["marks"]["Bio"] = 70
print(mydict)

mydict["marks"]["Comp"] = 100
print(mydict)

mydict["City"] = "Gurugram"
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)

mydict.clear()
print(mydict)


# print(mydict)
# print(mydict["marks"][1])
# mydict["marks"][1] = 70
# print(mydict["marks"][1])



# print(mydict)
# print(mydict["name"])
# print(mydict["age"])
# print(mydict["marks"])

# #access - key , mutate key

# mydict["age"] = 20
# print(mydict)

# # aagr key meri exist hogi - to key ki value change ho hojaegi
# # aagr meri key ki value nhi -> key add

# mydict["City"] = 'Delhi'
# print(mydict)

# print(mydict["City"])
# print(mydict.get("City"))

# print(mydict.keys())
# print(mydict.values())

# print(mydict)
# print(mydict.items())