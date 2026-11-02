"""Day 6 lesson: Nested lists (lists inside lists)

A nested list is a list that contains one or more other lists. It is useful
when data has more than one level, such as a grid of numbers, class seating,
or a set of students and their scores.

The outer list stores the rows (or groups). Each inner list stores the items
in one row (or group). Use more than one index to reach a value:
    data[row_index][column_index]

Indexes start at 0. For example, grid[1][2] means the item at index 2 in the
inner list at index 1 of grid.
"""


# ---------------------------------------------------------------------------
# 1. Creating and reading a nested list
# ---------------------------------------------------------------------------

# This grid has three rows, and each row contains three values.
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print("Grid:", grid)

# First choose the outer-list index (row), then the inner-list index (column).
print("First row:", grid[0])
print("Value in row 2, column 3:", grid[1][2])

# Negative indexes work at either level.
print("Last row:", grid[-1])
print("Last value in the last row:", grid[-1][-1])

# len(grid) counts rows. len(grid[0]) counts values in the first row.
print("Number of rows:", len(grid))
print("Values in the first row:", len(grid[0]))


# ---------------------------------------------------------------------------
# 2. Changing nested-list values
# ---------------------------------------------------------------------------

# The first index selects a row; the second index selects an item in that row.
grid[0][1] = 20
print("Grid after changing row 1, column 2:", grid)

# append adds an item to the selected inner list.
grid[1].append(10)
print("Grid after adding to row 2:", grid)

# append to the outer list adds a whole new row.
grid.append([10, 11, 12])
print("Grid after adding a row:", grid)


# ---------------------------------------------------------------------------
# 3. Looping through nested lists
# ---------------------------------------------------------------------------

scores = [
    [90, 85, 88],
    [76, 92, 81],
]

# The outer loop visits each inner list; the inner loop visits each score.
print("\nAll scores:")
for student_scores in scores:
    for score in student_scores:
        print(score)

# Use indexes when row and column positions are useful.
print("Scores with row and column indexes:")
for row_index, student_scores in enumerate(scores):
    for column_index, score in enumerate(student_scores):
        print(f"row {row_index}, column {column_index}: {score}")

# A nested list can also be summarized one row at a time.
for student_number, student_scores in enumerate(scores, start=1):
    average = sum(student_scores) / len(student_scores)
    print(f"Student {student_number} average: {average:.1f}")


# ---------------------------------------------------------------------------
# 4. Rows do not have to be the same length
# ---------------------------------------------------------------------------

# A nested list with rows of different lengths is called a jagged list.
shopping_bags = [
    ["bread", "milk"],
    ["apples"],
    ["rice", "beans", "oil"],
]

print("\nShopping bags:")
for bag_number, bag in enumerate(shopping_bags, start=1):
    print(f"Bag {bag_number} has {len(bag)} items:", bag)

# Check a row's length before using an index that might not exist.
if len(shopping_bags[1]) > 1:
    print("Second item in bag 2:", shopping_bags[1][1])
else:
    print("Bag 2 does not have a second item.")


# ---------------------------------------------------------------------------
# 5. A common nested-list pitfall
# ---------------------------------------------------------------------------

# This repeats a reference to the same inner list three times. Updating one
# row therefore appears to update every row.
shared_rows = [[0] * 3] * 3
shared_rows[0][0] = 1
print("\nRows accidentally sharing one inner list:", shared_rows)

# A list comprehension creates a new inner list for each row.
independent_rows = [[0] * 3 for _ in range(3)]
independent_rows[0][0] = 1
print("Rows with independent inner lists:", independent_rows)


# ---------------------------------------------------------------------------
# 6. Quick recap
# ---------------------------------------------------------------------------

# A nested list stores lists inside an outer list.
# Use list[row_index][column_index] to access a value in a two-level list.
# Use nested loops to visit every value.
# Rows may have different lengths, so check before indexing when needed.
# Build independent rows with a comprehension, not [[value] * size] * rows.