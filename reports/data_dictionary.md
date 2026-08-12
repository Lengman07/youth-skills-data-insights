# Youth Skills Program — Data Dictionary

## Dataset Overview

The `participants.csv` dataset contains 15 participant records and 12 variables used to evaluate youth skills training outcomes.

| Column | Data Type | Description | Example |
|---|---|---|---|
| `participant_id` | String | Unique identifier assigned to each participant. | P001 |
| `name` | String | Participant name. | Akosua Mensah |
| `age` | Integer | Participant age in years. | 24 |
| `gender` | Categorical | Participant gender category. | Female |
| `region` | Categorical | Region associated with the participant. | Greater Accra |
| `education` | Categorical | Highest recorded education level. | Tertiary |
| `program` | Categorical | Training program completed by the participant. | Data Analytics |
| `attendance_pct` | Integer | Percentage of training sessions attended. | 92 |
| `pre_score` | Integer | Assessment score recorded before training. | 48 |
| `post_score` | Integer | Assessment score recorded after training. | 78 |
| `employment_status` | Categorical | Employment status recorded after training. | Employed |
| `satisfaction` | Integer | Participant satisfaction rating on a 1–5 scale. | 5 |

## Derived Variables

### `score_improvement`

Calculated as:

`post_score - pre_score`

It measures the change in participant assessment score after training.

### `performance_flag`

Used to identify participants who may require additional support.

A participant is classified as **Needs Attention** when:

- Attendance is below 75%
- Score improvement is below 15 points

Otherwise, the participant is classified as **On Track**.

## Categorical Values

### Gender

- Female
- Male

### Region

- Greater Accra
- Ashanti
- Central
- Eastern
- Western

### Education

- Tertiary
- SHS

### Program

- Data Analytics
- Web Development
- Cybersecurity

### Employment Status

- Employed
- Unemployed

## Data Quality

The dataset was checked for:

- Missing values
- Duplicate records
- Data types
- Valid categorical values
- Numeric ranges

No missing values or duplicate rows were identified in the dataset.

## Important Limitations

The dataset contains only 15 participants. Therefore, findings should be treated as observations from this sample and not generalized to the wider youth training population without additional data.