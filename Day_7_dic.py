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

