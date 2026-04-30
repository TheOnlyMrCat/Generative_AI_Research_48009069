import numpy as np
import matplotlib.pyplot as plt

xs = []
ys = []
with open("data/Student_Attendance_and_Grades.csv") as file:
    is_line1 = True
    for line in file:
        if is_line1:
            is_line1 = False
            continue
        student, attendance, grade = line.strip().split(',')
        xs.append(float(attendance))
        ys.append(float(grade))

fit = np.poly1d(np.polyfit(xs, ys, 1))

plt.title("Student Attendance and Grades")
plt.xlabel("Lecture attendance (%)")
plt.ylabel("Final grade (%)")
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.scatter(xs, ys)

plt.plot(xs, fit(xs), "k")

plt.show()
