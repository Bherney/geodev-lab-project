with open("wards.csv") as f:
    lines = f.readlines()

total = 0

for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
    area_km2 = float(parts[1])
    area_hectares = area_km2 * 100
    total = total + area_km2
    if area_km2 > 9:
        size = "large"
    else:
        size = "small"
    print(ward, "is", size, "at", area_hectares, "hectares")

print("Total area:", total, "km2")
