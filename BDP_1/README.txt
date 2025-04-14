README

OVERVIEW
This Assignment contains three tasks implemented using MapReduce to analyze taxi trip data. The tasks involve processing Trips.txt and Taxis.txt stored on HDFS using Python MapReduce scripts. Each task involves different aspects of taxi trip analysis, including trip classification, clustering, and sorting.
**************************************************************************************************
Notes
	• Ensure that your Hadoop environment is correctly set up before executing the tasks.
     
        • before executing any tasks, give permission for execution with the chmod +x runfile name 
**************************************************************************************************
Task 1: Trip Classification and Fare Analysis
Objective: For each taxi, classify trips into three categories (short, medium, and long) based on the distance traveled. For each taxi and each trip type, calculate the following:
	1	Total number of trips.
	2	Maximum fare.
	3	Minimum fare.
	4	Average fare per trip.

Files:
	•	Task1_mapper.py: Mapper script that processes the trip data, classifies trips based on distance, and performs in-mapper combining.
	•	Task1_reducer.py: Reducer script that aggregates the trip data to calculate the total number of trips, max fare, min fare, and average fare for each taxi and trip type.
	•	Task1-run.sh: Shell script to execute the MapReduce job with 3 reducers.

Execution:
	1	Place all the code files in the same folder on the Hadoop cluster.
	2	Run the shell script:bash 		./Task1-run.sh
	3	The output will be stored in /Output/Task1 which contain  the trip counts and fare 		
		statistics for each taxi and trip type.

**************************************************************************************************

Task 2: K-Medoid Clustering on Dropoff Locations
Objective: Implement the Partitioning Around Medoids (PAM) algorithm using MapReduce to cluster taxi trips based on dropoff locations. The algorithm involves:
	1	Initialize: Select k random data points as medoids.
	2	Assignment: Associate each trip to the nearest medoid.
	3	Update: Swap medoids and compute the total cost to identify the best medoids.
	4	Iteration: Repeat the process until no change in assignments or a specified number of iterations.

Files:
	•	Task2_mapper.py: Mapper script to associate each trip with the nearest medoid.
	•	Task2_reducer.py: Reducer script to update medoids based on the assigned trips.
	•	Task2_mapper_reader.py: Script to check convergence of medoids.
	•	Task2-run.sh: Shell script to run the K-Medoid clustering with 3 reducers.

Execution:
	1	Place all the code files and the initialization.txt file in the same folder.
	2	Run the shell script:bash 		./Task2-run.sh
	3	The output will be stored in /Output/Task2, containing the final medoids for the 
		clusters.

**************************************************************************************************

Task 3: Counting Trips by Taxi Company and Sorting
Objective: This task involves counting the number of trips for each taxi company and sorting the companies based on the total number of trips. The task is divided into three subtasks:
	1	Join Operation: Join Trips.txt and Taxis.txt to associate trips with taxi companies.
	2	Counting Operation: Count the number of trips for each taxi company.
	3	Sorting Operation: Sort the taxi companies in ascending order based on the number of 	
		trips.

Files:
	•	Task3_mapper_join.py: Mapper script for the join operation between Trips.txt and 		
		Taxis.txt.
	•	Task3_reducer_join.py: Reducer script for the join operation.
	•	Task3_mapper_count.py: Mapper script to count the number of trips for each taxi 	
		company.
	•	Task3_reducer_count.py: Reducer script to aggregate the total trips for each company.
	•	Task3_mapper_sort.py: Mapper script to sort taxi companies by total trips.
	•	Task3_reducer_sort.py: Reducer script for sorting taxi companies.
	•	Task3-run.sh: Shell script to run all three subtasks with 3 reducers.

Execution:
	1	Place all the code files in the same folder on the Hadoop cluster.
	2	Run the shell script:bash 		./Task3-run.sh
	3	The final output will be stored in /Output/Task3, containing the sorted list of taxi 		
		companies by trip count.

**************************************************************************************************

General Notes:
	•	All scripts must be placed in the same folder on the Hadoop cluster.
	•	The shell scripts are used to execute the tasks and automate the MapReduce jobs.
	•	Each task uses 3 reducers as per the requirements.
	•	The data files Trips.txt and Taxis.txt must be stored in HDFS before running the 						
		tasks.

**************************************************************************************************

Execution
For each task, run the corresponding shell script:
	•	Task 1: ./Task1-run.sh
	•	Task 2: ./Task2-run.sh
	•	Task 3: ./Task3-run.sh
**************************************************************************************************
Input files: store in HDFS
	•	Trips.txt: /Input/Trips.txt
	•	Taxis.txt: /Input/Taxis.txt
**************************************************************************************************
Output Location
The outputs of the tasks are stored in the following HDFS directories:
	•	Task 1: /Output/Task1
	•	Task 2: /Output/Task2
	•	Task 3: /Output/Task3

