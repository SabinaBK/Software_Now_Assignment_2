import statistics

def seasonal_averages(data):
    """
    Compute average temperature per season:
    - Summer: Dec, Jan, Feb
    - Autumn: Mar, Apr, May
    - Winter: Jun, Jul, Aug
    - Spring: Sep, Oct, Nov
    """
    season_idx = {
        "Summer": [11, 0, 1],  # Dec, Jan, Feb
        "Autumn": [2, 3, 4],
        "Winter": [5, 6, 7],
        "Spring": [8, 9, 10]
    }

    season_avg = {}
    for season, idxs in season_idx.items():
        temps = []
        for station_temps in data.values():
            for i in idxs:
                temps.append(station_temps[i])
        season_avg[season] = sum(temps) / len(temps) if temps else 0
    return season_avg

def station_ranges(data):
    """
    Returns a dictionary with station ranges, min and max
    """
    ranges = {}
    for station, temps in data.items():
        ranges[station] = {
            "max": max(temps),
            "min": min(temps),
            "range": max(temps) - min(temps)
        }
    return ranges

def station_stddev(data):
    """
    Returns a dict with standard deviation of monthly temps for each station
    """
    stddevs = {}
    for station, temps in data.items():
        stddevs[station] = statistics.stdev(temps)
    return stddevs
