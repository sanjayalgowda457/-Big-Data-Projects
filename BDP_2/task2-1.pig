-- Load the necessary datasets from HDFS with different variable names for uniq$
athlete_region = LOAD 'hdfs:///input/person_region.csv' USING PigStorage(',') AS (person_id:int, region_id:int);

athlete_details = LOAD 'hdfs:///input/person.csv' USING PigStorage(',') AS (person_id:int, full_name:chararray, gender:chararray, height:int, weight:int);

olympic_region = LOAD 'hdfs:///input/noc_region.csv' USING PigStorage(',') AS (region_id:int, region_code:chararray, region_name:chararray);

competitor_event = LOAD 'hdfs:///input/competitor_event.csv' USING PigStorage(',') AS (event_id:int, athlete_id:int, prize_id:int);

medal_details = LOAD 'hdfs:///input/medal.csv' USING PigStorage(',') AS (prize_id:int, medal_type:chararray);

-- Combine athlete_region with athlete_details to correlate region and athlete details
region_athlete_info = JOIN athlete_region BY person_id, athlete_details BY person_id;

-- Merge the region_athlete_info with olympic_region to align region names
region_info = JOIN region_athlete_info BY athlete_region::region_id, olympic_region BY region_id;

-- Connect the region_info with competitor_event to access event and medal data
event_medal_info = JOIN region_info BY region_athlete_info::athlete_region::person_id, competitor_event BY athlete_id;

-- Link event_medal_info with medal_details to fetch the medal type
medal_info = JOIN event_medal_info BY competitor_event::prize_id, medal_details BY prize_id;

-- Filter to obtain only the gold and silver medals
gold_medal_info = FILTER medal_info BY medal_details::medal_type == 'Gold';
silver_medal_info = FILTER medal_info BY medal_details::medal_type == 'Silver';

-- Count gold medals by region
gold_medals_by_region = FOREACH (GROUP gold_medal_info BY olympic_region::region_name) GENERATE group AS region_name, COUNT(gold_medal_info) AS total_gold;

-- Count silver medals by region
silver_medals_by_region = FOREACH (GROUP silver_medal_info BY olympic_region::region_name) GENERATE group AS region_name, COUNT(silver_medal_info) AS total_silver;

-- Join the gold and silver medal counts using a LEFT OUTER JOIN to ensure all gold medal counts are included
medal_counts_combined = JOIN gold_medals_by_region BY region_name LEFT OUTER, silver_medals_by_region BY region_name;

-- Keep NULL values where silver medals are absent
final_medal_counts = FOREACH medal_counts_combined GENERATE
    gold_medals_by_region::region_name AS Region,
    gold_medals_by_region::total_gold AS Gold,
    silver_medals_by_region::total_silver AS Silver;

-- Sort the final output first by the number of gold medals in descending order, then by region name in ascending order for ties
sorted_medal_counts = ORDER final_medal_counts BY Gold DESC, Region ASC;

-- Store the final sorted results in HDFS
STORE sorted_medal_counts INTO 'hdfs:///output/task2-1' USING PigStorage(',');
