USE telecom_churn;

WITH contract_churn AS (
    SELECT
        Contract,
        COUNT(*) AS total_customers,

        SUM(
            LOWER(LEFT(TRIM(Churn), 1)) = 'y'
        ) AS churned_customers,

        ROUND(
            100.0 * SUM(
                LOWER(LEFT(TRIM(Churn), 1)) = 'y'
            ) / COUNT(*),
            2
        ) AS churn_rate_pct

    FROM customers
    GROUP BY Contract
)

SELECT
    Contract,
    total_customers,
    churned_customers,
    churn_rate_pct,

    RANK() OVER (
        ORDER BY churn_rate_pct DESC
    ) AS churn_risk_rank

FROM contract_churn
ORDER BY churn_risk_rank;