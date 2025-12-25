This project is a Python-based log anomaly detection tool designed to identify potential brute-force login attacks by analysing authentication logs (auth.log style files).

The tool parses raw log data, extracts source IP addresses associated with failed login attempts, and flags IPs that exceed a configurable threshold — a common detection technique used in SOC environments and SIEM platforms.

The project focuses on reliability, clarity, and detection logic, mirroring how real-world security teams validate telemetry before applying alerts.

🎯 Why This Project Exists

In real cybersecurity environments:

Logs are often messy, incomplete, or empty

Detection logic frequently fails due to bad parsing or assumptions

Analysts must validate log ingestion before trusting alerts

This project intentionally surfaces and solves those problems by:

Verifying raw log content before parsing

Using simple, explainable detection logic

Separating ingestion, parsing, and detection stages

🧠 What This Tool Detects

✅ Multiple failed login attempts
✅ Repeated authentication failures from the same IP
✅ Potential brute-force activity based on thresholds

🚫 Not a full SIEM
🚫 No ML / anomaly scoring (by design — clarity over complexity)

🛠️ How It Works (Step-by-Step)

Reads authentication logs from a specified file path

Validates file content (prevents false “no detection” scenarios)

Extracts IP addresses using regex

Counts failed login attempts per IP

Flags suspicious IPs exceeding a configurable threshold

This mirrors how detection rules work in tools like:

Splunk

Microsoft Sentinel

Elastic SIEM

🧩 Detection Logic

Failed login attempts are identified by keyword matching (Failed password)

IP addresses are extracted using regex

Each IP is counted

IPs exceeding the threshold are reported as suspicious

Threshold can be adjusted depending on environment sensitivity.

📂 Project Structure
Log-Anomaly-Detector/
│
├── detector.py          # Main detection script
├── Logs/
│   └── auth.log         # Sample authentication log file
├── README.md

▶️ How to Run
1️⃣ Clone the repository
git clone https://github.com/yourusername/log-anomaly-detector.git
cd log-anomaly-detector

2️⃣ Update log file path (Windows example)
LOG_FILE = r"F:\workspace\Log anomaly detector\Logs\auth.log"

3️⃣ Run the detector
python detector.py

📤 Sample Output
Suspicious IPs detected (failed login threshold exceeded):

192.168.1.10 → 3 failed attempts
203.0.113.50 → 3 failed attempts


If no IP exceeds the threshold:

No IPs exceeded the threshold.

⚠️ Key Lessons Learned

Empty logs = no detections, even if logic is correct

Always validate raw data before debugging detection rules

Regex failures are often caused by incorrect assumptions, not syntax

Simple detection logic is often more reliable than complex models

These lessons closely reflect real SOC troubleshooting scenarios.

🚀 Future Improvements

Planned extensions:

Time-based detection windows

Username-based analysis

Geo-IP enrichment

Output to CSV / JSON

Integration with alerting systems
