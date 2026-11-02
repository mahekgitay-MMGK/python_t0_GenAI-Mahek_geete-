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
print(sorted_marks)  # Output: [55, 65, 75, 76