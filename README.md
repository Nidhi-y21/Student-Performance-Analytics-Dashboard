# Student-Performance-Analytics-Dashboard

This project analyzes student performance data to identify trends, correlations, and at-risk students for early academic intervention.

## 🔍 Problem Statement

Institutions need early warnings for students who might fail or drop out. This dashboard helps identify such students using performance metrics.

## 🎯 Objective

* Analyze student data (marks, attendance, login activity)
* Identify top-performing and at-risk students
* Generate interactive and visual insights

## 📁 Files

* `student_dashboard.py`: Main script for data generation, analysis, and visualization
* `student_performance_data.csv`: Generated mock dataset
* `correlation_heatmap.png`: Heatmap showing correlation between features

## 📊 Features

* Descriptive statistics (averages of marks, attendance, logins)
* Correlation heatmap
* Visualization of top and at-risk students
* Distribution plot of marks
* Scatter plot showing relationship between attendance and marks

## 🛠️ Tech Stack

* Python 3
* pandas
* numpy
* seaborn
* matplotlib
* plotly (interactive graphs)

## 🚀 How to Run

1. Clone this repo
2. Install required packages:

   ```bash
   pip install pandas numpy seaborn matplotlib plotly
   ```
3. Run the script:

   ```bash
   python student_dashboard.py
   ```

## 📌 Note

* Ensure you have internet access to view interactive Plotly charts.
* PNG export for Plotly is not supported without `kaleido`. Visuals are displayed interactively.

## 📬 Contact

For questions or contributions, feel free to open an issue or pull request.
