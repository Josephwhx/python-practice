x, y = 5, 11
x, y = t

print(x, y)

# Example 1
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

print(list(student_attendance.items()))

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# Example 2
people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

# Destructured
for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# Not Destructured
# for person in people:
#     print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")


# Example 3
head, *tail = [1, 2, 3, 4, 5] 
print(head) # head = 1
print(tail) # tail = all the remaing values