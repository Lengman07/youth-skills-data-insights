# Youth Skills Data Insights

Data analysis and insights project evaluating youth skills training program outcomes across learning performance, attendance, satisfaction, and employment.

## Project Overview

This project analyzes participant data from a youth skills training program to understand how training outcomes vary across programs, regions, education levels, and participant characteristics.

The analysis focuses on transforming participant-level data into actionable insights that can support program monitoring, evaluation, and decision-making.

## Business Questions

The project seeks to answer:

- How much did participants improve after training?
- Which training programs produced the strongest learning outcomes?
- Which programs had the highest observed employment rates?
- Is attendance associated with learning improvement?
- How do outcomes vary across regions?
- How does education level relate to employment outcomes?
- Which participants may require additional support?

## Dataset

The dataset contains **15 participants** and 12 variables:

- Participant ID
- Name
- Age
- Gender
- Region
- Education
- Training Program
- Attendance Percentage
- Pre-training Score
- Post-training Score
- Employment Status
- Satisfaction

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQL
- SQLite
- Jupyter Notebook
- Git & GitHub

## Analysis Process

The project follows a structured data analytics workflow:

1. Data collection and preparation
2. Data quality validation
3. Exploratory data analysis
4. KPI development
5. Program performance analysis
6. Employment analysis
7. Regional and demographic analysis
8. Participant performance flagging
9. SQL analysis
10. Dashboard development
11. Insights and recommendations

## Key Findings

### Overall Performance

- **15 participants** were analyzed.
- Average attendance was **83.2%**.
- Average score improvement was **23.73 points**.
- Overall observed employment rate was **66.67%**.
- Average satisfaction was **4.13/5**.

### Program Performance

- **Data Analytics** recorded the highest average score improvement at **25.0 points**.
- **Cybersecurity** recorded the highest observed employment rate at **75%**.
- Data Analytics also recorded the highest average satisfaction at **4.33/5**.

### Attendance and Learning

A strong positive association was observed between attendance and score improvement, with a correlation of approximately **0.894**.

Employed participants had higher average attendance than unemployed participants:

- Employed: **90.1%**
- Unemployed: **69.4%**

### Education and Employment

The observed employment rate was:

- Tertiary: **90%**
- SHS: **20%**

Because the dataset contains only 15 participants, these findings should be interpreted as observations rather than causal conclusions.

### Participants Requiring Attention

Three participants, representing **20%** of the sample, were classified as "Needs Attention" based on the project criteria:

- Attendance below 75%
- Score improvement below 15 points

## Recommendations

1. Strengthen attendance monitoring and early intervention.
2. Provide targeted support to participants showing low attendance and low learning improvement.
3. Investigate employment pathways and employer demand across training programs.
4. Provide additional foundational and employability support for participants entering with SHS-level education.
5. Continue monitoring multiple cohorts to determine whether the observed patterns remain consistent.

## Project Structure

```text
youth-skills-data-insights/
│
├── data/
│   ├── participants.csv
│   ├── program_dashboard.csv
│   ├── region_dashboard.csv
│   └── employment_dashboard.csv
│
├── dashboard/
│
├── notebooks/
│   └── dti_analysis.ipynb
│
├── reports/
│   └── analysis_report.md
│
├── sql/
│   └── analysis.sql
│
├── README.md
└── .gitignore