import pandas as pd

pd.set_option('display.max_columns', None)

# Load dataset
df = pd.read_csv("netflix_titles.csv", encoding='latin1')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nCleaned Column Names:")
print(df.columns)

# Check for duplicate rows
duplicates = df.duplicated().sum()

print("Number of duplicate rows:", duplicates)

# Remove duplicate rows
df = df.drop_duplicates()

print("Duplicate rows after cleaning:", df.duplicated().sum())

# Check missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing values
df["director"] = df["director"].fillna("Not Available")
df["cast"] = df["cast"].fillna("Not Available")
df["country"] = df["country"].fillna("Not Available")
df["date_added"] = df["date_added"].fillna("Not Available")
df["rating"] = df["rating"].fillna("Not Rated")
df["duration"] = df["duration"].fillna("Not Available")

# Check missing values after cleaning
print("Missing values after cleaning:")
print(df.isnull().sum())

# Check data types
print("Data types:")
print(df.dtypes)

# Convert date_added to datetime
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

print(df["date_added"].head())
print(df["date_added"].dtype)

print("Missing dates after conversion:", df["date_added"].isnull().sum())

# Keep invalid/missing dates as NaT
print("Missing dates:", df["date_added"].isnull().sum())

print("Unique ratings:")
print(df["rating"].unique())

print("Unique values in type:")
print(df["type"].unique())

print("Minimum release year:", df["release_year"].min())
print("Maximum release year:", df["release_year"].max())

print("Sample duration values:")
print(df["duration"].unique()[:20])

# Remove extra spaces from text columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

print("Text spacing cleaned successfully.")

print("Final duplicate rows:", df.duplicated().sum())

print("Final missing values:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)

print("Cleaned dataset saved successfully!")