#problem with append and extend

a=[1,2]
a.append([3,4])

b=[1,2]
b.extend([3,4])

print(a,"\n",b)
# The difference between append and extend is that append adds its argument as a single element to the end of a list, while extend iterates over its argument adding each element to the list, extending the list.
#The way on thinking.
subjects=["DBMS","os"]
subjects.append(["CN","Python"])
new_subjects=["DBMS","os"]
new_subjects.extend(["CN","Python"])
print(subjects)
print(new_subjects)

#Here is the difference between append and extend in Python:
''' Look above we add (["CN","Python"]) to the subjects list using append and extend.
now look below we add (AIML) this bug create and we learn .'''
mergen_new_sem=["DBMS","os","CN","Python","Math"]

mergen_new_sem.append("AIML")
print(mergen_new_sem)
mergen_new_sem=["DBMS","os","CN","Python","Math"]

mergen_new_sem.extend("AIML")
print(mergen_new_sem)
