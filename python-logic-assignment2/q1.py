import pandas as pd

df = pd.read_csv("students_data.csv")
single_column = df["Score"]
print("\nSingle column:",single_column)

selectmultiple = df[["Name", "Score"]]
print("\nSelect multiple:",selectmultiple)

firstthree_rows = df.iloc[0:3]
print("\nFirst three rows:",firstthree_rows)

firstthree_rows = df.loc[0:3]
print("\nFirst three rows:",firstthree_rows)

filter_rows = df[df["Score"] > 85]
print("\nFiltered rows:",filter_rows)

high_performing_students = (
    df[(df["Score"] > 85) & (df["Passed"] == True)]
    .sort_values(by="Score", ascending=False)
)

print("\nHigh-performing students:")
print(high_performing_students)