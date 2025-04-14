#!/usr/bin/env python
import sys

# List to store dropoff locations for each cluster
cluster_locations = []
# Variable to track the currently active cluster being processed
active_cluster = None

# Function to calculate total cost (sum of squared distances to a medoid)
def calculate_total_cost(medoid, points):
    # Sum the squared distances from the medoid to each point in the cluster
    return sum([(x - medoid[0]) ** 2 + (y - medoid[1]) ** 2 for x, y in points])

try:
    # Process each input line from the mapper
    for input_line in sys.stdin:
        input_line = input_line.strip()  # Remove leading/trailing whitespace

        # Validate the input format (check if the line contains a tab separator)
        if '\t' not in input_line:
            sys.stderr.write("Skipping invalid line (no tab separator): {}\n".format(input_line))  # Log invalid line
            continue

        # Split the input line into the cluster ID and trip info (dropoff coordinates)
        cluster_id, trip_info = input_line.split('\t')
        try:
            # Extract dropoff x and y coordinates from the trip info
            dropoff_x, dropoff_y = map(float, trip_info.split(',')[1:])
        except ValueError as error:
            # Log and skip the line if it contains invalid coordinates
            sys.stderr.write("Skipping line with invalid coordinates: {} Error: {}\n".format(input_line, error))
            continue

        # If still processing the same cluster, add the dropoff point to the list of locations
        if active_cluster == cluster_id:
            cluster_locations.append([dropoff_x, dropoff_y])
        else:
            # If the cluster has changed, compute the new medoid for the previous cluster
            if active_cluster is not None:
                # Calculate the new medoid (point with minimum total cost)
                new_medoid = min(cluster_locations, key=lambda point: calculate_total_cost(point, cluster_locations))
                # Output the new medoid's coordinates
                print("{}\t{}".format(new_medoid[0], new_medoid[1]))

            # Switch to the new cluster and reset the locations list for the new cluster
            active_cluster = cluster_id
            cluster_locations = [[dropoff_x, dropoff_y]]

    # After processing all lines, handle the final cluster
    if active_cluster is not None:
        new_medoid = min(cluster_locations, key=lambda point: calculate_total_cost(point, cluster_locations))
        print("{}\t{}".format(new_medoid[0], new_medoid[1]))

# Catch any errors during the reducer process
except Exception as error:
    sys.stderr.write("Error encountered during reducer processing: {}\n".format(error))
    sys.exit(1)  # Exit with error code
