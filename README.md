# Network Monitoring Tool (Python)
Overview

This project is a simple Python-based network monitoring and analysis tool designed to process network event logs exported in CSV format.
It simulates real-world monitoring data (e.g. from NMS, syslog, or monitoring platforms) and focuses on analyzing network events such as link failures, recoveries, and incidents.

The main goal of this project is to demonstrate:

practical Python usage,
data parsing and analysis,
basic network monitoring concepts.

Features

Parse network event data from CSV files
Track network events per device and interface
Count and classify incidents by severity
Prepare the foundation for downtime and availability analysis


Features

Parse network event data from CSV files

Track network events per device and interface

Count and classify incidents by severity

Prepare the foundation for downtime and availability analysis

Project Structure
network-monitoring-tool/
├── README.md
├── sample-data/
│   └── events.csv
├── parser.py        # (planned) CSV parsing logic
├── analyzer.py      # (planned) event analysis and statistics
└── main.py          # (planned) CLI entry point

Input Data Format

The tool expects network events in CSV format with the following structure:

timestamp,device,interface,event_type,severity,description
2025-01-05 10:15:03,SW1,Gi0/1,LINK_DOWN,CRITICAL,Interface went down
2025-01-05 10:16:12,SW1,Gi0/1,LINK_UP,INFO,Interface restored


timestamp – event time (YYYY-MM-DD HH:MM:SS)
device – network device name
interface – affected interface
event_type – type of event (e.g. LINK_DOWN, LINK_UP)
severity – INFO / WARNING / CRITICAL
description – human-readable event description
Sample data is provided in the sample-data/ directory.

Technologies Used

Python 3
CSV data processing
Standard Python libraries (csv, datetime, collections)

Motivation

This project was created as a learning exercise to:
gain hands-on experience with Python,
practice working with structured monitoring data,
bridge networking knowledge with software development skills.
Future Improvements
Downtime calculation per interface
Event correlation (LINK_DOWN → LINK_UP)
Summary reports (top devices by incidents)
Simple CLI interface
Visualization of incidents (optional)

Author

Andrej Sedlák
Aspiring Python Software Engineer with a networking background
