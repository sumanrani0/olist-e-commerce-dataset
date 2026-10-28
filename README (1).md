# Olist E-Commerce Analysis

An end-to-end data analytics project on the Olist Brazilian e-commerce marketplace dataset: data cleaning in **Python**, storage and analysis in **PostgreSQL**, and reporting in a **Power BI** dashboard.

![Olist E-Commerce Dashboard](dashboard/dashboard_overview.png)

## Project Overview

Nine raw CSV files were explored and cleaned with pandas, loaded into a PostgreSQL database, queried with SQL to answer ten business questions, and visualised in an interactive Power BI dashboard.

**Tools used:** Python (pandas, NumPy, SQLAlchemy, psycopg2), PostgreSQL, Power BI

## Dataset

[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (Kaggle). The dataset has nine related tables:

| Table | Contents |
|---|---|
| `olist_customers` | Customer IDs, city and state |
| `olist_orders` | Order status and purchase, approval and delivery timestamps |
| `olist_order_items` | Products, sellers, price and freight value per order |
| `olist_order_payments` | Payment type, installments and payment value |
| `olist_order_reviews` | Review score, title and comment |
| `olist_products` | Product category and physical attributes |
| `olist_sellers` | Seller IDs and location |
| `olist_geolocation` | Zip-code level coordinates |
| `product_category_name_translation` | Category names (Portuguese to English) |

## Workflow

1. **Explore:** check shape, columns, data types, nulls and duplicates for every table.
2. **Clean:** handle missing values and convert date columns.
3. **Load:** write all nine cleaned DataFrames to PostgreSQL with SQLAlchemy.
4. **Analyse:** answer ten business questions with SQL.
5. **Visualise:** build the Power BI dashboard.

### Data cleaning summary

| Table | Issue | Treatment |
|---|---|---|
| `olist_order_reviews` | Missing review title and comment | Filled with `"no review"` |
| `olist_orders` | Missing approval, carrier and delivery timestamps | Converted to datetime and filled with interpolation |
| `olist_products` | Missing category and numeric attributes | Mode for category, median for numeric columns |

## SQL Analysis

The queries in [`olist_Q_A.sql`](olist_Q_A.sql) answer:

1. Which seller generates the highest revenue?
2. What is the total product revenue, and how does it change month by month?
3. What is the total freight cost, and which category has the highest shipping cost?
4. What is the average delivery time, and which orders were delivered late?
5. Which payment methods are most popular, and what is the average number of installments?
6. Which customer cities and states place the most orders?
7. Which product categories receive the highest average review scores?
8. Which customer states generate the highest total payment value?
9. Which product categories generate the most revenue?
10. How do monthly orders, delivered orders and product sales change over time?

**SQL concepts used:** joins, `GROUP BY`, aggregations, `date_trunc`, `to_timestamp`, `to_char`, `COUNT(DISTINCT)`, the `FILTER` clause, timestamp arithmetic and type casting.

## Dashboard

The Power BI dashboard shows:

- KPI cards: total orders, total revenue, average order value, average review score, average delivery days
- Monthly orders and revenue trend
- Top 10 states by orders
- Payment methods
- Revenue vs. freight by city
- Product categories by revenue

| KPI | Value |
|---|---|
| Total orders | 98.67K |
| Total revenue | R$13.59M |
| Average order value | R$137.75 |
| Average review score | 4.09 |
| Average delivery time | 14.85 days |

## Key Insights

- Orders and revenue grew steadily from late 2016 and peaked in **November 2017**.
- **São Paulo** accounts for 46.42% of orders among the top 10 states, followed by Rio de Janeiro (14.39%) and Minas Gerais (12.88%).
- **Credit card** is the most used payment method (R$12.5M), well ahead of boleto (R$2.9M).
- **beleza_saude** (health and beauty) is the top revenue category.
- About **14% of the total price** paid is freight value.

## Repository Structure

```
.
├── README.md
├── olist_dataset.py          # exploration, cleaning and PostgreSQL export
├── olist_Q_A.sql             # 10 business questions in SQL
├── dashboard/                # Power BI screenshots
└── Olist_Ecommerce_Project_Report_Suman_Rani.pdf
```

## How to Run

1. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) and place the CSV files in a `data/` folder.
2. Install the dependencies:
   ```bash
   pip install pandas numpy sqlalchemy psycopg2-binary
   ```
3. Create a PostgreSQL database named `olist_project`.
4. Set your database password as an environment variable instead of writing it in the code:
   ```bash
   export DB_PASSWORD="your_password"      # Windows (PowerShell): $env:DB_PASSWORD="your_password"
   ```
5. Run `olist_dataset.py` to clean the data and load all tables into PostgreSQL.
6. Run the queries in `olist_Q_A.sql` in pgAdmin or `psql`.
7. Open the Power BI file and connect it to your database.

## Future Improvements

- Link delivery delays to review scores.
- Analyse seller performance beyond the top seller.
- Study repeat purchases using `customer_unique_id`.
- Add Python visualisations and a sales forecast.

## Author

**Suman Rani**
