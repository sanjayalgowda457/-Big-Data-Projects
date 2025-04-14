#!/usr/bin/env python3
import sys

# Mapper to count trips by taxi company
for line in sys.stdin:
    # Split the input line into company and trip_id (tab-separated)
    company, trip_id = line.strip().split('\t')
    
    # Emit the company name and the number 1 (indicating one trip)
    print(f"{company}\t1")
