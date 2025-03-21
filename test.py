import pandas as pd

# Specify the file path
file_path = "sample.xlsx"  # Change to your actual file name

# Check the file extension and read accordingly
if file_path.endswith(".csv"):
    df = pd.read_csv(file_path)  # Read CSV
elif file_path.endswith((".xls", ".xlsx")):
    df = pd.read_excel(file_path)  # Read Excel
else:
    raise ValueError("Unsupported file format. Use CSV or Excel (.xls, .xlsx)")

# Define table name
table_name = "your_table_name"

# Initialize list for SQL statements
sql_statements = []

# Generate SQL INSERT statements with column names
for _, row in df.iterrows():
    values = []
    for val in row.values:
        if pd.isna(val):  # Convert NaN to NULL
            values.append("NULL")
        else:
            # Escape single quotes to prevent SQL errors
            escaped_value = str(val).replace("'", "''")
            values.append(f"'{escaped_value}'")  # Convert to string and add quotes
    
    columns = ", ".join(df.columns)  # Use column names in SQL statement
    sql_statements.append(f"INSERT INTO {table_name} ({columns}) VALUES ({', '.join(values)});")

# Save to an SQL file
sql_file_path = "output.sql"
with open(sql_file_path, "w", encoding="utf-8") as f:
    f.write("\n".join(sql_statements))

print(f"SQL file '{sql_file_path}' has been created successfully!")
