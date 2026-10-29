"""Bob's report: revenue per region, from sales.csv."""

import pandas as pd
from tabulate import tabulate

sales = pd.read_csv("sales.csv")
sales["revenue"] = sales["quantity"] * sales["unit_price"]
by_region = sales.groupby("region")["revenue"].sum().round(2)
print(tabulate(by_region.items(), headers=["region", "revenue"]))
