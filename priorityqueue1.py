'''append elements (key,values),
key:priority
value:element in queue
and sort the list every time an element
is appended'''
students_grade = []
students_grade.append((1,'Minato'))
students_grade.append((4,'Naruto'))
students_grade.sort(reverse = True)
print("Yes")
print(students_grade)
students_grade.append((3,"Itachi"))
students_grade.sort(reverse = True)
students_grade.append((2,"Goku"))
students_grade.sort(reverse = True)
print("priority wise sorted")
print(students_grade)
print("original Queue")
while students_grade:
    print(students_grade.pop())

