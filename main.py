import os
from utils.csv_loader import load_temperature_data
from utils.stats import seasonal_averages, station_ranges, station_stddev

TEMP_FOLDER = "temperatures"
OUTPUT_FOLDER = "output"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load monthly data
data = load_temperature_data(TEMP_FOLDER)

# Seasonal Average
season_avg = seasonal_averages(data)
with open(os.path.join(OUTPUT_FOLDER, "average_temp.txt"), "w") as f:
    for season, avg in season_avg.items():
        f.write(f"{season}: {avg:.1f}°C\n")

#  Largest Temperature Range
ranges = station_ranges(data)
if ranges:
    max_range = max(r["range"] for r in ranges.values())
    with open(os.path.join(OUTPUT_FOLDER, "largest_temp_range_station.txt"), "w") as f:
        for station, r in ranges.items():
            if r["range"] == max_range:
                f.write(
                    f"Station {station}: Range {r['range']:.1f}°C "
                    f"(Max: {r['max']:.1f}°C, Min: {r['min']:.1f}°C)\n"
                )

# Temperature Stability
stddevs = station_stddev(data)
if stddevs:
    min_std = min(stddevs.values())
    max_std = max(stddevs.values())
    with open(os.path.join(OUTPUT_FOLDER, "temperature_stability_stations.txt"), "w") as f:
        for station, std in stddevs.items():
            if std == min_std:
                f.write(f"Most Stable: Station {station}: StdDev {std:.1f}°C\n")
        for station, std in stddevs.items():
            if std == max_std:
                f.write(f"Most Variable: Station {station}: StdDev {std:.1f}°C\n")
