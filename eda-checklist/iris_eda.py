import pandas as pd
import plotly.express as px

# Load the dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# 1. Inspect dataset structure
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset shape (rows, columns):")
print(df.shape)

# 2. Check column information and missing values
print("\nDataset information:")
print(df.info())

print("\nMissing values in each column:")
print(df.isnull().sum())

# 3. Distribution of petal length
fig1 = px.histogram(df, x="petal_length", color="species",
                    title="Distribution of Petal Length by Species")
fig1.show()

# 4. Detect possible outliers
fig2 = px.box(df, x="species", y="petal_length",
              title="Box Plot of Petal Length by Species")
fig2.show()

# 5. Relationship between variables
fig3 = px.scatter(df, x="petal_length", y="petal_width", color="species",
                  title="Petal Length vs Petal Width")
fig3.show()

# 6. Example observations
# Observation 1: Setosa flowers have much smaller petal length compared to other species.
# Observation 2: Petal length and petal width show a strong positive relationship.
# Observation 3: Versicolor and Virginica have some overlapping values.
