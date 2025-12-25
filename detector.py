from pathlib import Path
from collections import defaultdict
import re

BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "Logs" / "auth.log"

THRESHOLD = 3

print("Reading log file:", LOG_FILE)

ip_pattern = re.compile(r"\d{1,3}(?:\.\d{1,3}){3}")
failed_attempts = defaultdict(int)

with open(LOG_FILE, "r", encoding="utf-8-sig", errors="ignore") as file:
    for line in file:
        for ip in ip_pattern.findall(line):
            failed_attempts[ip] += 1

print("\nSuspicious IPs (threshold exceeded):\n")

for ip, count in failed_attempts.items():
    if count >= THRESHOLD:
        print(f"IP: {ip} | Attempts: {count}")
