"""
demo_scraper.py

This is a SAFE demo script for Cyberhaven demos.
It mimics scraping financial or healthcare data from a webpage.
No external sites are contacted — it uses a local HTML sample.
"""

from bs4 import BeautifulSoup
import csv

# --- Sample HTML page (simulating a company/portfolio site) ---
html_page = """
<html>
<head><title>WCAS Portfolio</title></head>
<body>
<h1>WCAS Portfolio Companies</h1>
<table>
    <tr><th>Company</th><th>Sector</th><th>Investment Year</th></tr>
    <tr><td>HealthTech AI</td><td>Healthcare</td><td>2021</td></tr>
    <tr><td>FinSync</td><td>Technology</td><td>2020</td></tr>
    <tr><td>CareLink Partners</td><td>Healthcare</td><td>2023</td></tr>
</table>
</body>
</html>
"""

# --- Parse HTML content ---
soup = BeautifulSoup(html_page, "html.parser")

# --- Extract data from table ---
rows = soup.find_all("tr")[1:]  # Skip header row
data = []

for row in rows:
    cols = [col.text.strip() for col in row.find_all("td")]
    data.append(cols)

# --- Save to CSV (for lineage/demo purposes) ---
with open("wcas_portfolio_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Sector", "Investment Year"])
    writer.writerows(data)

print("✅ Demo data written to wcas_portfolio_data.csv")

# --- Example output ---
# Company,Sector,Investment Year
# HealthTech AI,Healthcare,2021
# FinSync,Technology,2020
# CareLink Partners,Healthcare,2023
