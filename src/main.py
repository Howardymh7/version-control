from datetime import datetime

# Define the file path
file_path = "/repo/version-control/src/version.md"

# Get the current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write the timestamp to version.md
with open(file_path, "w") as file:
    file.write(f"Version generated on: {current_time}\n")

print(f"Timestamp written to {file_path}")
