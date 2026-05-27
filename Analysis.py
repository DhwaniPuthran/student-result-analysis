import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# Show data
print(df)

# Average marks
df["Average"] = (
    df["Maths"] +
    df["Science"] +
    df["English"]
) / 3

print("\nAverage Marks:")
print(df[["Name", "Average"]])

# Grade Function
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    else:
        return "C"

# Add Grade Column
df["Grade"] = df["Average"].apply(grade)

print("\nGrades:")
print(df[["Name", "Average", "Grade"]])

# Pass/Fail Function
def result(avg):
    if avg >= 35:
        return "Pass"
    else:
        return "Fail"

# Add Result Column
df["Result"] = df["Average"].apply(result)

print("\nPass/Fail:")
print(df[["Name", "Result"]])

# Attendance Analysis
attendance_avg = df["Attendance"].mean()

print("\nAverage Attendance:")
print(attendance_avg)

# Low Attendance Students
low_attendance = df[df["Attendance"] < 80]

print("\nLow Attendance Students:")
print(low_attendance)

# Topper
topper = df.loc[df["Average"].idxmax()]

print("\nTopper:")
print(topper)

# Subject averages
subject_avg = df[[
    "Maths",
    "Science",
    "English"
]].mean()

print("\nSubject Averages:")
print(subject_avg)

# Bar Graph
subject_avg.plot(kind="bar")

plt.title("Subject Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()

# Pie Chart for Grades
df["Grade"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Grade Distribution")

plt.show()
