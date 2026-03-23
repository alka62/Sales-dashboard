!pip install seaborn plotly --quiet

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load dataset
df = pd.read_csv('/content/sales_data (4).csv')

# Clean column names (IMPORTANT FIX)
df.columns = df.columns.str.strip()

print("Columns in dataset:", df.columns)

# ==============================
# AUTO DETECT COLUMNS
# ==============================
# Try to guess columns
cat_col = None
num_col = None

for col in df.columns:
    if df[col].dtype == 'object':
        cat_col = col
        break

for col in df.columns:
    if df[col].dtype != 'object':
        num_col = col
        break

print(f"Using Category Column: {cat_col}")
print(f"Using Numeric Column: {num_col}")

# ==============================
# PLOTS
# ==============================

# 1. Boxplot
plt.figure()
sns.boxplot(x=cat_col, y=num_col, data=df)
plt.title('Box Plot')
plt.show()

# 2. Violin Plot
plt.figure()
sns.violinplot(x=cat_col, y=num_col, data=df)
plt.title('Violin Plot')
plt.show()

# 3. Heatmap
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# 4. Plotly Bar
fig1 = px.bar(df, x=cat_col, y=num_col, color=cat_col,
              title="Interactive Bar Chart")
fig1.show()

# 5. Scatter (if 2 numeric columns exist)
num_cols = df.select_dtypes(include=['number']).columns

if len(num_cols) >= 2:
    fig2 = px.scatter(df, x=num_cols[0], y=num_cols[1],
                      title="Scatter Plot")
    fig2.show()

# ==============================
# INSIGHTS
# ==============================
print("\n🔍 Insights:")

if cat_col and num_col:
    top = df.groupby(cat_col)[num_col].sum().idxmax()
    print(f"• Top Category: {top}")

print("✅ Dashboard Generated Successfully!")
