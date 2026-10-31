import csv


def read_rows(filename):
    with open(filename) as f:
        return list(csv.DictReader(f))


def clean_values(rows, column):
    values = []
    for row in rows:
        raw = row[column]
        if raw == "":
            continue
        values.append(float(raw))
    return values


def summarise(values):
    if len(values) == 0:
        return {"count": 0}
    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
        "average": round(sum(values) / len(values), 1),
    }


def summarise_all(filename, columns):
    rows = read_rows(filename)
    report = {}
    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarise(values)
    return report


rows = read_rows("ibadan_north_wards.csv")
values = clean_values(rows, "population_2024")
result = summarise(values)
print(result)

report = summarise_all("ibadan_north_wards.csv", ["area_km2", "population_2024", "facilities"])
for column, stats in report.items():
    print(column, "->", stats)
