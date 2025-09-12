# Configuring python-json-logger
print("Configuring python-json-logger")
print("------------\n")


import sys
import logging
from pythonjsonlogger.json import JsonFormatter

json_logger = logging.getLogger("json.logger")
json_logger.setLevel(logging.INFO)

json_hd = logging.StreamHandler(sys.stdout)

json_formatter = JsonFormatter(

        "{asctime}{levelname}{message}",
        style = "{",
        json_indent = 4,
        rename_fields = {"asctime": "timestamp", "levelname": "severity"}
)

json_hd.setFormatter(json_formatter)

json_logger.addHandler(json_hd)

json_logger.info("Structured logging")


# Logging with extra context

print("Logging with extra context")
print("------------\n")

extra_content = {

    "user_name": "devops",
    "request_id": "request-12345",
    "source_ip": "10.0.0.1"
}

json_logger.warning("Rquest took longer than 5s", extra = extra_content)


# Logging exceptions as JSON

print(" Logging exceptions as JSON")
print("------------\n")

try:
    result = 1/0
except ZeroDivisionError:
    json_logger.exception(
        "Unexpected calculation error",
        extra = {"operation": "Division"}
    )
