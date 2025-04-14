#!/usr/bin/env python3
import sys

# Dictionaries to store trip data and taxi company data
trip_data = {}
taxi_data = {}

# Read input from the mapper
for line in sys.stdin:
    # Split the input line into taxi_id and details
    taxi_id, details = line.strip().split('\t', 1)
    # Further split details into the data type (TAXI/TRIP) and its value
    data_type, value = details.split(',', 1)

    # If the line contains taxi company data
    if data_type == 'TAXI':
        # Store taxi company information for this taxi_id
        taxi_data[taxi_id] = value

    # If the line contains trip data
    elif data_type == 'TRIP':
        # Initialize the list for this taxi_id if it does not exist
        if taxi_id not in trip_data:
            trip_data[taxi_id] = []
        # Append the trip data to the list for the corresponding taxi_id
        trip_data[taxi_id].append(value)

# Emit the joined results
for taxi_id in trip_data:
    # Ensure there is matching taxi company data
    if taxi_id in taxi_data:
        # For each trip, print the taxi company and the trip data
        for trip in trip_data[taxi_id]:
            print(f"{taxi_data[taxi_id]}\t{trip}")
