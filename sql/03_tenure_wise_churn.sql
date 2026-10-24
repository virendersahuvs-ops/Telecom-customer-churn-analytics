USE telecom_churn;

SELECT
    CASE
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '49-72 Months'
    END AS tenure_group,

    COUNT(*) AS total_customers,

    SUM(LOWER(LEFT(TRIM(Churn), 1)) = 'y')
        AS churned_customers,

    SUM(LOWER(LEFT(TRIM(Churn), 1)) = 'n')
        AS retained_customers,

    ROUND(
        100.0 * SUM(LOWER(LEFT(TRIM(Churn), 1)) = 'y')
        / COUNT(*), 2
    ) AS churn_rate_pct

FROM customers
GROUP BY tenure_group
ORDER BY MIN(tenure);