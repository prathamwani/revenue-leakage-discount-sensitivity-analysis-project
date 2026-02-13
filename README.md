# Revenue Leakage Analysis using SQL, Python, and Power BI

## Project Overview
This project analyzes revenue leakage caused by aggressive discounting in a retail dataset. The goal is to identify how discount levels impact profitability across categories and subcategories, and to uncover areas where losses occur.

The analysis was performed using SQL for data querying, Python for exploratory data analysis (EDA), and Power BI for interactive visualization and business insights.

---

## Business Problem
Excessive discounting can increase sales but may reduce profit margins and create hidden revenue leakage. This project investigates:

- How discount affects profit
- Which categories and subcategories generate losses
- Which discount levels are most harmful
- Where business should reduce discounting

---

## Tools & Technologies
- SQL (MySQL Workbench)
- Python (Pandas, Matplotlib)
- Power BI
- Excel

---

## Data Files
- `orders.csv` → Raw dataset used for SQL and Python analysis  
- `orders_with_bands.csv` → Processed dataset with discount bands used for Power BI dashboard  

---

## Key Analysis Performed
- Profitability by Category
- Profitability by Sub-Category
- Discount vs Profit relationship
- Profit by Discount Band (Low, Medium, High)
- Revenue leakage identification
- Loss-making product segments

---

## Key Insights
- High discount levels generate significant negative profit
- Profit decreases as discount increases
- Tables and Bookcases are major loss-making subcategories
- Machines and Supplies also show negative margins
- Low discount strategy remains consistently profitable

---

## Business Recommendations
- Limit high discount usage (above 30%)
- Reduce discounting in Tables, Bookcases, and Machines
- Implement discount threshold policies
- Monitor discount sensitivity to protect margins

---

## Power BI Dashboard
The interactive dashboard highlights:

- Total Sales, Profit, Orders, and Average Discount
- Profit by Category
- Profit by Discount Band
- Profit by Sub-Category
- Revenue Leakage Visualization

---

## Analysis Visualizations

### Profit by Category
![Profit by Category](images/Profit_by_Category_bar_chart.png)

### Profit by Sub-Category
![Profit by Sub-Category](images/subcategory_profit.png)

### Discount vs Profit
![Discount vs Profit](images/discount_vs_profit.png)

### Profit by Discount Band
![Profit by Discount Band](images/discount_band_profit.png)

---

## Project Structure
data/
 ├── orders.csv
 ├── orders_with_bands.csv

python/
 └── eda.py

sql/
 └── analysis.sql

powerbi/
 └── revenue_leakage_dashboard.pbix

images/
 ├── category_profit.png
 ├── subcategory_profit.png
 ├── discount_vs_profit.png
 ├── discount_band_profit.png
---

## How to Run the Project

1. Open SQL file and run queries in MySQL Workbench
2. Run Python script `eda.py` to perform EDA and generate plots
3. Open Power BI dashboard file to explore interactive insights

---

## Author
Pratham Wani  
Data Analyst | SQL | Python | Power BI
