#!/usr/bin/env python3
import sys

# Dictionary to store aggregated trip data for each unique combination of taxi and trip type
aggregated_data = {}

# Process each line from the input (stdin) stream
for line in sys.stdin:
    fields = line.strip().split(',')

    # Ensure the line contains at least 4 fields (valid data line), otherwise skip the line
    if len(fields) < 4:
        continue
    
    # Extract relevant fields: taxi ID, fare, and distance from the input data
    taxi_id = fields[1]  # Taxi number (identifier)
    fare = float(fields[2])  # Fare amount (converted to float)
    distance = float(fields[3])  # Trip distance (converted to float)

    # Classify the trip type based on distance: 'long', 'medium', or 'short'
    if distance >= 200:
        trip_type = "long"
    elif 100 <= distance < 200:
        trip_type = "medium"
    else:
        trip_type = "short"

    # Create a unique key combining taxi ID and trip type for grouping data
    key = f"{taxi_id},{trip_type}"

    # Initialize the dictionary entry for this key if it's not already present
    if key not in aggregated_data:
        aggregated_data[key] = {
            'total_fare': 0.0,  # Total fare for this key
            'trip_count': 0,     # Count of trips for this key
            'max_fare': float('-inf'),  # Maximum fare (initialized to negative infinity)
            'min_fare': float('inf')    # Minimum fare (initialized to positive infinity)
        }

    # Update the aggregated data for the current key
    aggregated_data[key]['total_fare'] += fare  # Add the current fare to the total fare
    aggregated_data[key]['trip_count'] += 1  # Increment the trip count
    aggregated_data[key]['max_fare'] = max(aggregated_data[key]['max_fare'], fare)  # Update maximum fare
    aggregated_data[key]['min_fare'] = min(aggregated_data[key]['min_fare'], fare)  # Update minimum fare

# Emit the aggregated output in a tab-separated format for the reducer
for key, values in aggregated_data.items():
    # Output format: taxi_id, trip_type (key), followed by total fare, trip count, max fare, min fare
    print(f"{key}\t{values['total_fare']},{values['trip_count']},{values['max_fare']},{values['min_fare']}")
