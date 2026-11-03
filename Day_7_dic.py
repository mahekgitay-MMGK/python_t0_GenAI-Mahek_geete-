# Dictionary and Hash Map: Simple Theory
#
# A dictionary stores data as key-value pairs. Keys are unique and let us find
# their associated values. Python's built-in `dict` type is a dictionary.
#
# A hash map uses a hash function to turn a key into a location for storing or
# finding its value. Python dictionaries use a hash table internally, making
# lookups, insertions, and deletions fast on average (O(1)).
#
# Example:
'''student = {
	"name": "Asha",
	"age": 20,
	"course": "Data Science",
}

print(student["name"])
print(student["age"])

# Add a new key-value pair and update an existing value.
student["city"] = "Pune"
student["age"] = 21
print(student)

# Output:
# Asha
# 20
# {'name': 'Asha', 'age': 21, 'course': 'Data Science', 'city': 'Pune'}'''

#Task 

students={"Mahek": 90, "Arach": 85, "Riya": 95, "Aditya": 80, "Ananya": 88}
students["Riya"] = 99
print(students)

# Dictionary access and safety
# Use square brackets when you know the key exists. If it is missing, Python
# raises a KeyError. Use get() when a key may not exist; it returns None (or a
# default value you provide) instead of raising an error.
'''print(students["Mahek"])
print(students.get("Unknown"))
print(students.get("Unknown", "Student not found"))'''

# You can also check whether a key exists before accessing its value.
'''if "Riya" in students:
	print(students["Riya"])'''

# Output:
# {'Mahek': 90, 'Arach': 85, 'Riya': 99, 'Aditya': 80, 'Ananya': 88}
# 90
# None
# Student not found
# 99

# Task

print(students.get("Riya"))
print(students.get("sata","Not found"))

# Checking dictionary keys
# Use the `in` keyword to check whether a key exists in a dictionary. It returns
# True or False. This checks keys, not values.
'''if "Riya" in students:
	print("Riya is in the dictionary")'''

# Deleting dictionary items
# Use `del` to remove an item by key. Use `pop()` to remove an item and return
# its value; its optional default avoids a KeyError when the key is missing.
'''del students["Arach"]
removed_score = students.pop("Aditya", None)
print(students)
print(removed_score)'''


school_students={"Mahek": 90, "Arach": 85, "Riya": 95, "Aditya": 80, "Ananya": 88}

if "Mahek" in school_students:
    print("Mahek is in the dictionary")
else:
    print("Mahek is new student")

if "sara" in school_students:
    print("sara is in the dictionary")
else:
    print("sara is new student")

# Looping through a dictionary
# A dictionary loop can access its keys, values, or key-value pairs.
# `keys()` returns the keys, `values()` returns the values, and `items()`
# returns each key and value together as a tuple. In a for loop, `key, value`
# unpacks each pair returned by `items()`.

print("Student names:")
for key in school_students.keys():
	print(key)

print("Student scores:")
for value in school_students.values():
	print(value)

print("Student names and scores:")
for key, value in school_students.items():
	print(key, value)

for name, score in school_students.items():
    print(f"{name}: {score}")

# Nested dictionaries
# A nested dictionary is a dictionary whose values include other dictionaries.
# It is useful for grouping related information under one key. Access a nested
# value by chaining keys, and update it by assigning to the corresponding keys.
classroom = {
	"student1": {"name": "Asha", "age": 20},
	"student2": {"name": "Ravi", "age": 21},
}

print(classroom["student1"]["name"])  # Asha
classroom["student1"]["age"] = 22
classroom["student2"]["grade"] = "A"
print(classroom)

# Use get() when an outer or nested key might be missing.
print(classroom.get("student3", {}).get("name", "Student not found"))


