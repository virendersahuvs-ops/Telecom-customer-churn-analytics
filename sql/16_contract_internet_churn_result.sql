USE telecom_churn;

SELECT
    Contract,
    InternetService,
    COUNT(*) AS total_customers,
    SUM(LOWER(LEFT(TRIM(Churn), 1)) = 'y')
        AS churned_customers,
    ROUND(
        100.0 * SUM(LOWER(LEFT(TRIM(Churn), 1)) = 'y')
        / COUNT(*),
        2
    ) AS churn_rate_pct
FROM customers
GROUP BY Contract, InternetService
HAVING COUNT(*) >= 30
ORDER BY churn_rate_pct DESC;