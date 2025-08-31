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


def read_by_level_and_message(logs, level=None, message_substring=None):
        
        for log in logs:
             if (
                  level is not None 
                  and log.get("level", "").lower() != level.lower()
             ):
                  continue
             if(
                  message_substring is not None
                  and message_substring.lower() not in log.get("message", "").lower()
             ):
                  continue
             yield log
def extract_field(logs, field=None):
     for log in logs:
          yield log.get(field, "").strip()

def extract_log_by_n_line(logs, n):
     count = 0
     for log in logs:
          if count >= n:
               break
          yield log
          count += 1


log_by_line = read_the_file("large_logs.txt")
log_by_level_and_message= read_by_level_and_message(log_by_line,"Error")
log_by_field = extract_field(log_by_level_and_message,"message")


for log in extract_log_by_n_line(log_by_field, 10):
     print(log)

print("Generator object sizes (in bytes):",
      sys.getsizeof(log_by_line),
      sys.getsizeof(log_by_level_and_message),
      sys.getsizeof(log_by_field)
     )
