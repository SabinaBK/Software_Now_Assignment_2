import statistics   # For standard deviation calculation

def seasonal_averages(data):
  #Calculates average temperature for each season

    # Month indexes for each season (0 = Jan, 11 = Dec)
    season_idx = {
        "Summer": [11, 0, 1],  # Dec, Jan, Feb
        "Autumn": [2, 3, 4],
        "Winter": [5, 6, 7],
        "Spring": [8, 9, 10]
    }

    season_avg = {}  # Store average of each season

    # Loop through each season
    for season, idxs in season_idx.items():
        temps = []  # Store all temperatures for this season

        # Loop through all stations
        for station_temps in data.values():

            # Pick only months of this season
            for i in idxs:
                temps.append(station_temps[i])

        # Calculate average for the season
        season_avg[season] = sum(temps) / len(temps) if temps else 0

    return season_avg  # Return result


def station_ranges(data):
    #Finds min, max and range for each station

    ranges = {}  # Store range data

    # Loop through each station
    for station, temps in data.items():
        ranges[station] = {
            "max": max(temps),                 # Highest temp
            "min": min(temps),                 # Lowest temp
            "range": max(temps) - min(temps)   # Difference
        }

    return ranges  # Return all ranges


def station_stddev(data):
  #Calculates standard deviation for each station

    stddevs = {}  # Store std deviation

    # Loop through each station
    for station, temps in data.items():
        stddevs[station] = statistics.stdev(temps)  # Calculate std dev

    return stddevs  # Return results
