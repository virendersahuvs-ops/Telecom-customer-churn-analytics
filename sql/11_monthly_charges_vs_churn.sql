USE telecom_churn;

SELECT
    CASE
        WHEN LOWER(LEFT(TRIM(Churn), 1)) = 'y'
            THEN 'Churned'
        ELSE 'Retained'
    END AS customer_status,

    COUNT(*) AS total_customers,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges,
    ROUND(MIN(MonthlyCharges), 2) AS min_monthly_charges,
    ROUND(MAX(MonthlyCharges), 2) AS max_monthly_charges

FROM customers
GROUP BY customer_status
ORDER BY avg_monthly_charges DESC;