USE telecom_churn;

SELECT
    CASE
        WHEN MonthlyCharges < 35 THEN 'Low Charges'
        WHEN MonthlyCharges < 70 THEN 'Medium Charges'
        ELSE 'High Charges'
    END AS charge_segment,

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
GROUP BY charge_segment
ORDER BY
    CASE charge_segment
        WHEN 'Low Charges' THEN 1
        WHEN 'Medium Charges' THEN 2
        ELSE 3
    END;