README
**************************************************************************************************

OVERVIEW
**************************************************************************************************

This Assignment 2 involves processing various datasets related to Olympic events using Apache Pig on HDFS. It includes tasks that leverage Pig scripts to analyze data pertaining to athletes, events, and results stored in CSV format.

NOTES:

Ensure that your Hadoop environment is correctly set up before executing the tasks.
**************************************************************************************************

FILE MANAGEMENT INSTRUCTIONS

Unzipping and Transferring Files:

Unzip the File:
Begin by unzipping the file named 's4021582_BDP_A2.zip' on your local machine to extract its contents.

Transfer Files from Local Machine to Jumphost:
Use secure copy (SCP) or your preferred file transfer method to move the extracted files from your local machine to the jumphost.

Move Files from Jumphost to Master Node:
From the jumphost, transfer the files to the master node of your cluster, ensuring that all files are placed within the same directory for consistent access.

**************************************************************************************************

Before running any tasks, create an input folder in HDFS and upload all necessary input files. Follow these steps:
**************************************************************************************************
Step 1: Create Input Directory on HDFS
Create a directory named /input on HDFS to store all input files:

hadoop fs -mkdir /input
**************************************************************************************************

Step 2: Upload Input Files
Upload the input datasets from your local machine to the /input directory on HDFS:

hadoop fs -put /path/to/local/noc_region.csv /input/
hadoop fs -put /path/to/local/person_region.csv /input/
hadoop fs -put /path/to/local/person.csv /input/
hadoop fs -put /path/to/local/competitor_event.csv /input/
hadoop fs -put /path/to/local/medal.csv /input/

input folder files are 
/input/noc_region.csv
/input/person_region.csv
/input/person.csv
/input/competitor_event.csv
/input/medal.csv
**************************************************************************************************

Step 3: Verify Uploads
Confirm that all files are uploaded correctly by listing the contents of the /input directory:

hadoop fs -ls /input/
**************************************************************************************************

Step 4:Clearing Output Directory:
 Before executing the tasks, ensure that no previous output data interferes with the upcoming executions. You can clear any existing output by running the following command:

hadoop fs -rm -r /output/*
**************************************************************************************************

Task 1: Medal Distribution Analysis

Objective: Analyze the distribution of medals across different countries and types of medals.

Files:
task1.pig: Processes athlete and medal data to calculate medal distribution.
Execution:
Run the Pig script and the results will be stored in /output/task1:

pig -x mapreduce task1.pig
**************************************************************************************************

Task 2.1: Medal Statistics by Country

Objective: Compute medal statistics by country from the Olympics dataset.

Files:
task2-1.pig: Computes detailed statistics of medals won by each country.
Execution:
Run the Pig script and the results will be stored in /output/task2-1:

pig -x mapreduce task2-1.pig
**************************************************************************************************

Task 2.2: Athlete Performance Analysis

Objective: Analyze individual athlete performances to find top performers.

Files:
task2-2.pig: Analyzes individual athlete performances.
task2udf.py: Python UDF used to enhance data processing.
Execution:
Run the Pig script and the results will be stored in /output/task2-2:

pig -x mapreduce task2-2.pig
**************************************************************************************************

OUTPUT LOCATION

Outputs of the tasks are stored in the following HDFS directories:

Task 1: /output/task1
Task 2.1: /output/task2-1
Task 2.2: /output/task2-2
**************************************************************************************************