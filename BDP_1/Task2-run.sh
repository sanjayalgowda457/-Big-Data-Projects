#!/bin/bash

# Remove any previous output
hadoop fs -rm -r /Output/Task2

# Read the number of allowed iterations from the first line of the initialization file
max_iterations=$(head -n 1 initialization.txt | awk '{print $1}')
iteration=1

# Extract the initial medoids (starting from line 2 onward) and store them in 'medoids_update.txt'
tail -n +2 initialization.txt > medoids_update.txt

# Loop through the clustering process, stopping when the maximum iterations are reached or convergence is achieved
while (( $(echo "$iteration <= $max_iterations" | bc -l) ))
do
    # Remove any previous output from the current iteration
    hadoop fs -rm -r /output/clustering_round_iteration

    # Run the Hadoop job with MapReduce for the k-medoids clustering
    hadoop jar ./hadoop-streaming-3.1.4.jar \
        -D mapred.reduce.tasks=3 \
        -file initialization.txt \
        -file Task2_mapper.py \
        -mapper ./Task2_mapper.py \
        -file Task2_reducer.py \
        -reducer ./Task2_reducer.py \
        -input /Input/Trips.txt \
        -output /output/clustering_round_iteration \
        -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

    # Fetch the latest medoids output from Hadoop and store in 'medoids_update.txt'
    hadoop fs -getmerge /output/clustering_round_iteration/part* medoids_update.txt

    # Check for convergence by running the Python checker script
    convergence_status=$(python Task2_mapper_reader.py)

    # If the medoids have converged, exit the loop
    if [ "$convergence_status" == "1" ]; then
        echo "Convergence achieved at iteration $iteration."
        break
    fi

    # Copy the updated medoids for the next iteration
    cp medoids_update.txt initialization.txt

    # Increment the iteration counter
    iteration=$(echo "$iteration + 1" | bc)
done

# creating the directory for Task2
hadoop fs -mkdir -p /Output/Task2/

# Move the final clustering result to the output directory
hadoop fs -cp /output/clustering_round_iteration/part* /Output/Task2/
