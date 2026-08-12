import streamlit as st
import pandas as pd
import plotly.express as px
# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Youth Skills Data Insights",
    page_icon="📊",
    layout="wide"
)


# ==========================================
# 2. LOAD DATA
# ==========================================

df = pd.read_csv("data/participants.csv")


# ==========================================
# 3. FEATURE ENGINEERING
# ==========================================

# Calculate score improvement
df["score_improvement"] = df["post_score"] - df["pre_score"]

# Create performance flag
df["performance_flag"] = "On Track"

df.loc[
    (df["attendance_pct"] < 75) &
    (df["score_improvement"] < 15),
    "performance_flag"
] = "Needs Attention"


# ==========================================
# 4. DASHBOARD TITLE
# ==========================================

st.title("Youth Skills Data Insights")

st.markdown(
    "### Youth Skills Training Program Performance Dashboard"
)

st.write(
    "This dashboard evaluates participant attendance, learning "
    "improvement, satisfaction, and employment outcomes."
)


# ==========================================
# 5. SIDEBAR FILTERS
# ==========================================

st.sidebar.header("Filters")

selected_program = st.sidebar.multiselect(
    "Training Program",
    options=sorted(df["program"].unique()),
    default=sorted(df["program"].unique())
)

selected_region = st.sidebar.multiselect(
    "Region",
    options=sorted(df["region"].unique()),
    default=sorted(df["region"].unique())
)

selected_gender = st.sidebar.multiselect(
    "Gender",
    options=sorted(df["gender"].unique()),
    default=sorted(df["gender"].unique())
)

selected_education = st.sidebar.multiselect(
    "Education",
    options=sorted(df["education"].unique()),
    default=sorted(df["education"].unique())
)

selected_employment = st.sidebar.multiselect(
    "Employment Status",
    options=sorted(df["employment_status"].unique()),
    default=sorted(df["employment_status"].unique())
)


# ==========================================
# 6. APPLY FILTERS
# ==========================================

filtered_df = df[
    df["program"].isin(selected_program) &
    df["region"].isin(selected_region) &
    df["gender"].isin(selected_gender) &
    df["education"].isin(selected_education) &
    df["employment_status"].isin(selected_employment)
]

st.sidebar.write(
    f"Filtered participants: {len(filtered_df)}"
)


# ==========================================
# 7. CALCULATE FILTERED KPIs
# ==========================================

total_participants = len(filtered_df)

average_attendance = filtered_df["attendance_pct"].mean()

average_improvement = filtered_df["score_improvement"].mean()

employment_rate = (
    (filtered_df["employment_status"] == "Employed").mean() * 100
)

average_satisfaction = filtered_df["satisfaction"].mean()

needs_attention = (
    (filtered_df["performance_flag"] == "Needs Attention").mean() * 100
)


# ==========================================
# 8. DISPLAY KPI CARDS
# ==========================================

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Participants",
    total_participants
)

col2.metric(
    "Avg Attendance",
    f"{average_attendance:.1f}%"
)

col3.metric(
    "Avg Improvement",
    f"{average_improvement:.2f}"
)

col4.metric(
    "Employment Rate",
    f"{employment_rate:.2f}%"
)

col5.metric(
    "Avg Satisfaction",
    f"{average_satisfaction:.2f}/5"
)


# ==========================================
# 9. PERFORMANCE OVERVIEW
# ==========================================

st.divider()

st.subheader("Performance Overview")

st.metric(
    "Needs Attention",
    f"{needs_attention:.1f}%"
)

# ==========================================
# 10. PROGRAM PERFORMANCE
# ==========================================

st.divider()

st.subheader("Program Performance")

program_performance = (
    filtered_df
    .groupby("program", as_index=False)
    .agg(
        participants=("participant_id", "count"),
        average_attendance=("attendance_pct", "mean"),
        average_improvement=("score_improvement", "mean"),
        average_satisfaction=("satisfaction", "mean")
    )
)

fig_program = px.bar(
    program_performance,
    x="program",
    y="average_improvement",
    title="Average Score Improvement by Program",
    labels={
        "program": "Training Program",
        "average_improvement": "Average Score Improvement"
    },
    text_auto=".1f"
)

st.plotly_chart(
    fig_program,
    use_container_width=True
)


