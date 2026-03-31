# ============================================================
# Iris Dataset - Exploratory Data Analysis (EDA)
# ============================================================
# This script performs a comprehensive EDA on the Iris dataset
# using Pandas for data manipulation and Plotly for visualization.
# ============================================================

# --- Step 0: Import Required Libraries ---
import pandas as pd
import plotly.express as px

# ============================================================
# STEP 1: Load the Dataset
# ============================================================
# Load the Iris dataset from the provided URL.
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
print("[OK] Dataset loaded successfully!\n")

# ============================================================
# STEP 2: Inspect the Dataset Structure
# ============================================================

# 2a. View the first 5 rows to get a quick look at the data
print("=" * 60)
print("FIRST 5 ROWS OF THE DATASET")
print("=" * 60)
print(df.head())
print()

# 2b. View the last 5 rows
print("=" * 60)
print("LAST 5 ROWS OF THE DATASET")
print("=" * 60)
print(df.tail())
print()

# 2c. Check the shape (rows, columns)
print("=" * 60)
print("DATASET SHAPE")
print("=" * 60)
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
# Observation: The dataset contains 150 samples and 5 features (4 numeric + 1 categorical).
print()

# ============================================================
# STEP 3: Check Column Information and Missing Values
# ============================================================

# 3a. Column data types and non-null counts
print("=" * 60)
print("COLUMN INFORMATION (df.info())")
print("=" * 60)
df.info()
print()

# 3b. Check for missing values
print("=" * 60)
print("MISSING VALUES PER COLUMN")
print("=" * 60)
missing = df.isnull().sum()
print(missing)
# Observation: There are no missing values in any column. The dataset is clean.
print()

# 3c. Check for duplicate rows
print("=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")
# Observation: There are a few duplicate rows, but they may represent
# genuinely identical flower measurements, so we keep them.
print()

# ============================================================
# STEP 4: Summary Statistics
# ============================================================
print("=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)
print(df.describe())
# Observation: Petal length has the widest range (1.0 to 6.9 cm), suggesting
# it may be a strong differentiator between species. Sepal width has the
# narrowest spread among the numeric features.
print()

# Species distribution
print("=" * 60)
print("SPECIES DISTRIBUTION (Value Counts)")
print("=" * 60)
print(df["species"].value_counts())
# Observation: The dataset is perfectly balanced — each species has exactly 50 samples.
print()

# ============================================================
# STEP 5: Distribution Analysis of Individual Features
# ============================================================
# Analyzing the distribution of petal_length as a representative feature.

# 5a. Histogram of petal_length colored by species
fig1 = px.histogram(
    df,
    x="petal_length",
    color="species",
    nbins=30,
    title="Distribution of Petal Length by Species",
    labels={"petal_length": "Petal Length (cm)", "count": "Frequency"},
    opacity=0.7,
    barmode="overlay",
    color_discrete_sequence=["#636EFA", "#EF553B", "#00CC96"],
)
fig1.update_layout(template="plotly_white")
fig1.show()
# Observation: Setosa has distinctly shorter petals (clustered around 1.0–1.9 cm).
# Versicolor and Virginica overlap slightly but Virginica tends to have longer petals.

# 5b. Box plots for all numeric features grouped by species
for col in ["sepal_length", "sepal_width", "petal_length", "petal_width"]:
    fig = px.box(
        df,
        x="species",
        y=col,
        color="species",
        title=f"Box Plot of {col.replace('_', ' ').title()} by Species",
        labels={col: col.replace("_", " ").title() + " (cm)", "species": "Species"},
        color_discrete_sequence=["#636EFA", "#EF553B", "#00CC96"],
    )
    fig.update_layout(template="plotly_white")
    fig.show()
# Observation: Setosa is clearly separable from the other two species across
# all features, especially petal_length and petal_width.

# ============================================================
# STEP 6: Identify Possible Outliers
# ============================================================
# Using the IQR (Interquartile Range) method to detect outliers.

print("=" * 60)
print("OUTLIER DETECTION (IQR Method)")
print("=" * 60)

numeric_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"\n{col}:")
    print(f"  Q1 = {Q1}, Q3 = {Q3}, IQR = {IQR:.2f}")
    print(f"  Lower Bound = {lower_bound:.2f}, Upper Bound = {upper_bound:.2f}")
    print(f"  Number of outliers = {len(outliers)}")
    if len(outliers) > 0:
        print(f"  Outlier rows:\n{outliers[[col, 'species']].to_string(index=True)}")

# Observation: Sepal width has a few outliers. These are mostly Setosa samples
# with unusually wide or narrow sepals. The other features have few to no outliers,
# indicating the data is relatively well-distributed.
print()

# ============================================================
# STEP 7: Analyze Relationships Between Variables
# ============================================================

