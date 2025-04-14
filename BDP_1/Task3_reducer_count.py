#!/usr/bin/env python3
import sys

# Initialize variables to track the current company and trip count
current_company = None
trip_count = 0

# Process each line of input from the mapper
for line in sys.stdin:
    # Split the line into company name and trip count (tab-separated)
    company, count = line.strip().split('\t')
    count = int(count)  # Convert the count to an integer

    # If the current line belongs to the same company, increment the trip count
    if current_company == company:
        trip_count += count
    else:
        # If the company changes, print the result for the previous company
        if current_company:
            print(f"{current_company}\t{trip_count}")
        # Update the current company and reset the trip count
        current_company = company
        trip_count = count

# Emit the final company's trip count
if current_company:
    print(f"{current_company}\t{trip_count}")