# ==========================================
# 11. EMPLOYMENT BY PROGRAM
# ==========================================

st.subheader("Employment Rate by Program")

employment_by_program = (
    filtered_df
    .groupby("program")
    .agg(
        employment_rate=(
            "employment_status",
            lambda x: (x == "Employed").mean() * 100
        )
    )
    .reset_index()
)

fig_employment = px.bar(
    employment_by_program,
    x="program",
    y="employment_rate",
    title="Employment Rate by Program",
    labels={
        "program": "Training Program",
        "employment_rate": "Employment Rate (%)"
    },
    text_auto=".1f"
)

st.plotly_chart(
    fig_employment,
    use_container_width=True
)

# ==========================================
# 12. REGIONAL PERFORMANCE
# ==========================================

st.divider()

st.subheader("Regional Performance")

region_performance = (
    filtered_df
    .groupby("region", as_index=False)
    .agg(
        participants=("participant_id", "count"),
        average_attendance=("attendance_pct", "mean"),
        average_improvement=("score_improvement", "mean"),
        average_satisfaction=("satisfaction", "mean")
    )
)

fig_region = px.bar(
    region_performance,
    x="region",
    y="average_improvement",
    title="Average Score Improvement by Region",
    labels={
        "region": "Region",
        "average_improvement": "Average Score Improvement"
    },
    text_auto=".1f"
)

st.plotly_chart(
    fig_region,
    use_container_width=True
)


# ==========================================
# 13. ATTENDANCE VS SCORE IMPROVEMENT
# ==========================================

st.subheader("Attendance vs. Score Improvement")

fig_scatter = px.scatter(
    filtered_df,
    x="attendance_pct",
    y="score_improvement",
    color="employment_status",
    hover_data=[
        "participant_id",
        "program",
        "region"
    ],
    title="Attendance vs. Score Improvement",
    labels={
        "attendance_pct": "Attendance (%)",
        "score_improvement": "Score Improvement",
        "employment_status": "Employment Status"
    }
)

st.plotly_chart(
    fig_scatter,
    use_container_width=True
)

# ==========================================
# 14. PARTICIPANT PERFORMANCE
# ==========================================

st.divider()

st.subheader("Participant Performance")

st.write(
    "Participants classified as 'Needs Attention' may require "
    "additional monitoring or support based on attendance and "
    "score improvement."
)

needs_attention_df = filtered_df[
    filtered_df["performance_flag"] == "Needs Attention"
].copy()

if len(needs_attention_df) > 0:

    display_columns = [
        "participant_id",
        "name",
        "program",
        "attendance_pct",
        "score_improvement",
        "employment_status",
        "performance_flag"
    ]

    st.dataframe(
        needs_attention_df[display_columns],
        use_container_width=True,
        hide_index=True
    )

else:

    st.success(
        "No participants currently meet the Needs Attention criteria."
    )

# ==========================================
# 15. KEY INSIGHTS
# ==========================================

st.divider()

st.subheader("Key Insights")

st.markdown(
    """
    **1. Overall training performance**

    Participants achieved an average score improvement of
    **23.73 points**, with average attendance of **83.2%**.

    **2. Program performance**

    Data Analytics recorded the highest average score improvement
    at **25.0 points**, while Cybersecurity recorded the highest
    observed employment rate at **75%**.

    **3. Attendance and learning outcomes**

    The analysis found a strong positive association between
    attendance and score improvement. Participants with higher
    attendance generally achieved greater learning gains.

    **4. Employment**

    The overall observed employment rate was **66.67%**.
    Employment outcomes varied across programs and education levels.

    **5. Participants requiring attention**

    **20% of participants** were classified as "Needs Attention"
    based on the project's attendance and score-improvement criteria.
    These participants may benefit from early intervention and
    additional support.
    """
)


# ==========================================
# 16. RECOMMENDATIONS
# ==========================================

st.subheader("Recommendations")

st.markdown(
    """
    - Strengthen attendance monitoring and early intervention.

    - Provide targeted academic support to participants showing
      low attendance and low learning improvement.

    - Investigate employment pathways and employer demand across
      training programs.

    - Provide additional foundational and employability support
      for participants entering with SHS-level education.

    - Continue collecting data across multiple cohorts to determine
      whether the observed patterns remain consistent.
    """
)