# 7a. Scatter plot of petal_length vs petal_width (colored by species)
fig2 = px.scatter(
    df,
    x="petal_length",
    y="petal_width",
    color="species",
    title="Petal Length vs Petal Width by Species",
    labels={
        "petal_length": "Petal Length (cm)",
        "petal_width": "Petal Width (cm)",
    },
    color_discrete_sequence=["#636EFA", "#EF553B", "#00CC96"],
)
fig2.update_layout(template="plotly_white")
fig2.show()
# Observation: There is a strong positive linear correlation between petal length
# and petal width. Setosa forms a tight, well-separated cluster in the bottom-left.
# Versicolor and Virginica are also separable but with some overlap.

# 7b. Scatter plot of sepal_length vs sepal_width
fig3 = px.scatter(
    df,
    x="sepal_length",
    y="sepal_width",
    color="species",
    title="Sepal Length vs Sepal Width by Species",
    labels={
        "sepal_length": "Sepal Length (cm)",
        "sepal_width": "Sepal Width (cm)",
    },
    color_discrete_sequence=["#636EFA", "#EF553B", "#00CC96"],
)
fig3.update_layout(template="plotly_white")
fig3.show()
# Observation: Sepal measurements show more overlap between species compared to
# petal measurements. Setosa has wider sepals relative to its sepal length.

# 7c. Correlation Heatmap
print("=" * 60)
print("CORRELATION MATRIX (Numeric Features)")
print("=" * 60)
corr = df[numeric_cols].corr()
print(corr)
print()
# Observation: Petal length and petal width have a very high correlation (≈0.96).
# Sepal length is also positively correlated with petal dimensions.
# Sepal width is negatively correlated with the other features.

# Plotly heatmap of the correlation matrix
fig4 = px.imshow(
    corr,
    text_auto=".2f",
    title="Correlation Heatmap of Numeric Features",
    labels=dict(color="Correlation"),
    color_continuous_scale="RdBu_r",
    zmin=-1,
    zmax=1,
)
fig4.update_layout(template="plotly_white")
fig4.show()

# 7d. Pair plot (scatter matrix) — overview of all feature relationships
fig5 = px.scatter_matrix(
    df,
    dimensions=numeric_cols,
    color="species",
    title="Scatter Matrix of All Features",
    color_discrete_sequence=["#636EFA", "#EF553B", "#00CC96"],
)
fig5.update_traces(diagonal_visible=False)
fig5.update_layout(template="plotly_white", height=800, width=800)
fig5.show()
# Observation: The scatter matrix confirms that petal-based features provide the
# best species separation. Setosa is linearly separable from the others in almost
# every feature combination.

# ============================================================
# STEP 8: Species-Level Insights
# ============================================================

# Group by species and compute summary statistics
print("=" * 60)
print("MEAN VALUES BY SPECIES")
print("=" * 60)
species_mean = df.groupby("species")[numeric_cols].mean()
print(species_mean)
print()
# Observation:
# - Setosa has the smallest petals (avg petal_length ≈ 1.46 cm) but relatively
#   wide sepals (avg sepal_width ≈ 3.43 cm).
# - Virginica has the largest measurements overall.
# - Versicolor falls between Setosa and Virginica in all features.

print("=" * 60)
print("STANDARD DEVIATION BY SPECIES")
print("=" * 60)
species_std = df.groupby("species")[numeric_cols].std()
print(species_std)
print()
# Observation: Setosa has the least variability in petal measurements,
# meaning its petal features are very consistent — making it easy to classify.

# Violin plots — showing distribution shape per species
for col in numeric_cols:
    fig = px.violin(
        df,
        x="species",
        y=col,
        color="species",
        box=True,
        points="all",
        title=f"Violin Plot of {col.replace('_', ' ').title()} by Species",
        labels={col: col.replace("_", " ").title() + " (cm)", "species": "Species"},
        color_discrete_sequence=["#636EFA", "#EF553B", "#00CC96"],
    )
    fig.update_layout(template="plotly_white")
    fig.show()
# Observation: Violin plots reveal the probability density of each feature
# per species. Setosa distributions are narrow and non-overlapping with the
# other species for petal features, confirming its distinctiveness.

# ============================================================
# STEP 9: Final Summary of EDA Insights
# ============================================================
print("=" * 60)
print("SUMMARY OF KEY EDA INSIGHTS")
print("=" * 60)
print("""
1. The Iris dataset has 150 samples, 4 numeric features, and 1 target (species).
2. There are NO missing values. The dataset is balanced (50 samples per species).
3. Petal length and petal width are the most discriminative features for species classification.
4. Setosa is linearly separable from Versicolor and Virginica based on petal measurements.
5. Versicolor and Virginica overlap slightly but can still be distinguished.
6. Petal length and petal width are highly correlated (r ≈ 0.96).
7. Sepal width has some outliers, mostly in the Setosa class.
8. A machine learning model using petal features should achieve high accuracy.
""")
print("[OK] EDA Complete!")
