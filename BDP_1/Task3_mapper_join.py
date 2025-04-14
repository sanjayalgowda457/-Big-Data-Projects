#!/usr/bin/env python3
import sys

# Mapper for joining the Trips and Taxis files
for line in sys.stdin:
    data = line.strip().split(',')  # Split the input line by commas to get individual fields
    
    # If it's from the Trips.txt file (based on the number of fields being 8)
    if len(data) == 8:
        # Emit Taxi# as the key and trip data (prefixed with "TRIP")
        print(f"{data[1]}\tTRIP,{data[0]}")
    
    # If it's from the Taxis.txt file (based on the number of fields being 4)
    elif len(data) == 4:
        # Emit Taxi# as the key and company data (prefixed with "TAXI")
        print(f"{data[0]}\tTAXI,{data[1]}")
