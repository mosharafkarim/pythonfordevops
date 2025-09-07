# size-based log rotation
import os
import time
import logging
import logging.handlers

def cleanup_logfiles(filename):
    for i in os.listdir("."):
        if i.startswith(filename):
            try:
                os.remove(filename)
            except FileNotFoundError:
                pass
            


print("Size-based log rotation with RotatingFileHandler")
print("-------\n")

rotating_flie_name = "rotatingfile.log"

cleanup_logfiles(rotating_flie_name)

logger = logging.getLogger("file.rotating")
logger.setLevel(logging.DEBUG)

rotating_fh = logging.handlers.RotatingFileHandler(
    rotating_flie_name,
    maxBytes=500,
    backupCount=2,
    encoding="utf-8",  
)

rotating_fh.setFormatter(
    logging.Formatter("%(levelname)-8s %(message)s")
)

logger.addHandler(rotating_fh)

for i in range(40):
    logger.info(f"Entry {i}: {'Z' * 50}")
    time.sleep(0.05)


