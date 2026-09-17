import json
import os

import pandas as pd
import requests

base_endpoint = "https://api.fda.gov/drug/event.json"

glps = [
    "semaglutide",
    "liraglutide",
    "dulaglutide",
    "exenatide",
    "lixisenatide",
    "tirzepatide",
]

search_terms = [
    f'patient.drug.medicinalproduct:"{drug}"'
    for drug in glps
]

search_query = " OR ".join(search_terms)

params = {
    "search": search_query,
    "limit": 1000,
}

all_reports = []
r = requests.get(base_endpoint, params=params)

while True:
    print("Status:", r.status_code)

    if r.status_code != 200:
        print(r.text)
        print("Request failed.")
        break

    data = r.json()
    all_reports.extend(data["results"])
    print(f"Collected {len(all_reports)} reports")

    next_page = r.links.get("next")
    if next_page is None:
        print("No more pages.")
        break

    r = requests.get(next_page["url"])

reports_df = pd.DataFrame(all_reports)
print(reports_df.shape)
print(reports_df.head())

os.makedirs("data/raw", exist_ok=True)
with open("data/raw/glp1_reports.json", "w", encoding="utf-8") as f:
    json.dump(all_reports, f)

print("Saved raw GLP-1 reports.")
