import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import re


df = pd.read_csv("company_dataset.csv")
df.columns = df.columns.str.strip().str.lower()

df = df.head(30)

hq_col = 'hq'
top_hq = df[hq_col].dropna().unique()[:10]
df = df[df[hq_col].isin(top_hq)]

for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].mean())


def parse_employees(val):
    if pd.isna(val):
        return np.nan
    val = str(val).lower()

    num = re.findall(r'\d+\.?\d*', val)
    if not num:
        return np.nan

    num = float(num[0])

    if 'lakh' in val:
        num *= 1e5
    elif 'crore' in val:
        num *= 1e7

    return num

df['employees'] = df['employees'].apply(parse_employees)


df = df.dropna(subset=['employees'])
df = df[df['employees'] > 0]


def remove_outliers(data, col):
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    return data[(data[col] >= Q1 - 1.5 * IQR) & (data[col] <= Q3 + 1.5 * IQR)]

for col in df.select_dtypes(include=np.number).columns:
    if col != 'employees':  
        df = remove_outliers(df, col)


num_cols = [c for c in df.select_dtypes(include=np.number).columns if c != 'employees']
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])


if len(df) > 0:
    plt.figure()
    plt.pie(df['employees'], labels=df['name'], autopct='%1.1f%%')
    plt.title("Employees Distribution")
    plt.show()
else:
    print("No valid data for pie chart after cleaning.")


df_sorted = df.sort_values(by='review_count', ascending=False)

plt.figure()
plt.barh(df_sorted['name'], df_sorted['review_count'])
plt.gca().invert_yaxis()
plt.title("Funnel Chart (Reviews)")
plt.show()

print("\nCompany Headquarters:")
print(df[['name', 'hq']])


plt.figure()
plt.bar(df['name'], df['ratings'])
plt.xticks(rotation=90)
plt.title("Company Ratings")
plt.show()


df_year = df.groupby('years').mean(numeric_only=True)

plt.figure()
plt.plot(df_year.index, df_year['ratings'])
plt.title("Year-wise Trend")
plt.xlabel("Year")
plt.ylabel("Average Rating")
plt.show()
