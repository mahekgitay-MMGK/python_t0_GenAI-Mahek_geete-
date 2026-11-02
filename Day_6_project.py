students = [
	{"name": "Aarav", "marks": 85},
	{"name": "Aditi", "marks": 92},
	{"name": "Arjun", "marks": 78},
	{"name": "Diya", "marks": 88},
	{"name": "Ishaan", "marks": 74},
	{"name": "Kavya", "marks": 95},
	{"name": "Meera", "marks": 81},
	{"name": "Rohan", "marks": 89},
	{"name": "Sana", "marks": 67},
	{"name": "Vihaan", "marks": 90},
]
#sort highest to lowest marks

sorted_students=sorted(students, key=lambda x: x["marks"], reverse=True)
print(sorted_students,"\n")
#pop last student
removed_student=sorted_students.pop()
print("removed student:\n", removed_student)
print("remaining students:\n", sorted_students)