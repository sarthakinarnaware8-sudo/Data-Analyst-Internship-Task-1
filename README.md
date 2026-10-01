# Data-Analyst-Internship-Task-1
Data cleaning and preprocessing of the Netflix Movies and TV Shows dataset using Python and Pandas.

Netflix Data Cleaning and Preprocessing

📌 Project Overview

This project was completed as part of an internship task focused on data cleaning and preprocessing.

The project uses the Netflix Movies and TV Shows dataset and demonstrates how raw data can be inspected, cleaned, validated, and prepared for further analysis using Python and Pandas.

---

🎯 Objectives

The main objectives of this task were to:

- Load and inspect the raw dataset
- Understand the dataset structure
- Check column names and data types
- Identify missing values
- Identify duplicate records
- Remove duplicate rows
- Check data consistency
- Validate numerical and categorical data
- Save the cleaned dataset
- Document all cleaning steps
- Upload the complete project to GitHub

---

🛠️ Technologies Used

Technology| Purpose
Python| Data cleaning and preprocessing
Pandas| Data manipulation and analysis
VS Code| Writing and running Python code
GitHub| Project documentation and version control
CSV| Dataset storage format

---

📊 Dataset Information

The dataset contains information about movies and TV shows available on Netflix.

Dataset Size

The original dataset contains:

- Rows: 8,807
- Columns: 12

Dataset Columns

Column| Description
"show_id"| Unique identifier for each title
"type"| Type of content, such as Movie or TV Show
"title"| Title of the movie or TV show
"director"| Director of the title
"cast"| Cast members
"country"| Country or countries associated with the title
"date_added"| Date the title was added to Netflix
"release_year"| Original release year
"rating"| Content rating
"duration"| Duration of a movie or number of seasons
"listed_in"| Genre or category
"description"| Description of the title

---

🔍 Data Inspection

The dataset was first loaded into Python using Pandas.

import pandas as pd

df = pd.read_csv("netflix_titles.csv")

print(df.shape)
print(df.info())

The dataset was then inspected to understand its structure, columns, data types, missing values, and duplicate records.

---

🧹 Data Cleaning Process

1. Dataset Loading

The raw Netflix dataset was loaded using Pandas.

df = pd.read_csv("netflix_titles.csv")

---

2. Dataset Shape Check

The number of rows and columns was checked using:

print("Dataset Shape:", df.shape)

The original dataset contained 8,807 rows and 12 columns.

---

3. Column Name Check

The column names were checked to make sure that the dataset headers were correctly identified.

print(df.columns)

The dataset contains the following columns:

show_id
type
title
director
cast
country
date_added
release_year
rating
duration
listed_in
description

---

4. Missing Value Check

Missing values were identified using:

print(df.isnull().sum())

This helped identify columns containing incomplete information.

Missing values were reviewed before deciding how they should be handled.

---

5. Duplicate Row Check

Duplicate records were checked using:

duplicates = df.duplicated().sum()

print("Number of duplicate rows:", duplicates)

This was done to ensure that repeated records did not remain in the final dataset.

---

6. Removing Duplicate Rows

Duplicate rows were removed using:

df = df.drop_duplicates()

The dataset was then checked again to confirm that duplicate rows had been removed.

---

7. Data Type Check

The data types of all columns were checked using:

print(df.dtypes)

This helped identify whether the columns contained appropriate data types for further analysis.

---

8. Release Year Validation

The "release_year" column was checked to identify the range of years present in the dataset.

print("Minimum:", df["release_year"].min())
print("Maximum:", df["release_year"].max())

The observed range was:

- Minimum year: 1925
- Maximum year: 2024

---

9. Final Dataset Validation

After completing the cleaning process, the dataset was checked again for:

- Duplicate rows
- Missing values
- Correct column names
- Data types
- Valid values
- Overall dataset structure

This ensured that the final dataset was ready for further analysis.

---

📄 Cleaning Summary

A separate file named "cleaning_summary.md" has been included in this repository.

It contains a short description of:

- The original dataset
- Issues identified
- Cleaning operations performed
- Final validation

---

📸 Screenshots

Screenshots documenting the data-cleaning process are included in the "screenshots" folder.

The screenshots provide evidence of:

1. Raw dataset
2. Dataset information
3. Missing-value check
4. Duplicate check
5. Duplicate removal
6. Data-type check
7. Release-year validation
8. Final cleaned dataset

---

📈 Final Result

The Netflix dataset was successfully inspected and cleaned using Python and Pandas.

The cleaning process addressed common data-quality issues and produced a cleaned dataset that can be used for further exploratory data analysis and visualization.

---

🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Python-based data cleaning
- Pandas data manipulation
- Dataset inspection
- Missing-value identification
- Duplicate detection and removal
- Data-type inspection
- Data validation
- Data-quality documentation
- GitHub project organization

---

🚀 Future Scope

The cleaned dataset can be used for further analysis such as:

- Netflix content trends
- Movies vs. TV Shows analysis
- Release-year trends
- Country-wise content analysis
- Genre analysis
- Rating distribution
- Content growth over time
- Power BI dashboards and visualizations

---

👩‍💻 Author

Sarthaki Narnaware

B.Tech Electronics & Telecommunication Engineering
St. Vincent Pallotti College of Engineering and Technology, Nagpur

---

📌 Conclusion

This project demonstrates a basic but practical data-cleaning workflow using Python and Pandas. The raw Netflix dataset was inspected, cleaned, validated, and documented to make it suitable for further analysis.
