# 🤖 My First Repo in Agentic Systems

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![SQL](https://img.shields.io/badge/SQL-Relational_DB-CC292B?style=for-the-badge&logo=sqlite&logoColor=white)](https://en.wikipedia.org/wiki/SQL)

---

## 📌 Overview

Welcome to **`myFirstRepoinAgenticSystems`**! This repository serves as a comprehensive, structured foundation for mastering core software engineering, data science, and database fundamentals required for building robust **Agentic AI Systems**.

Before deploying intelligent agents, autonomous pipelines, and LLM-powered systems, a strong mastery of foundational Python, algorithmic logic, numerical computation, exploratory data analysis, and relational data management is essential.

---

## 📂 Repository Structure

```plaintext
myFirstRepoinAgenticSystems/
│
├── 🧠 Python Core & Logic
│   ├── python-fundamentals-assignment/   # Basic syntax, variables, operators, user input
│   ├── python-logic-assignment/          # Conditional logic and branching
│   ├── python-logic-assignment1/         # Logical filtering with sample CSV data
│   ├── python-logic-assignment2/         # Complex condition evaluation on student records
│   ├── python-loops-assignment/          # Iteration patterns, for/while loops, counters
│   ├── python-functions-assignment/      # Modular function design, parameters, return values
│   └── python-data-assignment/           # Built-in data structures (Lists, Tuples, Dictionaries, Sets)
│   └── python-data-assignment1/          # Data manipulation and problem solving
│
├── 📄 File I/O & Serialization
│   ├── python-files-assignment/          # File handling (read, write, append) and logging
│   └── python-json-assignment/           # Parsing, validation, and serialization of JSON payloads
│
├── 📊 Numerical Computing & Data Wrangling
│   ├── python-numpy-assignment/          # Array operations, normalization (Z-score), reshaping
│   └── pandas-cleaning-grouping/         # Data cleaning, null handling, aggregation & groupby
│
├── 📈 Visualization & Exploratory Data Analysis (EDA)
│   ├── matplotlib-visualization-assignment/ # Static line plots, scatter plots, bar charts
│   ├── plotly-visualization-assignment/     # Interactive loss curves and chart annotations
│   └── eda-checklist/                    # Full EDA pipeline (inspection, distribution, outliers, correlations)
│
├── 🗄️ Relational Databases & SQL
│   ├── sql-thinking-in-tables/          # Database mental models, schemas, keys, integrity in AI
│   ├── sql-query-assignment/             # Table creation, filtering, sorting, aliases, distinct
│   └── sql-join-assignment/              # INNER/LEFT joins, multi-table aggregations, grouping
│
└── main.py                               # Sanity checks and repo entry point
```

---

## 📚 Curriculum & Modules Breakdown

### 1. Python Core & Flow Control
* **Fundamentals & Arithmetic**: Working with variables, type conversions, and user inputs (`python-fundamentals-assignment`).
* **Conditional Logic**: Decision trees, comparison operators, and threshold filters (`python-logic-assignment*`).
* **Loops & Iterations**: Traversing sequences, accumulating statistics, and building iterative routines (`python-loops-assignment`).
* **Modular Functions**: Writing clean, reusable, testable functions with parameter handling (`python-functions-assignment`).
* **Data Structures**: Efficient usage of Python's built-in collections—lists, dictionaries, sets, and tuples (`python-data-assignment*`).

### 2. File Systems, Logging & JSON
* **File Operations**: Safe file read/write workflows with context managers (`with open`), computing metrics and saving audit logs (`python-files-assignment`).
* **JSON Serialization**: Handling structured API responses, validating confidence thresholds, and persisting JSON objects (`python-json-assignment`).

### 3. Numerical Computing & Data Processing
* **NumPy**: Vectorized mathematics, mean/std calculation, statistical normalization, and multidimensional array reshaping (`python-numpy-assignment`).
* **Pandas**: Handling missing data (`fillna`, `dropna`), column transformations, and multi-level data aggregations using `groupby` (`pandas-cleaning-grouping`).

### 4. Data Visualization & EDA
* **Matplotlib**: Plotting training loss dynamics, scatter visualizations, and model accuracy comparisons (`matplotlib-visualization-assignment`).
* **Plotly**: Building rich, interactive visualizations with annotations and dynamic tooltips (`plotly-visualization-assignment`).
* **Exploratory Data Analysis**: Systematic checklist covering shape inspection, missing value profiling, distribution analysis, box-plot outlier detection, and feature relationship mapping (`eda-checklist`).

### 5. Relational Databases & SQL
* **Thinking in Tables**: Theoretical foundations of relational databases, primary keys, foreign keys, schema integrity, and why structured data is critical for AI systems (`sql-thinking-in-tables`).
* **SQL Queries**: Table DDL/DML, conditional filtering (`WHERE`, `AND`, `OR`, `NOT`), sorting (`ORDER BY`), and limits (`LIMIT`) (`sql-query-assignment`).
* **SQL Joins & Aggregations**: Relational joins (`INNER JOIN`, `LEFT JOIN`), detecting orphaned records (`IS NULL`), and multi-table analytics (`GROUP BY`, `SUM`, `AVG`) (`sql-join-assignment`).

---

## 🚀 Getting Started

### Prerequisites
- [Python 3.10+](https://www.python.org/downloads/) installed.
- Git installed on your system.

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abhineet115/myFirstRepoinAgenticSystems.git
   cd myFirstRepoinAgenticSystems
   ```

2. **Create and activate a virtual environment:**
   - **Windows (PowerShell):**
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
   - **Linux / macOS:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install required dependencies:**
   ```bash
   pip install numpy pandas matplotlib plotly
   ```

---

## 💻 Running the Code

You can run any module or assignment directly via Python. Here are some examples:

### Run Exploratory Data Analysis (EDA)
```bash
python eda-checklist/iris_eda.py
```

### Run NumPy Normalization Exercise
```bash
python python-numpy-assignment/q1_numpy.py
```

### Run Pandas Data Cleaning & Aggregation
```bash
python pandas-cleaning-grouping/q1.py
```

### Run Interactive Plotly Visualizations
```bash
python plotly-visualization-assignment/plotly_visualization.py
```

### Run File Processing & Logging Script
```bash
cd python-files-assignment
python main.py
```

---

## 🎯 Next Steps in Agentic AI

This repository establishes the bedrock for building autonomous, intelligent systems. Upcoming concepts and extensions include:
- 🤖 **LLM Tool Calling & Function Execution**
- 🧠 **Agent Memory & Context Management (SQL + Vector Databases)**
- ⚡ **Multi-Agent Orchestration & Workflow Automation**
- 🔄 **Autonomous Feedback Loops & Evaluation Pipelines**

---

## 👤 Author

Developed and maintained by **Abhineet** ([@abhineet115](https://github.com/abhineet115)).

---

⭐ *If you find this repository helpful as a learning foundation for Agentic Systems, feel free to star the repo!*
