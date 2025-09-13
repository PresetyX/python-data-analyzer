# python-data-analyzer

# Data Analysis and Automation Tool

This command-line application, developed in Python, automates the process of collecting, cleaning, and analyzing data from multiple CSV sources. It uses the powerful **Pandas** library to process datasets and generate insightful summary reports directly in the terminal.

## Key Features

-   **Multi-Source Ingestion:** Automatically reads and combines all `.csv` files from a specified `data/` directory.
-   **Data Cleaning:** Implements a cleaning pipeline that handles missing values, corrects data types, standardizes categorical data, and removes duplicates.
-   **Insightful Analysis:** Calculates key business metrics such as total revenue, average product price, best-selling products, and sales breakdown by category.
-   **Automated Reporting:** Generates a clean, formatted summary report in the console upon execution.

## Tech Stack

-   **Language:** `Python`
-   **Library:** `Pandas`

## How to Run

1.  Ensure you have Python and Pandas installed (`pip install pandas`).
2.  Place your `.csv` data files inside the `data/` directory.
3.  Run the script from your terminal:

```bash
python analyzer.py
```
