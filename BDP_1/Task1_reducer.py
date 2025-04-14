#!/usr/bin/env python3
import sys

# Initialize variables for tracking the current key and its aggregated data
active_key = None  # Stores the current taxi_id and trip_type combination
total_fare = 0.0   # Accumulates the total fare for the current key
total_trips = 0     # Counts the number of trips for the current key
highest_fare = 0.0  # Tracks the highest fare for the current key
lowest_fare = float('inf')  # Tracks the lowest fare for the current key (initialized to infinity)

# Process each line of input from the mapper's output
for line in sys.stdin:
    key, values = line.strip().split('\t')  # Split input into key (taxi_id, trip_type) and values
    fare_sum, trip_count, max_fare, min_fare = map(float, values.split(','))  # Extract fare data and convert to floats

    # If a new key is encountered (key changes), output the aggregated result for the previous key
    if active_key and active_key != key:
        avg_fare = total_fare / total_trips if total_trips > 0 else 0  # Calculate average fare for the previous key
        taxi_id, trip_type = active_key.split(',')  # Split the active key into taxi_id and trip_type
        # Output the aggregated result in the required format
        print(f"{taxi_id},{trip_type},{int(total_trips)},{highest_fare:.2f},{lowest_fare:.2f},{avg_fare:.2f}")

        # Reset the aggregates for the new key
        total_fare = fare_sum  # Start the aggregation with the fare_sum of the new key
        total_trips = trip_count  # Initialize trip count for the new key
        highest_fare = max_fare  # Set the highest fare for the new key
        lowest_fare = min_fare   # Set the lowest fare for the new key
    else:
        # If the key remains the same, aggregate the fare and trip data
        total_fare += fare_sum  # Accumulate the total fare
        total_trips += trip_count  # Increment the trip count
        highest_fare = max(highest_fare, max_fare)  # Update the highest fare if applicable
        lowest_fare = min(lowest_fare, min_fare)    # Update the lowest fare if applicable

    # Update the active key to the current key being processed
    active_key = key

# Output the final key's aggregated result after the loop ends
if active_key:
    avg_fare = total_fare / total_trips if total_trips > 0 else 0  # Calculate the average fare for the last key
    taxi_id, trip_type = active_key.split(',')  # Split the final key into taxi_id and trip_type
    # Output the final result for the last key
    print(f"{taxi_id},{trip_type},{int(total_trips)},{highest_fare:.2f},{lowest_fare:.2f},{avg_fare:.2f}")
