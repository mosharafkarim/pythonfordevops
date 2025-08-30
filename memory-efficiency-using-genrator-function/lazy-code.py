# Code for memory efficient message/custom field extraction from log file
import sys
import json

def read_the_file(filepath):

    with open(filepath, 'r') as file:

        for line in file:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)


log_by_line = read_the_file("large_logs.txt")
print(next(log_by_line))
