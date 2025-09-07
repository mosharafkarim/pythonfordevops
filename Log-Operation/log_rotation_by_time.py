import logging
import logging.handlers
import os
import time

def cleanup_file(base_name :str):
    for file_name in os.listdir("."):
        if file_name.startswith(base_name):
            try:
                os.remove(file_name)
            except FileNotFoundError:
                pass

print("Time-based log rotation with TimedRotatingFileHandler")
print("-------\n")

timedbased_rotating_file = "timebasedrotatingfile.log"

cleanup_file(timedbased_rotating_file)

logger = logging.getLogger("file.rotation")
logger.setLevel(logging.INFO)

timebased_fh = logging.handlers.TimedRotatingFileHandler(
    filename=timedbased_rotating_file,
    when="s",
    interval=3,
    delay=True,
    backupCount=2,
    encoding="utf-8"
)

timebased_fh.setFormatter(
    logging.Formatter("%(levelname)-8s %(message)s")
)

logger.addHandler(timebased_fh)

for i in range(30):
    logger.info(f"Entry {i}: {'Z' * 50}")
    time.sleep(0.2)
