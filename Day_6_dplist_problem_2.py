# Theory: Slicing a nested list makes a shallow copy. The outer list is new,
# but its inner lists are shared.
#
# Simple example:
# original = [[1, 2]]
# sliced = original[:]
# sliced[0][0] = 9
# print(original)  # [[9, 2]] because the inner list is shared
'''
interviw question what is sclicing [::-1]in python?
Anwer: [::-1] is a slicing operation in Python that reverses the order of elements in a list.

'''
"Problem 2: learn slicing a nested list ."


chat_history = ["Hi","What is DBMS?","DBMS is Database Management System","What is OS?","OS is Operating System"]

print(chat_history[0:],"\n") 
print(chat_history[::-1], "\n") 
print(chat_history[1:3], "\n") 

#student marks

marks=[55, 80, 75, 85 ,65, 76]
print(marks[::-1], "\n")

for topper in marks:
    if topper > 80:
        print(topper, "is a topper")