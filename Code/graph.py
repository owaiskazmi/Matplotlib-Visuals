import matplotlib.pyplot as plt

students = ["Ali", "Sara", "Owais", "Ayesha"]
marks = [85, 90, 78, 88]

print ()
plt.bar (students, marks, color = "purple")
plt.title ("Student Marks")
plt.xlabel ("Students")
plt.ylabel ("Marks")
plt.show ()
print ()
