import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

INPUT = "output/cleaned_students.csv"
OUT = Path("output")
OUT.mkdir(exist_ok=True)

df = pd.read_csv(INPUT)

subjects = ["python", "dsa", "dbms", "maths", "os"]

summary = pd.DataFrame({
    "Metric": [
        "Total Students", "Average CGPA", "Average Attendance (%)",
        "Placement Rate (%)", "Average Projects", "Average Internships",
        "Students With Backlogs"
    ],
    "Value": [
        len(df),
        round(df["cgpa"].mean(), 2),
        round(df["attendance"].mean(), 2),
        round(df["placed"].eq("yes").mean() * 100, 2),
        round(df["projects"].mean(), 2),
        round(df["internships"].mean(), 2),
        int(df["backlogs"].gt(0).sum()),
    ]
})
summary.to_csv(OUT / "summary.csv", index=False)

subject_avg = df[subjects].mean().round(2).rename("Average_Marks").reset_index()
subject_avg.columns = ["Subject", "Average_Marks"]
subject_avg.to_csv(OUT / "subject_averages.csv", index=False)

placement = (df.groupby("placed")[
    ["cgpa", "attendance", "projects", "internships", "backlogs"]
].mean().round(2).reset_index())
placement.to_csv(OUT / "placement_analysis.csv", index=False)

# Top students
df.nlargest(10, "cgpa")[["student_id", "name", "cgpa", "attendance", "projects", "placed"]].to_csv(
    OUT / "top_10_students.csv", index=False
)

# Correlation report
corr_cols = ["attendance", *subjects, "projects", "internships", "backlogs", "cgpa"]
df[corr_cols].corr()["cgpa"].sort_values(ascending=False).to_csv(OUT / "cgpa_correlations.csv", header=["Correlation"])

# Charts
plt.figure(figsize=(7, 4))
df["cgpa"].plot(kind="hist", bins=15)
plt.title("CGPA Distribution")
plt.xlabel("CGPA")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(OUT / "cgpa_distribution.png", dpi=150)
plt.close()

plt.figure(figsize=(7, 4))
subject_avg.plot(x="Subject", y="Average_Marks", kind="bar", legend=False)
plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUT / "subject_averages.png", dpi=150)
plt.close()

plt.figure(figsize=(7, 4))
plt.scatter(df["attendance"], df["cgpa"], alpha=0.5)
plt.title("Attendance vs CGPA")
plt.xlabel("Attendance (%)")
plt.ylabel("CGPA")
plt.tight_layout()
plt.savefig(OUT / "attendance_vs_cgpa.png", dpi=150)
plt.close()

plt.figure(figsize=(6, 4))
df["placed"].value_counts().plot(kind="bar")
plt.title("Placement Status")
plt.xlabel("Placed")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUT / "placement_status.png", dpi=150)
plt.close()

print(summary.to_string(index=False))
print("\nAnalysis completed. Reports and charts are in output/")
