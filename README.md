# 🎓 Student Data Analyzer

A Python-based **Student Data Analysis and Data Cleaning project** built using **Pandas, NumPy, and Matplotlib**.

This project works with a messy student dataset containing missing values, duplicate records, inconsistent formats, invalid values, and other real-world data problems. The main goal is to clean the dataset and extract useful insights from it.

## 🚀 Project Overview

Real-world datasets are rarely clean. This project demonstrates how to:

* Load data using Pandas
* Explore and understand a dataset
* Detect missing values
* Handle duplicate records
* Fix inconsistent data
* Detect invalid values and outliers
* Convert incorrect data types
* Perform statistical analysis using NumPy
* Analyze student performance
* Study relationships between attendance, marks, CGPA, projects, and placements
* Generate useful insights from student data

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Jupyter Notebook / VS Code**
* **Git & GitHub**

## 📂 Project Structure

```text
Student-Data-Analyzer/
│
├── data/
│   └── messy_students_1000.csv
│
├── notebooks/
│   └── student_data_analysis.ipynb
│
├── src/
│   └── data_cleaning.py
│
├── output/
│   └── cleaned_students.csv
│
├── README.md
└── requirements.txt
```

## 📊 Dataset

The dataset contains student information such as:

| Column         | Description               |
| -------------- | ------------------------- |
| Student_ID     | Unique student identifier |
| Name           | Student name              |
| Age            | Student age               |
| Gender         | Student gender            |
| Attendance     | Attendance percentage     |
| Python         | Python marks              |
| DSA            | DSA marks                 |
| DBMS           | DBMS marks                |
| Maths          | Mathematics marks         |
| OS             | Operating Systems marks   |
| Projects       | Number of projects        |
| Internships    | Number of internships     |
| Backlogs       | Number of backlogs        |
| CGPA           | Student CGPA              |
| Placed         | Placement status          |
| Admission_Date | Admission date            |

The original dataset contains **1000 students**, with additional duplicate records and intentionally messy values for practicing data cleaning.

## 🧹 Data Cleaning

The project handles several common real-world data-quality problems:

### Missing Values

```python
df.isnull().sum()
```

Missing values are identified and handled using appropriate Pandas techniques.

### Duplicate Records

```python
df.duplicated().sum()

df.drop_duplicates(inplace=True)
```

### Inconsistent Categories

For example:

```text
Male
M
male
Male 
```

These values can be standardized into a single format.

### Invalid Values

Examples include:

```text
Attendance = 145%
Python = -5
CGPA = 15
Age = 99
```

These values are identified and corrected or removed based on logical constraints.

### Incorrect Data Types

Some numerical values may be stored as strings:

```text
"85"
"N/A"
"unknown"
```

These are converted into appropriate numerical formats.

## 📈 Data Analysis

After cleaning the dataset, different questions can be answered.

### Student Performance

* Average CGPA
* Highest and lowest CGPA
* Average marks in each subject
* Top-performing students
* Students with low attendance
* Students with backlogs

### Placement Analysis

The project can analyze:

* Placement percentage
* Average CGPA of placed students
* Average CGPA of non-placed students
* Effect of projects on placement
* Effect of internships on placement
* Relationship between attendance and placement

### Example

```python
placed_students = df[df["Placed"] == "Yes"]

average_cgpa = placed_students["CGPA"].mean()

print("Average CGPA of placed students:", average_cgpa)
```

## 🔢 NumPy Usage

NumPy is used for numerical and statistical operations such as:

```python
import numpy as np

mean = np.mean(df["CGPA"])
median = np.median(df["CGPA"])
std = np.std(df["CGPA"])
```

This helps understand the distribution and variation of student performance.

## 📊 Visualization

Matplotlib can be used to create:

* CGPA distribution
* Subject-wise average marks
* Attendance vs CGPA
* Projects vs placement
* Placement distribution
* Gender-wise performance

Example:

```python
import matplotlib.pyplot as plt

plt.hist(df["CGPA"], bins=10)
plt.xlabel("CGPA")
plt.ylabel("Number of Students")
plt.title("CGPA Distribution")
plt.show()
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/Student-Data-Analyzer.git
```

Move into the project directory:

```bash
cd Student-Data-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Start Jupyter Notebook:

```bash
jupyter notebook
```

Then open:

```text
notebooks/student_data_analysis.ipynb
```

Or run the Python scripts directly:

```bash
python src/data_cleaning.py
```

## 📦 Requirements

Example `requirements.txt`:

```text
pandas
numpy
matplotlib
jupyter
```

## 🎯 Learning Objectives

This project was created to practice:

* Python programming
* NumPy
* Pandas
* Data cleaning
* Exploratory Data Analysis (EDA)
* Data visualization
* Handling real-world messy datasets
* Git and GitHub

## 🔮 Future Improvements

Possible improvements include:

* Add Seaborn visualizations
* Build an interactive dashboard
* Add Streamlit interface
* Add machine learning-based placement prediction
* Add automated data-cleaning functions
* Perform correlation analysis
* Add automated EDA reports

## 👨‍💻 Author

**Shaurya Singh**

B.Tech CSE Student

Interested in:

* Python
* Data Science
* AI/ML
* DSA
* Software Development

## ⭐ If You Like This Project

If you found this project useful, consider giving it a ⭐ on GitHub!

---

**Made with Python 🐍 | Pandas 🐼 | NumPy 🔢 | Matplotlib 📊**
