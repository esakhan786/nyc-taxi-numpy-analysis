import numpy as np

uni = np.genfromtxt('university_data.csv', delimiter=',', skip_header=True)
mean_GPA = uni[:, 4].mean()
print("Q1 - Average GPA:", mean_GPA)
num_students = uni.shape[0]
print("Q2 - Number of students:", int(num_students))
mean_age = uni[:, 3].mean()
print("Q3 - Average Age:", mean_age)
max_GPA = uni[:, 4].max()
print("Q4 - Highest GPA:", max_GPA)
min_att = uni[:, 6].min()
print("Q5 - Lowest Attendance:", min_att)
avg_proj = uni[:, 7].mean()
print("Q6 - Average Project Score:", avg_proj)
high_gpa_students = uni[uni[:, 4] > 3.5]
print("Q7 - Students with GPA > 3.5:", high_gpa_students.shape[0])
low_att_students = uni[uni[:, 6] < 80]
print("Q8 - Students with Attendance < 80:", low_att_students.shape[0])
total_intern = uni[:, 9].sum()
print("Q9 - Total Internship Hours:", total_intern)
avg_credits = uni[:, 5].mean()
print("Q10 - Average Credits:", avg_credits)
