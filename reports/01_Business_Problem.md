
# Telecom Customer Churn & Retention Analytics

## 1. Business Problem

A telecommunications company is experiencing customer churn.
The company needs to understand customer retention patterns,
identify customer segments with higher churn rates, and determine
which services, contracts, and customer characteristics are
associated with customers leaving.

## 2. Business Objective

- Calculate the overall customer churn rate.
- Analyze churn across contract types and customer tenure.
- Examine the relationship between monthly charges and churn.
- Identify services and payment methods associated with churn.
- Estimate monthly revenue associated with churned customers.
- Recommend practical customer retention strategies.

## 3. Dataset Overview

Dataset: IBM Telco Customer Churn

Initial inspection:
- Total records: 7,043
- Total columns: 21
- Unique customer IDs: 7,043
- Exact duplicate rows: 0
- Missing values reported by initial inspection: 0

## 4. Tools

- Excel: Data cleaning, formulas, Pivot Tables and KPIs
- MySQL: Business queries and customer segmentation
- Python: Data quality checks and exploratory data analysis
- Power BI: Interactive retention dashboard

## 5. Key Business Questions

1. What is the overall churn rate?
2. Which contract types have higher churn?
3. How does tenure relate to churn?
4. How do monthly charges differ between churned and retained customers?
5. Which services and payment methods are associated with churn?
6. Which customer segments should the business prioritize?

## 6. Project Limitations

This analysis identifies patterns and associations in the available
dataset. It does not automatically establish causation or prove
that a particular intervention will prevent churn.

## Contract-wise Churn Analysis

| Contract Type | Customers | Churned | Churn Rate |
|---|---:|---:|---:|
| Month-to-month | 3,875 | 1,655 | 42.71% |
| One year | 1,473 | 166 | 11.27% |
| Two year | 1,695 | 48 | 2.83% |

### Key Finding

Month-to-month customers have the highest observed churn
rate at 42.71%, while two-year contract customers have
the lowest observed churn rate at 2.83%.

### Business Recommendation

Investigate the reasons for higher churn among month-to-month
customers and evaluate targeted retention offers.

Note: These results show an association, not proof that
contract type causes churn.

## Monthly Charges vs Customer Churn

### Analysis Results

| Customer Status | Average Monthly Charges |
|---|---:|
| Retained (No) | 61.27 |
| Churned (Yes) | 74.44 |
| Overall Average | 64.76 |

### Key Finding

Customers who churned had average monthly charges of 74.44, compared with 61.27 for retained customers. The difference is approximately 13.18 units, or 21.5% higher for churned customers.

### Business Recommendation

Investigate whether higher monthly charges are associated with churn, particularly across different contract types and customer tenure groups. Consider reviewing pricing plans and targeted retention offers.

### Limitation

This comparison shows an association, not proof that higher monthly charges cause customers to leave. Other factors, such as contract type and tenure, may also influence churn.