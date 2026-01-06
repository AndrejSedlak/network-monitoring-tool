import csv
from datetime import datetime


def parse_events(csv_file_path):
    """
    Parse network events from CSV file.

    :param csv_file_path: Path to CSV file with network events
    :return: List of parsed events (list of dictionaries)
    """
    events = []

    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                event = {
                    "timestamp": datetime.strptime(
                        row["timestamp"], "%Y-%m-%d %H:%M:%S"
                    ),
                    "device": row["device"],
                    "interface": row["interface"],
                    "event_type": row["event_type"],
                    "severity": row["severity"],
                    "description": row["description"],
                }
                events.append(event)

            except ValueError as e:
                # Skip malformed rows but keep processing
                print(f"Skipping invalid row: {row} ({e})")

    return events


if __name__ == "__main__":
    # Simple test run
    parsed_events = parse_events("sample-data/events.csv")
    print(f"Loaded {len(parsed_events)} events")

    for event in parsed_events:
        print(event)
