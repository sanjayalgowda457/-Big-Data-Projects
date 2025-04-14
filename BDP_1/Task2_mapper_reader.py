#!/usr/bin/env python

# Load the initial centroids from initialization.txt
initial_medoids = []
with open('initialization.txt') as file_init:
    data_lines = file_init.readlines()
    
    # Skip header line if it's not numeric (this is often used for iteration count or metadata)
    try:
        float(data_lines[0].split()[0])
    except (ValueError, IndexError):
        data_lines = data_lines[1:]  # If not numeric, skip the first line

    # Process each line for coordinate extraction
    for line in data_lines:
        line = line.strip()  # Remove leading/trailing whitespace
        if line:
            coordinates = line.split()  # Split line by whitespace to extract coordinates
            if len(coordinates) == 2:  # Ensure there are exactly two coordinate values
                initial_medoids.append([float(coordinates[0]), float(coordinates[1])])  # Append coordinates as floats

# Load the newly calculated centroids from medoids_update.txt
revised_medoids = []
with open('medoids_update.txt') as file_update:
    updated_lines = file_update.readlines()
    
    # Extract new centroid coordinates
    for line in updated_lines:
        line = line.strip()  # Remove leading/trailing whitespace
        if line:
            coordinates = line.split()  # Split line by whitespace to extract coordinates
            if len(coordinates) == 2:  # Ensure there are exactly two coordinate values
                revised_medoids.append([float(coordinates[0]), float(coordinates[1])])  # Append coordinates as floats

# Check if centroids have converged by comparing both sets
has_converged = all(
    abs(initial_medoids[i][0] - revised_medoids[i][0]) < 1 and  # Check if x-coordinates are within a threshold
    abs(initial_medoids[i][1] - revised_medoids[i][1]) < 1  # Check if y-coordinates are within a threshold
    for i in range(len(initial_medoids))  # Iterate over each medoid
)

# Output the convergence result
if has_converged:
    print(1)  # Convergence achieved
else:
    print(0)  # Not yet converged
