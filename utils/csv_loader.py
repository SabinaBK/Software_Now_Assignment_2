# Import csv module to read CSV files
import csv

# Import os module to work with folders and file paths
import os

# This function loads temperature data from CSV files inside a folder
def load_temperature_data(folder_path):
    """
    This function:
    - Reads all CSV files from the given folder
    - Each row contains one weather station's monthly temperatures
    - Returns a dictionary in this format:
      {
        "Station Name": [Jan, Feb, Mar, ..., Dec]
      }
    """

    # Create an empty dictionary to store all station data
    data = {}

    # Check if the given folder path exists or not
    # If it does NOT exist, print error message and return empty data
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return data   # Stop function here and return empty dictionary


    # Loop through all files inside the folder
    for filename in os.listdir(folder_path):

        # Check if the file is a CSV file
        if filename.endswith(".csv"):

            # Create full path of the file (folder + filename)
            filepath = os.path.join(folder_path, filename)

            # Open the CSV file in read mode
            # newline="" prevents blank lines
            # encoding="utf-8" supports special characters
            with open(filepath, "r", newline="", encoding="utf-8") as f:

                # Create a CSV reader that reads each row as a dictionary
                # Example: row["January"], row["STATION_NAME"], etc.
                reader = csv.DictReader(f)

                # Loop through each row in the CSV file
                for row in reader:

                    # Read the station name and remove extra spaces
                    station = row["STATION_NAME"].strip()

                    # Create an empty list to store 12 months temperatures
                    temps = []

                    # Loop through all 12 months
                    for month in [
                        "January","February","March","April","May","June",
                        "July","August","September","October","November","December"
                    ]:

                        # Read temperature value as string and remove spaces
                        temp_str = row[month].strip()

                        # Convert string temperature to float number
                        temp = float(temp_str)

                        # Add temperature to the list
                        temps.append(temp)

                    # Store station data in dictionary
                    # Example: data["Adelaide"] = [30.1, 29.4, ..., 18.2]
                    data[station] = temps


    # Print how many stations were loaded
    print(f"Total stations loaded: {len(data)}")

    # Return the final dictionary containing all station data
    return data
