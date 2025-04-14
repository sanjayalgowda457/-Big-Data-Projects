#!/usr/bin/env python
import sys
from math import sqrt

# Load the initial medoids (cluster centers) from the file
cluster_centers = []
with open('initialization.txt') as file:
    lines = file.readlines()
    try:
        # Skip the first line if it contains non-numeric values (likely metadata or iteration count)
        float(lines[0].split()[0])
    except (ValueError, IndexError):
        lines = lines[1:]  # Skip the first line if it's non-numeric

    # Read each medoid's (cluster center's) coordinates from the file
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        if line:
            coords = line.split()  # Split the line to extract coordinates
            if len(coords) == 2:  # Ensure the line has two coordinate values
                cluster_centers.append([float(coords[0]), float(coords[1])])  # Append the coordinates as floats

# Process each line of the input dataset (Trips.txt)
for record in sys.stdin:
    try:
        record = record.strip()  # Remove leading/trailing whitespace
        trip_data = record.split(',')  # Split the line to get the trip details

        # Check if the line contains the expected number of fields (at least 8)
        if len(trip_data) < 8:
            sys.stderr.write("Skipping invalid input: {}\n".format(record))  # Log invalid input
            continue

        # Extract dropoff location (x, y coordinates) from the trip data
        dropoff_x = float(trip_data[6])  # Dropoff x-coordinate
        dropoff_y = float(trip_data[7])  # Dropoff y-coordinate

        # Initialize variables to find the closest medoid (cluster center)
        min_distance = float('inf')  # Start with an infinitely large distance
        nearest_cluster = -1  # Initialize the nearest cluster to an invalid value

        # Iterate through all medoids (cluster centers) and find the nearest one based on Euclidean distance
        for idx, center in enumerate(cluster_centers):
            # Compute Euclidean distance between the trip's dropoff point and the medoid
            distance = sqrt((dropoff_x - center[0]) ** 2 + (dropoff_y - center[1]) ** 2)
            # Update the nearest cluster if the current distance is smaller than the previous minimum
            if distance < min_distance:
                min_distance = distance
                nearest_cluster = idx

        # Output the nearest cluster and the trip's dropoff coordinates
        print("{}\t{}, {}, {}".format(nearest_cluster, trip_data[0], dropoff_x, dropoff_y))

    except Exception as ex:
        # Log any errors encountered while processing the record
        sys.stderr.write("Error processing record {}: {}\n".format(record, ex))
        sys.exit(1)  # Exit the script with an error code
