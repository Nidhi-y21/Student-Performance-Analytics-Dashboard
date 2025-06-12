# Student Performance Analytics Dashboard - Full Working Version with Mock Data (No Streamlit)

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

np.random.seed(42)
n_students = 100
data = {
    'Student_ID': [f"S{i:03d}" for i in range(1, n_students + 1)],
    'Name': [f"Student_{i}" for i in range(1, n_students + 1)],
    'Marks (%)': np.clip(np.random.normal(65, 15, n_students), 0, 100),
    'Attendance (%)': np.clip(np.random.normal(80, 10, n_students), 40, 100),
    'Logins': np.random.poisson(12, n_students)
}
df = pd.DataFrame(data)

# Save data to CSV
df.to_csv("student_performance_data.csv", index=False)

print("=== Student Performance Analytics Dashboard ===")
print("\n--- Student Data ---")
print(df)

print("\n--- Averages ---")
print("Average Marks:", round(df['Marks (%)'].mean(), 2))
print("Average Attendance:", round(df['Attendance (%)'].mean(), 2))
print("Average Logins:", round(df['Logins'].mean(), 2))

print("\n--- Correlation Heatmap ---")
corr = df[['Marks (%)', 'Attendance (%)', 'Logins']].corr()
fig1, ax1 = plt.subplots()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax1)
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()

print("\n--- Top Performing Students ---")
top_students = df[df['Marks (%)'] > 75].sort_values(by='Marks (%)', ascending=False)
print(top_students[['Name', 'Marks (%)', 'Attendance (%)']].head(10))

print("\n--- At-Risk Students ---")
at_risk = df[(df['Marks (%)'] < 40) | (df['Attendance (%)'] < 60)].sort_values(by='Marks (%)')
print(at_risk[['Name', 'Marks (%)', 'Attendance (%)']].head(10))

print("\n--- Marks Distribution ---")
fig2 = px.histogram(df, x="Marks (%)", nbins=20, title="Distribution of Marks")
fig2.show()

print("\n--- Attendance vs Marks ---")
fig3 = px.scatter(df, x='Attendance (%)', y='Marks (%)', color='Logins',
                  title='Attendance vs Marks Colored by Logins', size='Logins')
fig3.show()

print("\nDashboard generation complete. Data saved to 'student_performance_data.csv'.")

