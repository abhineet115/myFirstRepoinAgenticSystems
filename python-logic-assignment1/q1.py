import pandas as pd

load_data = pd.read_csv("sample_data.csv")
print("First 5 rows:\n",load_data.head(5))
print("Last 5 rows:\n",load_data.tail(5))
print("Data info:\n",load_data.info())
print("Data description:\n",load_data.describe())

single_column = load_data["Age"]
print("Single column:\n",single_column.head(5))

multiple_columns = load_data[["Age", "City"]]
print("Multiple columns:\n",multiple_columns.head(5))

filter_row = load_data[load_data["Age"] > 30]
print("Filter row:\n",filter_row.head(5))
