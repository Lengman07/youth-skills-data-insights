-- Youth Skills Program
-- SQL Analysis

-- 1. Total number of participants
SELECT COUNT(*) AS total_participants
FROM participants;

-- 2. Average attendance rate
SELECT ROUND(AVG(CAST(attendance_pct AS REAL)), 2) AS average_attendance
FROM participants;

-- 3. Average score improvement
SELECT ROUND(
    AVG(
        CAST(post_score AS REAL) - CAST(pre_score AS REAL)
    ), 2
) AS average_score_improvement
FROM participants;

-- 4. Overall employment rate
SELECT ROUND(
    AVG(
        CASE
            WHEN employment_status = 'Employed' THEN 1.0
            ELSE 0.0
        END
    ) * 100,
    2
) AS employment_rate
FROM participants;

-- 5. Learning improvement by training program
SELECT
    program,
    COUNT(*) AS participants,
    ROUND(
        AVG(
            CAST(post_score AS REAL) - CAST(pre_score AS REAL)
        ), 2
    ) AS average_improvement
FROM participants
GROUP BY program
ORDER BY average_improvement DESC;

-- 6. Employment rate by training program
SELECT
    program,
    COUNT(*) AS participants,
    ROUND(
        AVG(
            CASE
                WHEN employment_status = 'Employed' THEN 1.0
                ELSE 0.0
            END
        ) * 100,
        2
    ) AS employment_rate
FROM participants
GROUP BY program
ORDER BY employment_rate DESC;

-- 7. Learning improvement by region
SELECT
    region,
    COUNT(*) AS participants,
    ROUND(
        AVG(
            CAST(post_score AS REAL) - CAST(pre_score AS REAL)
        ), 2
    ) AS average_improvement
FROM participants
GROUP BY region
ORDER BY average_improvement DESC;

-- 8. Identify participants needing attention
-- Criteria: attendance below 75% AND score improvement below 15 points

SELECT
    participant_id,
    name,
    program,
    CAST(attendance_pct AS INTEGER) AS attendance_pct,
    CAST(post_score AS INTEGER) - CAST(pre_score AS INTEGER) AS score_improvement,
    employment_status
FROM participants
WHERE CAST(attendance_pct AS INTEGER) < 75
  AND (
      CAST(post_score AS INTEGER) - CAST(pre_score AS INTEGER)
  ) < 15
ORDER BY score_improvement ASC;