dictionary = {
    "cat" : "a small animal",
    "table":["a piece of furniture", "list of facts & figures"]
    }

print(dictionary)

# que 2....

subjects = {
    "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "C"     
}

print(len(subjects))

# 3rd....
marks = {}

x = int (input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter math :"))
marks.update({"math" : x})

x = int(input("enter chem :"))
marks.update({"chem" : x})

print(marks)


# 4th......built in deta type use...

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)
# ......

values = {9, "9.0"}
print(values)

# .....

values = {9, "9.0", 2, 4,}
print(values)

# .......

values = {9, 9.0, 8 , "8.0"}
print(values)