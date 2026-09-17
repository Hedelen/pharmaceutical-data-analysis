import json

import pandas as pd

with open("data/raw/glp1_reports.json", "r", encoding="utf-8") as f:
    all_reports = json.load(f)

reports_df = pd.DataFrame(all_reports)

print(reports_df.shape)
print(reports_df.head())
