REGISTER 'task2udf.py' USING jython as FillSilver;

-- Load the necessary datasets
athlete_region = LOAD 'hdfs:///input/person_region.csv' USING PigStorage(',') AS (person_id:int, region_id:int);
athlete_details = LOAD 'hdfs:///input/person.csv' USING PigStorage(',') AS (person_id:int, full_name:chararray, gender:chararray, height:int, weight:int);
olympic_region = LOAD 'hdfs:///input/noc_region.csv' USING PigStorage(',') AS (region_id:int, region_code:chararray, region_name:chararray);
competitor_event = LOAD 'hdfs:///input/competitor_event.csv' USING PigStorage(',') AS (event_id:int, athlete_id:int, prize_id:int);
medal_details = LOAD 'hdfs:///input/medal.csv' USING PigStorage(',') AS (prize_id:int, medal_type:chararray);

-- Join operations
region_athlete_info = JOIN athlete_region BY person_id, athlete_details BY person_id;
region_info = JOIN region_athlete_info BY athlete_region::region_id, olympic_region BY region_id;
event_medal_info = JOIN region_info BY region_athlete_info::athlete_region::person_id, competitor_event BY athlete_id;
medal_info = JOIN event_medal_info BY competitor_event::prize_id, medal_details BY prize_id;

-- Filter for gold and silver medals
gold_medal_info = FILTER medal_info BY medal_details::medal_type == 'Gold';
silver_medal_info = FILTER medal_info BY medal_details::medal_type == 'Silver';

-- Count medals by region
gold_medals_by_region = FOREACH (GROUP gold_medal_info BY olympic_region::region_name) GENERATE group AS region_name, COUNT(gold_medal_info) AS total_gold;
silver_medals_by_region = FOREACH (GROUP silver_medal_info BY olympic_region::region_name) GENERATE group AS region_name, COUNT(silver_medal_info) AS total_silver;

-- Combine counts
medal_counts_combined = JOIN gold_medals_by_region BY region_name LEFT OUTER, silver_medals_by_region BY region_name;

-- Use the UDF to adjust for missing silver counts
final_medal_counts = FOREACH medal_counts_combined GENERATE
    gold_medals_by_region::region_name AS Region,
    gold_medals_by_region::total_gold AS Gold,
    FillSilver.fill_missing(silver_medals_by_region::total_silver) AS Silver;

-- Apply correct sorting
sorted_medal_counts = ORDER final_medal_counts BY Gold DESC, Silver DESC, Region ASC;

-- Store the sorted results
STORE sorted_medal_counts INTO 'hdfs:///output/task2-2' USING PigStorage(',');
