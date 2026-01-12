# 📊 Student Marks Bar Chart 🏫

A simple Python project using `matplotlib` to **visualize student marks** in a colorful bar chart. Perfect for beginners learning data visualization! 🎨✨

## Features ⭐

- 📈 Displays a bar chart of student marks  
- 🎨 Uses a vibrant color for the bars  
- 🐍 Simple Python code for beginners to understand  

## Requirements 🛠️

- Python 3.x  
- `matplotlib` module (`pip install matplotlib` if not already installed)  

## How to Run ▶️

1. Clone or download this repository  
2. Open the Python file (`student_marks.py`) in your IDE or editor  
3. Run the script:

```bash
python student_marks.py
```

4. A bar chart will pop up showing the marks of each student 📊

### Code Overview 📝

```bash
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
```

### How it Works 🔍

1. 🧑‍🎓 Student names are stored in a list
2. 📝 Their marks are stored in a corresponding list
3. 🟪 plt.bar() creates a bar chart with the given data
4. 🏷️ Titles and labels are added for clarity
5. 📊 plt.show() displays the chart

### Screenshots 📸
[![Student Marks Bar Chart](https://github.com/owaiskazmi/Matplotlib-Visuals/blob/main/Screenshots/graph.png)](https://github.com/owaiskazmi/Matplotlib-Visuals/blob/main/Screenshots/graph.png)

