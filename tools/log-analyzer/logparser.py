"""Analyze SSH authentication logs and export failed-login counts as CSV."""

import argparse
import csv
import ipaddress
import re
import sys
from collections import Counter
from pathlib import Path

DEFAULT_LOG = Path(__file__).resolve().parent / "auth.log"
DEFAULT_REPORT = Path.cwd() / "report.csv"
FAILED_PASSWORD = re.compile(
    r"Failed password for (?:invalid user )?\S+ from (\S+) port \d+"
)


def count_failed_attempts(lines):
    """Count failed-password events by valid IPv4 source address."""
    counts = Counter()
    for line in lines:
        match = FAILED_PASSWORD.search(line)
        if not match:
            continue
        try:
            address = ipaddress.ip_address(match.group(1))
        except ValueError:
            continue
        if address.version == 4:
            counts[str(address)] += 1
    return counts


def status_for(count, threshold=5):
    """Return a triage label; the threshold is not proof of malicious activity."""
    return "SUSPICIOUS" if count >= threshold else "Normal"


def write_report(counts, report_path, threshold=5):
    """Write a CSV report ordered by descending count, then IP address."""
    with Path(report_path).open("w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(["IP Address", "Failed Attempts", "Status"])
        for address, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
            writer.writerow([address, count, status_for(count, threshold)])


def positive_int(value):
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be a whole number") from exc
    if number < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return number


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Count failed SSH password logins by source IP."
    )
    parser.add_argument("--log", type=Path, default=DEFAULT_LOG,
                        help="input log file (default: auth.log beside this script)")
    parser.add_argument("--output", type=Path, default=DEFAULT_REPORT,
                        help="CSV output path (default: report.csv in current folder)")
    parser.add_argument("--threshold", type=positive_int, default=5,
                        help="failed attempts needed for SUSPICIOUS label (default: 5)")
    args = parser.parse_args(argv)

    try:
        if args.log.resolve() == args.output.resolve():
            parser.error("input log and output CSV must be different files")
        with args.log.open("r", encoding="utf-8", errors="replace") as log_file:
            counts = count_failed_attempts(log_file)
        write_report(counts, args.output, args.threshold)
    except OSError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print("Failed SSH password attempts by source IP:")
    if not counts:
        print("No matching failed-password events found.")
    for address, count in counts.most_common():
        print(f"{address}: {count} — {status_for(count, args.threshold)}")
    print(f"\nCSV report saved to: {args.output}")
    print("Note: a threshold is a review signal, not proof of an attack.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
