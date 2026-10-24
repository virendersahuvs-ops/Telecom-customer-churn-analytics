<div align="center">

# Telecom Customer Churn & Retention Analytics

**Turning customer data into actionable retention insights**

![Excel](https://img.shields.io/badge/Excel-1F3864?style=flat-square&logo=microsoftexcel&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-2E75B6?style=flat-square&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-1F3864?style=flat-square&logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-2E75B6?style=flat-square&logo=powerbi&logoColor=white)
![Dataset](https://img.shields.io/badge/Dataset-IBM%20Telco%20Churn-F4B6CB?style=flat-square)

An end-to-end data analytics portfolio project that uses **Excel, MySQL, Python, and Power BI** to explore churn patterns and identify customer segments that may need retention-focused attention.

[Overview](#project-at-a-glance) · [Findings](#key-findings) · [Tools](#tools--technologies) · [Structure](#repository-structure) · [Dashboard](#power-bi-dashboard) · [SQL](#sql-validation) · [Quick Start](#how-to-explore-the-project) · [Limitations](#limitations)

</div>

---

<p align="center">
  <img src="Screenshot/project_overview_infographic.png" alt="Project overview infographic" width="900">
</p>

<p align="center"><em>Project overview infographic (design summary). The actual Power BI report is shown in the <a href="#power-bi-dashboard">Power BI Dashboard</a> section.</em></p>

---

## Project at a Glance

| Metric | Result |
|---|---:|
| Customers analyzed | **7,043** |
| Churned customers | **1,869** |
| Retained customers | **5,174** |
| Overall churn rate | **26.54%** |
| Overall retention rate | **73.46%** |

> **Business question:** Which customer groups show higher churn rates, and how can these patterns inform more focused retention strategies?

## Executive Summary

This project analyzes the **IBM Telco Customer Churn** dataset to understand how churn varies across contract type, customer tenure, payment method, internet service, and monthly charges. The workflow combines data preparation, exploratory analysis, SQL queries, spreadsheet analysis, and an interactive Power BI dashboard.

> **Note:** All findings are descriptive. They highlight associations in the data and do **not** establish that any single factor causes churn.

## Key Findings

### Churn by contract type

| Contract | Customers | Churned | Churn rate |
|---|---:|---:|---:|
| Month-to-month | 3,875 | 1,655 | **42.71%** |
| One year | 1,473 | 166 | 11.27% |
| Two year | 1,695 | 48 | 2.83% |

### Churn by customer tenure

| Tenure group | Customers | Churned | Churn rate |
|---|---:|---:|---:|
| 0–12 months | 2,186 | 1,037 | **47.44%** |
| 13–24 months | 1,024 | 294 | 28.71% |
| 25–48 months | 1,594 | 325 | 20.39% |
| 49–72 months | 2,239 | 213 | 9.51% |

### Average monthly charges

| Customer group | Average MonthlyCharges |
|---|---:|
| Retained customers | 61.27 |
| All customers | 64.76 |
| Churned customers | 74.44 |

*Values are in the dataset's currency units.*

### Churn by monthly-charge group

| Monthly-charge group | Churn rate |
|---|---:|
| 0–30 | 9.80% |
| 30–50 | 31.05% |
| 50–70 | 20.21% |
| 70–90 | 37.95% |
| 90+ | 32.86% |

*Source: Power BI dashboard. Churn does not rise steadily with charges, so charge level alone does not explain churn.*

### Additional segments to investigate

| Dimension | Segment | Churn rate |
|---|---|---:|
| Internet service | Fiber optic | 41.89% |
| Internet service | DSL | 18.96% |
| Internet service | No internet service | 7.40% |
| Payment method | Electronic check | 45.29% |
| Payment method | Mailed check | 19.11% |
| Payment method | Automatic bank transfer | 16.71% |
| Payment method | Automatic credit card | 15.24% |
| Online security | Without | 41.77% |
| Online security | With | 14.61% |
| Tech support | Without | 41.64% |
| Tech support | With | 15.17% |

### What the findings suggest

1. **Early-life experience:** Review onboarding and support during the first year, where observed churn is highest.
2. **Contract commitment:** Investigate the needs of month-to-month customers and test suitable longer-term contract incentives.
3. **Service and billing:** Explore whether payment experience, service expectations, and perceived value differ across high-churn segments.
4. **Measure outcomes:** Test targeted retention actions and track results before scaling them.

> These are hypotheses for further investigation, not proof of causation.

## Tools & Technologies

| Tool | How it was used |
|---|---|
| **Microsoft Excel** | Data review, pivot-based analysis, KPI summaries, and segment comparisons |
| **MySQL** | Querying customer data and analyzing churn across business dimensions |
| **Python** (Pandas, NumPy, Matplotlib, Seaborn) | Data inspection, quality checks, cleaning, exploratory analysis, and visualizations |
| **Power BI** | Interactive executive dashboard with KPI cards, charts, and slicers |

## Project Workflow

```text
Inspect  →  Validate  →  Clean & Prepare  →  Analyze  →  Visualize  →  Recommend
```

1. **Inspect** the source data and understand the available fields.
2. **Validate** data quality, including customer IDs, duplicates, and missing values.
3. **Clean and prepare** the dataset for analysis.
4. **Analyze** churn patterns with Excel, SQL, and Python.
5. **Visualize** key findings in Python charts and Power BI.
6. **Translate** the results into practical retention questions and recommendations.

## Repository Structure

```text
Telecom-customer-churn-analytics/
├── data/          # Source and cleaned datasets
├── excel/         # Excel workbook and analysis
├── powerbi/       # Power BI dashboard (.pbix)
├── python/        # Python scripts and Jupyter notebook
├── reports/       # Project report, presentation, and charts
├── Screenshot/    # Project screenshots and SQL result captures
├── sql/           # SQL analysis queries and outputs
└── README.md      # Project overview and documentation
```

*Folder contents may evolve as the project is refined.*

## Power BI Dashboard

A single-page **Executive Overview** of churn and retention.

<p align="center">
  <img src="Screenshot/powerbi_executive_overview.png" alt="Power BI Executive Overview dashboard" width="900">
</p>

<p align="center"><em>Executive Overview dashboard. KPI cards display values in thousands (7.043K = 7,043).</em></p>

**What it includes**

- **KPI cards:** Total Customer, Churn, Retained, Churn Rate, and Retention Rate
- **Customer distribution by tenure group**, with Highest (47.44%) and Lowest (9.51%) churn group cards
- **Churn rate by contract type**, with a Highest Churn Rate card (42.71%)
- **Churn rate by internet service**, with a Fiber Optic card (41.89%)
- **Churn rate by monthly charges** across five charge groups
- **Slicers:** Contract, Internet Service, Gender, and Tenure Group

**Dashboard file:** [`powerbi/`](powerbi/). Download the `.pbix` file and open it in Power BI Desktop.

## SQL Validation

MySQL queries were used to cross-check the headline KPIs and the tenure-wise churn results. The queries normalize the `Churn` field with `LOWER(LEFT(TRIM(Churn), 1))` to avoid the carriage-return import issue described below.

| Overall churn query | Tenure-wise churn query |
|---|---|
| <img src="Screenshot/01_overall_churn_sql.png" alt="Overall churn SQL result" width="440"> | <img src="Screenshot/03_tenure_wise_churn_sql.png" alt="Tenure-wise churn SQL result" width="440"> |

- **Overall:** 7,043 customers, 1,869 churned, 5,174 retained, 26.54% churn rate, average monthly charges 64.76, average tenure 32.37 months.
- **Tenure-wise:** 47.44%, 28.71%, 20.39%, and 9.51% churn for the 0–12, 13–24, 25–48, and 49–72 month groups.

## Project Deliverables

| Deliverable | Location |
|---|---|
| Project report (Word) | `reports/01_Project_Report.docx` |
| Presentation (10 slides) | `reports/06_Presentation.pptx` |
| Power BI dashboard | `powerbi/` |
| SQL queries and outputs | `sql/` |
| Excel analysis | `excel/` |
| Python EDA | `python/` |
| Screenshots | `Screenshot/` |

## Data Quality Notes

| Check | Result |
|---|---:|
| Dataset shape | 7,043 rows × 21 columns |
| Unique customer IDs | 7,043 |
| Duplicate rows | 0 |
| Missing `TotalCharges` values | 11 |

- The 11 records with missing `TotalCharges` should be handled transparently. They should not be silently deleted, and any exclusion or imputation choice should be documented.
- **MySQL note:** after import, the `Churn` field may carry a carriage-return character on the value `Yes`. The SQL queries normalize it with `TRIM` and a first-character check before filtering or grouping.

## How to Explore the Project

1. Start with the project report in `reports/` for context and conclusions.
2. Open the Excel workbook in `excel/` to review KPI and segment analyses.
3. Review the SQL files in `sql/` to see how each question was queried.
4. Open `python/Python_EDA.ipynb` (or the scripts in `python/`) to follow the analysis workflow. Typical requirements: `pandas`, `numpy`, `matplotlib`, `seaborn`, and Jupyter.
5. Open the `.pbix` file in `powerbi/` to explore the dashboard interactively.

## Limitations

- The analysis uses a historical sample dataset and may not represent every telecom business.
- Observed relationships are associations, not proof of causation.
- Segments overlap (for example, fiber optic and electronic-check customers), so single-factor comparisons can be confounded.
- No predictive model or statistical significance testing is reported.
- Retention recommendations should be validated with additional context and controlled experiments before business implementation.

## Author

**Virender Sahu**
B.Tech, Delhi Technological University (DTU)
Roll No.: 23/EE/286

---

<div align="center">

*Data analytics • Customer insights • Retention strategy*

</div>
