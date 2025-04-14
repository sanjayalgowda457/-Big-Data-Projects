#!/usr/bin/env python3
import sys

# This reducer just reads in the sorted key-value pairs and outputs them in the original order
for line in sys.stdin:
    line = line.strip()
    if line:
        total_trips, company_id = line.split('\t')
        print(f"{company_id}\t{total_trips}")
