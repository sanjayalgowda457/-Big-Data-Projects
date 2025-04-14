#!/bin/bash

# Remove the previous output directory from HDFS if it exists
hadoop fs -rm -r /Output/Task1

# Execute the Hadoop streaming job
hadoop jar ./hadoop-streaming-3.1.4.jar \
  -D stream.num.map.output.key.fields=2 \
  -D mapred.text.key.partitioner.options=-k1,1 \
  -D mapred.reduce.tasks=3 \
  -file Task1_mapper.py -mapper Task1_mapper.py \
  -file Task1_reducer.py -reducer Task1_reducer.py \
  -input /Input/Trips.txt \
  -output /Output/Task1 \
  -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

