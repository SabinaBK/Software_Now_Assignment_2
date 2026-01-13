
"""
ID: s398027
Name:Asmita Shrestha
Question 2
Create a program that analyses temperature data collected from multiple weather stations in Australia. The data is stored in multiple CSV files under a "temperatures" folder, with each file representing data from one year. Process ALL .csv files in the temperatures folder. Ignore missing temperature values (NaN) in calculations.
Main Functions to Implement:
Seasonal Average: Calculate the average temperature for each season across ALL stations and ALL years. Save the results to "average_temp.txt".
• Use Australian seasons: Summer (Dec-Feb), Autumn (Mar-May), Winter (Jun-Aug), Spring (Sep-Nov)
• Output format example: "Summer: 28.5°C"
Temperature Range: Find the station(s) with the largest temperature range (difference between the highest and lowest temperature ever recorded at that station). Save the results to "largest_temp_range_station.txt".
• Output format example: "Station ABC: Range 45.2°C (Max: 48.3°C, Min: 3.1°C)"
• If multiple stations tie, list all of them
Temperature Stability: Find which station(s) have the most stable temperatures (smallest standard deviation) and which have the most variable temperatures (largest standard deviation). Save the results to "temperature_stability_stations.txt".
• Output format example:
o "Most Stable: Station XYZ: StdDev 2.3°C"
o "Most Variable: Station DEF: StdDev 12.8°C"
StdDev 12.8°C"
• If multiple stations tie, list all of them
"""

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
TEMP_FOLDER = "Question_2/temperatures"

# Folder name where output text files will be saved
OUTPUT_FOLDER = "Question_2/output"

# Create the output folder if it does not already exist, exist_ok=True prevents error if the folder already exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load monthly temperature data
# Load temperature data from CSV files inside TEMP_FOLDER
# The returned data is usually a dictionary of station data
data = load_temperature_data(TEMP_FOLDER)

# Seasonal Average Calculation
#For each season calculate average temperature
season_avg = seasonal_averages(data)

#To write seasonal averages ,files is created naming average_temp.txt
with open(os.path.join(OUTPUT_FOLDER, "average_temp.txt"), "w") as f:
    
    # Loop is used to iterate through each season and its average temperature
    for season, avg in season_avg.items():
        
        # Write season name and average temperature (1 decimal place)
        f.write(f"{season}: {avg:.1f}°C\n")

#Show the Largest Temperature Range by Station
# Calculate temperature range (max - min) for each station
ranges = station_ranges(data)

# Check if range data exists or not
if ranges:
    
    # Find the maximum temperature range among all stations
    max_range = max(r["range"] for r in ranges.values())
    
    # Create a file to write station with largest range
    with open(os.path.join(OUTPUT_FOLDER, "largest_temp_range_station.txt"), "w") as f:
        
        # Loop is used to iterate each station and its range data
        for station, r in ranges.items():
            
            # If this station has the maximum range then this will execute
            if r["range"] == max_range:
                
                # Write station details: range, max temp, and min temp
                f.write(
                    f"Station {station}: Range {r['range']:.1f}°C "
                    f"(Max: {r['max']:.1f}°C, Min: {r['min']:.1f}°C)\n"
                )


# Temperature Stability (Std Deviation)
# Calculate standard deviation of temperature for each station
stddevs = station_stddev(data)

# Check if standard deviation data exists
if stddevs:
    
    # Find the minimum standard deviation (most stable station)
    min_std = min(stddevs.values())
    
    # Find the maximum standard deviation (most variable station)
    max_std = max(stddevs.values())
    
    #To write stability a file is created naming "temperature_stability_stations.txt"
    with open(os.path.join(OUTPUT_FOLDER, "temperature_stability_stations.txt"), "w") as f:
        
        #Loop is used to iterate and Find and write the most stable station
        for station, std in stddevs.items():
            if std == min_std:
                f.write(f"Most Stable: Station {station}: StdDev {std:.1f}°C\n")
        
        # Find and write the most variable station using loop
        for station, std in stddevs.items():
            if std == max_std:
                f.write(f"Most Variable: Station {station}: StdDev {std:.1f}°C\n")

