

# Import the built-in os module
# This is used for working with folders and file paths
import os

# Import the function to load temperature CSV data
# This function is defined inside utils/csv_loader.py
from utils.csv_loader import load_temperature_data

# Import statistical functions from utils/stats.py
# - seasonal_averages: calculates average temperature per season
# - station_ranges: calculates min, max, and range per station
# - station_stddev: calculates standard deviation per station
from utils.stats import seasonal_averages, station_ranges, station_stddev


# Folder name where temperature CSV files are stored
TEMP_FOLDER = "temperatures"

# Folder name where output text files will be saved
OUTPUT_FOLDER = "output"

# Create the output folder if it does not already exist
# exist_ok=True prevents error if the folder already exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# -----------------------------
# Load monthly temperature data
# -----------------------------

# Load temperature data from CSV files inside TEMP_FOLDER
# The returned data is usually a dictionary of station data
data = load_temperature_data(TEMP_FOLDER)


# -----------------------------
# Seasonal Average Calculation
# -----------------------------

# Calculate average temperature for each season
season_avg = seasonal_averages(data)

# Open (or create) a file to write seasonal averages
with open(os.path.join(OUTPUT_FOLDER, "average_temp.txt"), "w") as f:
    
    # Loop through each season and its average temperature
    for season, avg in season_avg.items():
        
        # Write season name and average temperature (1 decimal place)
        f.write(f"{season}: {avg:.1f}°C\n")


# ---------------------------------
# Largest Temperature Range by Station
# ---------------------------------

# Calculate temperature range (max - min) for each station
ranges = station_ranges(data)

# Check if range data exists (not empty)
if ranges:
    
    # Find the maximum temperature range among all stations
    max_range = max(r["range"] for r in ranges.values())
    
    # Open (or create) file to write station(s) with largest range
    with open(os.path.join(OUTPUT_FOLDER, "largest_temp_range_station.txt"), "w") as f:
        
        # Loop through each station and its range data
        for station, r in ranges.items():
            
            # If this station has the maximum range
            if r["range"] == max_range:
                
                # Write station details: range, max temp, and min temp
                f.write(
                    f"Station {station}: Range {r['range']:.1f}°C "
                    f"(Max: {r['max']:.1f}°C, Min: {r['min']:.1f}°C)\n"
                )


# ---------------------------------
# Temperature Stability (Std Deviation)
# ---------------------------------

# Calculate standard deviation of temperature for each station
stddevs = station_stddev(data)

# Check if standard deviation data exists
if stddevs:
    
    # Find the minimum standard deviation (most stable station)
    min_std = min(stddevs.values())
    
    # Find the maximum standard deviation (most variable station)
    max_std = max(stddevs.values())
    
    # Open (or create) file to write stability results
    with open(os.path.join(OUTPUT_FOLDER, "temperature_stability_stations.txt"), "w") as f:
        
        # Find and write the most stable station(s)
        for station, std in stddevs.items():
            if std == min_std:
                f.write(f"Most Stable: Station {station}: StdDev {std:.1f}°C\n")
        
        # Find and write the most variable station(s)
        for station, std in stddevs.items():
            if std == max_std:
                f.write(f"Most Variable: Station {station}: StdDev {std:.1f}°C\n")

