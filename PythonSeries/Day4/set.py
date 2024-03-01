
collection = {1, 2, 3, "hello" , "world",  4}

print(collection)
print(type(collection))
print(len(collection))      

# for empity set...

collection = set ()

print(type(collection))

#  set methods......
collection = set ()
collection.add(1)
collection.add("apna college")
collection.add(2)

collection.remove(1)

print(collection)

collection.clear()

print(len(collection))

# pop .....
collection = {"hello ", "apna college", "world" , "coading", "python"}

print(collection.pop())
print(collection.pop())
print(collection.pop())

# set methods.....
# union methods....

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2)) # ......
print(set1)             #.......
print(set2)             #........

#intersection.....
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.intersection(set2)) 