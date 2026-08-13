import pandas as pd
import numpy as np

INPUT = "data/messy_students_1000.csv"
OUTPUT = "output/cleaned_students.csv"


def clean_data(path=INPUT):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)

    # Text cleanup
    for col in ["name", "gender", "placed"]:
        if col in df.columns:
            df[col] = df[col].astype("string").str.strip()

    df["gender"] = (df["gender"].str.lower()
                    .replace({"m": "male", "f": "female"})
                    .replace({"nan": pd.NA})
                    .str.title())
    df["placed"] = df["placed"].str.lower().replace({"y": "yes", "n": "no"})

    # Numeric conversion and attendance percent cleanup
    df["attendance"] = pd.to_numeric(
        df["attendance"].astype("string").str.replace("%", "", regex=False),
        errors="coerce"
    )
    numeric = ["student_id", "age", "python", "dsa", "dbms", "maths", "os",
               "attendance", "projects", "internships", "backlogs", "cgpa"]
    for col in numeric:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Date parsing
    df["admission_date"] = pd.to_datetime(df["admission_date"], errors="coerce", dayfirst=True)

    # Logical validation
    ranges = {
        "age": (17, 30), "attendance": (0, 100),
        "python": (0, 100), "dsa": (0, 100), "dbms": (0, 100),
        "maths": (0, 100), "os": (0, 100), "cgpa": (0, 10),
        "projects": (0, 20), "internships": (0, 10), "backlogs": (0, 20),
    }
    for col, (low, high) in ranges.items():
        df.loc[(df[col] < low) | (df[col] > high), col] = np.nan

    # Remove duplicate student records
    df = df.drop_duplicates(subset="student_id", keep="first")

    # Missing values
    df["name"] = df["name"].fillna("Unknown Student")
    for col in ["gender", "placed"]:
        df[col] = df[col].fillna(df[col].mode(dropna=True).iloc[0])
    for col in ["age", "attendance", "python", "dsa", "dbms", "maths", "os",
                "projects", "internships", "backlogs", "cgpa"]:
        df[col] = df[col].fillna(df[col].median())

    return df


if __name__ == "__main__":
    df = clean_data()
    df.to_csv(OUTPUT, index=False)
    print(f"Cleaned dataset saved: {OUTPUT}")
    print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
