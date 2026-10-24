USE telecom_churn;

SELECT
    CASE
        WHEN SeniorCitizen = 1 THEN 'Senior Citizen'
        ELSE 'Non-Senior Citizen'
    END AS customer_group,

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
GROUP BY customer_group
ORDER BY churn_rate_pct DESC;