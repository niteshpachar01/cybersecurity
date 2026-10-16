import re
import csv
from collections import Counter

LOG_FILE = "auth.log"
CSV_FILE = "report.csv"
THRESHOLD = 5

failed_attempts = Counter()
pattern = re.compile(
    r"Failed password for .*? from (\d{1,3}(?:\.\d{1,3}){3})"
)

try:
    with open(LOG_FILE, "r", encoding="utf-8") as file:
        for line in file:
            match = pattern.search(line)
            if match:
                failed_attempts[match.group(1)] += 1

    print("Failed SSH login attempts by IP:")

    if not failed_attempts:
        print("No failed SSH login attempts found.")

    for ip, count in failed_attempts.most_common():
        status = "SUSPICIOUS" if count >= THRESHOLD else "Normal"
        print(f"{ip}: {count} — {status}")

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["IP Address", "Failed Attempts", "Status"])
        for ip, count in failed_attempts.most_common():
            status = "SUSPICIOUS" if count >= THRESHOLD else "Normal"
            writer.writerow([ip, count, status])

    print(f"\nCSV report saved to {CSV_FILE}")

except FileNotFoundError:
    print(f"Error: {LOG_FILE} was not found in this folder.")
