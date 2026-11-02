# Theory: pop(), remove(), sort(), and sorted()

# pop(index) removes and returns the item at the given index. Without an index,
# it removes and returns the last item. It changes the original list.
# Example:
# fruits = ["apple", "banana", "cherry"]
# item = fruits.pop(1)
# print(item)    # Output: banana
# print(fruits)  # Output: ['apple', 'cherry']

# remove(value) removes the first matching value. It changes the original list,
# returns None, and raises ValueError if the value is not found.
# Example:
# numbers = [2, 4, 2, 6]
# result = numbers.remove(2)
# print(result)   # Output: None
# print(numbers)  # Output: [4, 2, 6]

# sort() sorts a list in place, changing the original, and returns None.
# Use reverse=True to sort in descending order.
# Example:
# numbers = [5, 1, 4, 2]
# result = numbers.sort()
# print(result)   # Output: None
# print(numbers)  # Output: [1, 2, 4, 5]
# numbers.sort(reverse=True)
# print(numbers)  # Output: [5, 4, 2, 1]

# sorted(iterable) returns a new sorted list and leaves the original unchanged.
# It works with lists, tuples, and other iterables. Use reverse=True for
# descending order.
# Example:
# numbers = [5, 1, 4, 2]
# ordered = sorted(numbers)
# print(ordered)  # Output: [1, 2, 4, 5]
# print(numbers)  # Output: [5, 1, 4, 2]
# print(sorted(numbers, reverse=True))  # Output: [5, 4, 2, 1]


# pop use
subjects=["DBMS","OS","Python","Java","C++"]
subjects.pop(2)  # Removes "Python"
print(subjects)  # Output: ['DBMS', 'OS', 'Java', 'C++']

#sort vs sorted
marks=[55, 80, 75, 85 ,65, 76]
marks.sort() 
print(marks)  # Output: [55, 65, 75, 76, 80, 85]


marks=[55, 80, 75, 85 ,65, 76]
sorted_marks=sorted(marks)
print(marks)  # Output: [55, 80, 75, 85, 65, 76]
print(sorted_marks)  # Output: [55, 65, 75, 76, 80, 85]

#remove 
marks=[55, 80, 75, 85 ,65, 76]
marks.remove(75)  # Removes the first occurrence of 75
print(marks)  # Output: [55, 80, 85, 65, 76]

"interview question what is the difference between sort() and sorted() in python?"
"Answer: The main difference between sort() and sorted()"
"in Python is that sort() is a method that modifies the original list in place and returns None,"
" while sorted() is a built-in function that returns a new sorted list without changing the original list. "
"Additionally, sort() can only be used with lists, whereas sorted() can be used with any iterable (like lists, tuples, etc.)."

# 2nd question: "What is the difference between pop() and remove() in Python?"
"Answer: The main difference between pop() and remove() "
"in Python is that pop() removes an item at a specified index (or the last item if no index is provided) "
"and returns that item, while remove() removes the first occurrence of a specified value from the list and does not return anything."
" Additionally, pop() can raise an IndexError if the index is out of range, while remove() raises a ValueError if the value is not found in the list."