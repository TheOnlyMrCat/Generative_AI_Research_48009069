import csv
import matplotlib.pyplot as plt
import numpy as np

improvements = []
perceived_improvements = []
satisfactions = []

scores = ["0\nStrongly Disagree", "1", "2", "3", "4", "5\nStrongly Agree"]
Q4_totals = []

with open("data/StudyData_Table1.csv") as file:
    reader = csv.reader(file)
    first_line = True
    for row in reader:
        if first_line:
            first_line = False
            continue
        Particpant,Hours,Before,After,Change,Q1,Q2,Q3,Q4,Q5,Q6 = row
        improvements.append(int(Change))
        perceived_improvements.append(int(Q2))
        satisfactions.append(int(Q4))

with open("data/StudyData_Table2.csv") as file:
    reader = csv.reader(file)
    first_line = True
    for row in reader:
        if first_line:
            first_line = False
            continue
        Score,Q1,Q2,Q3,Q4 = row
        Q4_totals.append(Q4)
        


fig, ax = plt.subplots()
fig.suptitle("Participant satisfaction")
ax.set_xlabel("Score")
ax.set_ylabel("# Participants")
ax.bar(scores, Q4_totals)



fig, ax = plt.subplots()
fig.suptitle("Satisfaction and learning outcomes")
ax.set_xlabel("Satisfaction (0-5)")
ax.set_ylabel("Measured Improvement (Δ points)")

# Move spines to origin (https://stackoverflow.com/questions/25689238/show-origin-axis-x-y-in-matplotlib-plot)
# ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.yaxis.tick_left()

ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
# ax.xaxis.tick_bottom()

fit = np.poly1d(np.polyfit(satisfactions, improvements, 1))

ax.scatter(satisfactions, improvements)

xs = np.arange(min(satisfactions), max(satisfactions) + 1)
ax.plot(xs, fit(xs), "--k")

fig, ax = plt.subplots()
fig.suptitle("Perceived improvement and learning outcomes")
ax.set_xlabel("Perceived improvement (0-5)")
ax.set_ylabel("Measured Improvement (Δ points)")

# Move spines to origin (https://stackoverflow.com/questions/25689238/show-origin-axis-x-y-in-matplotlib-plot)
# ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.yaxis.tick_left()

ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
# ax.xaxis.tick_bottom()

fit = np.poly1d(np.polyfit(perceived_improvements, improvements, 1))

ax.scatter(perceived_improvements, improvements)

xs = np.arange(min(perceived_improvements), max(perceived_improvements) + 1)
ax.plot(xs, fit(xs), "--k")

plt.show()
