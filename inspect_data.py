import csv


def inspect_column(filename, column):
    with open(filename) as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column]
        if raw == "":
            continue
        values.append(float(raw))
    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
    }


with open("ibadan_north_wards.csv") as f:
    rows = list(csv.DictReader(f))

print("Number of rows:", len(rows))
print("Columns:", list(rows[0].keys()))

result = inspect_column("ibadan_north_wards.csv", "population_2024")
print(result)
