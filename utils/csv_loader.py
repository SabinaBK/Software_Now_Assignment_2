import csv
import os

def load_temperature_data(folder_path):
    """
    Load CSV files where each row contains a station's monthly averages.
    Returns a dictionary: {station_name: [Jan, Feb, ..., Dec]}
    """
    data = {}

    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return data

    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    station = row["STATION_NAME"].strip()
                    # Read monthly temps
                    temps = []
                    for month in ["January","February","March","April","May","June",
                                  "July","August","September","October","November","December"]:
                        temp_str = row[month].strip()
                        temp = float(temp_str)
                        temps.append(temp)
                    data[station] = temps
    print(f"Total stations loaded: {len(data)}")
    return data
