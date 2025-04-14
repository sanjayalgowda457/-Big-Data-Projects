#!/usr/bin/env python3
import sys

# This mapper reads company_id and total_number_of_trips, then outputs the trip count as the key
# and company_id as the value to allow sorting by trip count in the reducer.
for line in sys.stdin:
    line = line.strip()  # Remove any surrounding whitespace or newline characters
    if line:
        # Split the line into company_id and total_trips (tab-separated)
        company_id, total_trips = line.split('\t')
        # Output the total_trips first for sorting purposes, followed by the company_id
        print(f"{total_trips}\t{company_id}")
