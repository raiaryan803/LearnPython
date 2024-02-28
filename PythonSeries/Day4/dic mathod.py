#  update method.....

student = {
    "name" : "alok rai shivam",
    "subjects" : {
    

    "phy" : 35,
        "chem" :8,
        "math" :10,
    }
}

student.update({"city" : "delhi" ,"age": 29})
print (student)

new_dict = {"name" : "aluu", "age" : 16}
student.update(new_dict)

print(student)

#.key student .....
{
    "name" : "alok rai shivam",
    "subjects" : {
        "phy" : 35,
        "chem" :8,
        "math" :10,
    }
}

print (student.keys())  # 1st.....
print(len(student))     # 2nd.....

 #  values methods......

student = {
    "name" : "alok rai shivam",
    "subjects" : {
        "phy" : 35,
        "chem" :8,
        "math" :10,
    }
}

print (student.values())         #1st.....
print (list(student.values()))   #2nd.....

# #dict.items methods.........
 
student = {
    "name" : "alok rai shivam",
    "subjects" : {
        "phy" : 35,
        "chem" :8,
        "math" :10,
    }
}    

print(student.items())        #1st......
print(list(student.items()))  #2nd......

pairs = list(student.items())
print(pairs[0])                 #3rd.......

 # .get methods...........

student = {
    "name" : "alok rai shivam",
    "subjects" : {
        "phy" : 35,
        "chem" :8,
        "math" :10,
    }
}

print(student["name"])
print(student.get("name"))

#print(student["name2"])       # error
print(student.get("name2"))   # no error -> None


# # error ke baad ka shi code bhi execute nhi hoga....

# print ("BEFORE")
# print (student["name2"])    # error
# print("AFTER")