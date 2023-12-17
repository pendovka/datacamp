from common.base import session

# Create the view with the appropriate metrics
query = """
CREATE OR REPLACE VIEW insights AS
SELECT county,
       COUNT(*) AS sales_count,
       SUM(CAST(price AS int)) AS sales_total,
       MAX(CAST(price AS int)) AS sales_max,
       MIN(CAST(price AS int)) AS sales_min,
       AVG(CAST(price AS int))::numeric(10,2) AS sales_avg
FROM ppr_clean_all
GROUP BY county
"""

def main():
       session.execute(query)
       session.commit()
       print("Data exported:", f"{base_path}/insights_export/InsightsExport_202102.xlsx")
