# Telecom Customer Churn & Retention Analytics

A data analytics portfolio project exploring customer churn patterns in
the IBM Telco Customer Churn dataset. The goal is to identify customer
segments with higher observed churn and translate the findings into
practical retention recommendations using Excel, SQL, Python, and Power
BI.

## Project Overview

Customer churn can reduce recurring revenue and make customer retention
a key business priority. This project examines churn across contract
types, customer tenure, monthly charges, payment methods, and selected
services.

**Student:** Virender Sahu\
**College:** Delhi Technological University (DTU)\
**Roll Number:** 23/EE/286

## Key Findings

  Metric / Segment                                       Result
  ---------------------------------------------------- --------
  Total customers                                         7,043
  Churned customers                                       1,869
  Retained customers                                      5,174
  Overall churn rate                                     26.54%
  Overall retention rate                                 73.46%
  Month-to-month contract churn rate                     42.71%
  One-year contract churn rate                           11.27%
  Two-year contract churn rate                            2.83%
  Churn rate for customers with 0--12 months tenure      47.44%
  Churn rate for customers with 49--72 months tenure      9.51%
  Average monthly charges --- churned customers           74.44
  Average monthly charges --- retained customers          61.27
  Churn rate --- electronic check users                  45.29%
  Churn rate --- fiber-optic customers                   41.89%

These are descriptive patterns in this dataset. They show associations,
not proof that any single factor causes churn.

## Tools Used

-   **Excel:** Data checks, KPI summary, segment analysis, charts, and
    spreadsheet analysis.
-   **MySQL:** Customer churn queries and segment comparisons.
-   **Python:** Pandas, NumPy, Matplotlib, and Seaborn for data
    inspection, cleaning checks, exploratory analysis, and
    visualizations.
-   **Power BI:** Interactive Executive Overview dashboard with KPI
    cards, churn charts, and slicers.

## Repository Structure

``` text
telecom-customer-churn-analytics/
├── data/
│   └── (place the dataset here if redistribution is permitted)
├── excel/
│   └── 02_Excel_Analysis.xlsx
├── sql/
│   └── 03_SQL_Queries.sql
├── python/
│   └── 04_Python_EDA.ipynb
├── powerbi/
│   └── 05_PowerBI_Dashboard.pbix
├── reports/
│   ├── 01_Project_Report.pdf
│   └── 06_Presentation.pptx
└── README.md
```

*Adjust filenames and folders to match the actual files in your local
project. Keep generated charts in the appropriate reports or charts
folder.*

## Analysis Workflow

1.  Inspect the dataset structure, data types, missing values, duplicate
    rows, and customer ID uniqueness.
2.  Validate the overall churn and retention totals.
3.  Analyze churn by contract type, tenure group, monthly charges,
    payment method, internet service, and selected support/security
    services.
4.  Use SQL to query and rank churn patterns across customer segments.
5.  Use Python for exploratory data analysis and visualizations.
6.  Summarize the results in a Power BI dashboard.
7.  Translate observed patterns into testable customer retention
    recommendations.

## Data Quality Notes

-   The dataset contains **7,043 rows** and **21 columns**.
-   **7,043 unique customer IDs** were reported.
-   **0 duplicate rows** were reported.
-   **11 missing values** were found in `TotalCharges`.
-   Missing `TotalCharges` records should not be silently removed;
    document any handling decision and preserve the original records.
-   During MySQL import, the `Churn` field was observed to contain a
    trailing carriage-return character for some `Yes` values.
    Normalize/trim this field before relying on exact text comparisons.

## Business Recommendations

1.  **Focus on early retention:** Review onboarding and proactively
    check in with customers during their first 12 months.
2.  **Test contract incentives:** Evaluate suitable, transparent
    benefits for customers who may prefer longer-term contracts.
3.  **Investigate higher-charge segments:** Review billing clarity,
    service bundles, and customer feedback.
4.  **Review payment journeys:** Investigate potential friction in the
    electronic-check payment experience.
5.  **Improve support and service experience:** Explore feedback from
    higher-churn segments before choosing interventions.

Recommendations should be tested and measured. The analysis is
descriptive and does not establish causal relationships.

## How to Reproduce

### Python

1.  Install Python 3.10+ (or a compatible version already used for the
    notebook).

2.  Install the core libraries:

    ``` bash
    pip install pandas numpy matplotlib seaborn jupyter
    ```

3.  Place the cleaned CSV at the path expected by the notebook,
    currently described as `../data/telco_churn_cleaned.csv`, or update
    the notebook's data path.

4.  Open and run `04_Python_EDA.ipynb` in Jupyter Notebook or VS Code.

### SQL

1.  Create a MySQL database for the project.
2.  Import the cleaned dataset into a customer table.
3.  Open the SQL scripts in the `sql/` folder and run them against the
    imported table.
4.  If your imported `Churn` values contain carriage returns, normalize
    them before using exact string comparisons.

### Power BI

1.  Open the `.pbix` file in Power BI Desktop.
2.  Confirm the data source path and refresh the data if needed.
3.  Check KPI values and test the slicers before presenting the
    dashboard.

### Excel

1.  Open the Excel workbook in Microsoft Excel.
2.  Confirm the raw-data source and refresh any PivotTables/PivotCharts
    if applicable.
3.  Check KPI values and formulas before final submission.

## Deliverables

The project is intended to include:

-   `01_Project_Report.pdf` --- written report.
-   `02_Excel_Analysis.xlsx` --- Excel analysis workbook.
-   `03_SQL_Queries.sql` --- consolidated SQL queries.
-   `04_Python_EDA.ipynb` --- Python exploratory analysis notebook.
-   `05_PowerBI_Dashboard.pbix` --- Power BI dashboard.
-   `06_Presentation.pptx` --- project presentation.
-   `07_ReadMe.pdf` or `README.md` --- project documentation.

Some filenames above are recommended names; update them to reflect the
actual files you publish.

## Limitations

-   The analysis is descriptive and does not prove causation.
-   Missing `TotalCharges` values require documented handling for
    analyses that use this field.
-   Results depend on the dataset, data preparation choices, and
    definitions of churn/retention.
-   Before publishing, verify the dataset's source and licence. Do not
    upload data if redistribution is not permitted.

## Author

**Virender Sahu**\
Delhi Technological University (DTU)\
Roll Number: 23/EE/286
