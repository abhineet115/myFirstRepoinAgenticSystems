#  Sample Data (5–10 Rows)

import pandas as pd
import numpy as np

# Creating sample dataset
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)
print(df)


null_values = df.isnull(True)
print(null_values)

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df)

df_clean = df.dropna(subset=["Temporary_Notes"])
print(df_clean)


rename = df.rename(columns={"Salary": "Annual_Salary"})
print(rename)

summary = df.groupby("Department")["Salary"].agg(["mean", "count"])
print(summary)