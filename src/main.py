# with chat-gpt assistance
from zoneinfo import ZoneInfo
from datetime import datetime
#import pytz

# Define the file path
file_path = "/repo/version-control/src/version.md"

# Get the current date and time and define time zone

#tz = pytz.timezone(America/Los_Angeles)
current_time = datetime.now(ZoneInfo('America/Los_Angeles')).strftime("%Y-%m-%d %H:%M:%S")

# Write the timestamp to version.md
with open(file_path, "w") as file:
    file.write(f"Version generated on: {current_time}\n")

print(f"Timestamp written to {file_path}")
