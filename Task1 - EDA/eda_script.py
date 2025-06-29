import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading CSV file 
df = pd.read_csv('data.csv')

#Summary
print("Data Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())

#Histogram
df.select_dtypes(include=['number']).hist(figsize=(10,8))
plt.suptitle('Distribution of Numeric Columns', fontsize=16)
plt.tight_layout()
plt.show()

#Correlation
numeric_df = df.select_dtypes(include=['number'])
plt.figure(figsize=(8,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

#Bar plot
plt.figure(figsize=(8,6))
sns.barplot(x='Department', y='Salary', data=df, estimator='mean', ci=None)
plt.title('Average Salary by Department')
plt.ylabel('Average Salary ($)')
plt.show()

#Box plot
plt.figure(figsize=(8,6))
sns.boxplot(x='Department', y='Performance_Rating', data=df)
plt.title('Performance Rating by Department')
plt.show()
