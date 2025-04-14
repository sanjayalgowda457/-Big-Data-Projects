-- Load the necessary datasets from HDFS with new variable names
national_olympic_committee = LOAD 'hdfs:///input/noc_region.csv' USING PigStorage(',') AS (noc_id:int, noc_code:chararray, region_name:chararray);
person_region_info = LOAD 'hdfs:///input/person_region.csv' USING PigStorage(',') AS (person_id:int, region_id:int);
personal_information = LOAD 'hdfs:///input/person.csv' USING PigStorage(',') AS (person_id:int, name:chararray, gender:chararray, height_cm:int);
competition_event = LOAD 'hdfs:///input/competitor_event.csv' USING PigStorage(',') AS (event_id:int, competitor_id:int, medal_id:int);
medal_info = LOAD 'hdfs:///input/medal.csv' USING PigStorage(',') AS (medal_id:int, medal_title:chararray);

-- Combine competition events with their respective medals
competitor_medals = JOIN competition_event BY medal_id, medal_info BY medal_id;

-- Select only those records that correspond to gold medals
gold_medal_winners = FILTER competitor_medals BY medal_info::medal_title == 'Gold';

-- Merge with person region info to associate medalists with their regions
gold_with_region = JOIN gold_medal_winners BY competition_event::competitor_id, person_region_info BY person_id;

-- Join with the national Olympic committee to fetch region names
gold_region_info = JOIN gold_with_region BY person_region_info::region_id, national_olympic_committee BY noc_id;

-- Group the results by region name and calculate the total gold medals per region
gold_medal_distribution = GROUP gold_region_info BY national_olympic_committee::region_name;

-- Generate a dataset with the region and count of gold medals
gold_count_by_region = FOREACH gold_medal_distribution GENERATE group AS region_name, COUNT(gold_region_info) AS total_gold_medals;

-- Order the results: first by total gold medals (descending), then by region name (ascending)
ordered_gold_counts = ORDER gold_count_by_region BY total_gold_medals DESC, region_name ASC;

-- Save the final output to HDFS
STORE ordered_gold_counts INTO 'hdfs:///output/task1' USING PigStorage(',');
