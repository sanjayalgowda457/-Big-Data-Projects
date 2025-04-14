#!/bin/bash

# Remove previous output directories if they exist
hadoop fs -rm -r /Output/join /Output/count /Output/Task3

# Step 1: Join operation (3 reducers)
hadoop jar ./hadoop-streaming-3.1.4.jar \
  -D mapreduce.job.reduces=3 \
  -file ./Task3_mapper_join.py \
  -mapper ./Task3_mapper_join.py \
  -file ./Task3_reducer_join.py \
  -reducer ./Task3_reducer_join.py \
  -input /Input/Trips.txt \
  -input /Input/Taxis.txt \
  -output /Output/join

# Step 2: Counting operation (3 reducers)
hadoop jar ./hadoop-streaming-3.1.4.jar \
  -D mapreduce.job.reduces=3 \
  -file ./Task3_mapper_count.py \
  -mapper ./Task3_mapper_count.py \
  -file ./Task3_reducer_count.py \
  -reducer ./Task3_reducer_count.py \
  -input /Output/join/part-* \
  -output /Output/count

# Step 3: Global sorting operation (ensure distribution across reducers)
# Run a MapReduce job to globally sort the trip counts for taxi companies
# Use a custom comparator for sorting
hadoop jar ./hadoop-streaming-3.1.4.jar \
  -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
  -D stream.num.map.output.key.fields=2 \
  -D mapred.text.key.partitioner.options=-k2,1 \
  -D mapred.text.key.comparator.options='-k1,1n -k2,2' \
  -D mapred.reduce.tasks=3 \
  -file ./Task3_mapper_sort.py \
  -mapper ./Task3_mapper_sort.py \
  -file ./Task3_reducer_sort.py \
  -reducer ./Task3_reducer_sort.py \
  -input /Output/count/part-* \
  -output /Output/Task3 \
  -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
