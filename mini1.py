import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

server = "LAPTOP-LAC8A4E2\\SQLEXPRESS"
database = "sales_data"
driver = "ODBC Driver 17 for SQL Server"

conn_str = f"mssql+pyodbc://{server}/{database}?driver={driver}&trusted_connection=yes"
engine = create_engine(conn_str)

# conn = pyodbc.connect(
#     "DRIVER={SQL Server};"
#     "SERVER=LAPTOP-LAC8A4E2\\SQLEXPRESS;"
#     "DATABASE=sales_data;"
#     "Trusted_Connection=yes;"
# )

# cursor = conn.cursor()

queries = {
    "Total Sales per Branch": "SELECT branch, round(SUM(Total),2) AS total_sales FROM sales_data GROUP BY branch",
    "Sales by Product Category": "SELECT Product_line, round(SUM(Total),2) AS total_sales FROM sales_data GROUP BY Product_line",
    "Sales per Month": "SELECT FORMAT(Date, 'MMM') AS Month, ROUND(SUM(Total), 2) AS total_sales FROM sales_data GROUP BY FORMAT(Date, 'MMM') ORDER BY MIN(Date); ",
    "Avg Rating per Branch": "SELECT branch, AVG(Rating) AS avg_rating FROM sales_data GROUP BY branch",
}

# Fetching Data
dataframes = {title: pd.read_sql(query, engine) for title, query in queries.items()}

df_tsales = dataframes["Total Sales per Branch"]
print(df_tsales)
df_psales = dataframes["Sales by Product Category"]
print(df_psales)
df_msales = dataframes["Sales per Month"]
print(df_msales)
df_arating = dataframes["Avg Rating per Branch"]
print(df_arating)


# Create a 2x2 Subplot Layout
fig, axes = plt.subplots(2, 2, figsize=(12, 8))  # 2 rows, 2 columns

#graph 1
sns.barplot(x = 'branch', y='total_sales',data=df_tsales, ax=axes[0,0],palette='coolwarm')
axes[0, 0].set(title="Total sales per branch",xlabel="Branches",ylabel="Sales")

#graph 2
df_psales.plot(kind='pie',y='total_sales',labels=df_psales['Product_line'],autopct='%1.1f%%',cmap='viridis',ax=axes[0,1],legend=False)
axes[0,1].set(title="Sales by Product Category",xlabel="",ylabel="")

#graph 3
axes[1,0].plot(df_msales['Month'], df_msales['total_sales'], marker='o', color='b')
axes[1,0].set(title="Monthly Sale Trend",ylabel="Sales",xlabel="Month")

#graph
sns.barplot(x='branch', y='avg_rating', data=df_arating, ax=axes[1,1])
axes[1,1].set(title="Rating Distribution per Branch", xlabel="Branch", ylabel="Rating")

# Adjust layout
plt.tight_layout()
plt.show()

# Close Connection
# conn.close()

# Plot Graphs
# for ax, (title, df) in zip(axes.flat, dataframes.items()):
#     ax.bar(df.iloc[:, 0], df.iloc[:, 1], color=['#1995AD', '#A1D6E2', '#F1F1F2'])  # Custom colors
#     ax.set_title(title)
#     ax.set_xlabel(df.columns[0])
#     ax.set_ylabel(df.columns[1])
#     ax.tick_params(axis='x', rotation=30)
