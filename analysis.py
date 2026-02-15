# ONLINE SALES DATA ANALYSIS PROJECT (WORKING VERSION)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

#  Load Online Dataset (WORKING LINK)
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

print("✅ Dataset Loaded Successfully!")
print("Shape:", df.shape)
print(df.head())

#  BASIC DATA INFO

print("\nColumn Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

#  KPI CALCULATIONS

total_revenue = df["total_bill"].sum()
average_bill = df["total_bill"].mean()
average_tip = df["tip"].mean()
total_customers = df.shape[0]

print("\n===== KPI SUMMARY =====")
print("Total Revenue:", round(total_revenue, 2))
print("Average Bill:", round(average_bill, 2))
print("Average Tip:", round(average_tip, 2))
print("Total Customers:", total_customers)

#  REVENUE BY DAY

revenue_by_day = df.groupby("day")["total_bill"].sum()
print("\nRevenue by Day:")
print(revenue_by_day)

plt.figure()
sns.barplot(x="day", y="total_bill", data=df)
plt.title("Revenue by Day")
plt.show()

#  BILL VS TIP ANALYSIS

plt.figure()
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.title("Total Bill vs Tip")
plt.show()

#  GENDER ANALYSIS

plt.figure()
sns.boxplot(x="sex", y="total_bill", data=df)
plt.title("Bill Distribution by Gender")
plt.show()

#  SMOKER ANALYSIS

plt.figure()
sns.boxplot(x="smoker", y="total_bill", data=df)
plt.title("Bill Distribution: Smoker vs Non-Smoker")
plt.show()

#  PARTY SIZE ANALYSIS

plt.figure()
sns.boxplot(x="size", y="total_bill", data=df)
plt.title("Bill by Party Size")
plt.show()