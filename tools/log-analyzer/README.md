# SSH Log Analyzer

A beginner-friendly Python tool that analyzes sample SSH authentication logs, counts failed login attempts per IP address, flags suspicious activity, and exports a CSV report.

## Features

- Reads SSH authentication logs from `auth.log`.
- Extracts IP addresses associated with failed password attempts.
- Counts failed attempts per IP address.
- Flags an IP as `SUSPICIOUS` when it has 5 or more failed attempts.
- Exports results to `report.csv`.
- Handles a missing log file with an error message.

## Requirements

- Python 3
- No external packages required.

## How to run

Keep `logparser.py` and `auth.log` in the same directory, then run:

```powershell
python .\logparser.py
```

The script prints a summary and creates `report.csv` in the current directory.

## Files

- `logparser.py` — log analysis script.
- `auth.log` — fictional sample SSH authentication logs.
- `report.csv` — generated when the script runs.
- `README.md` — project documentation.

## Threshold test

The sample includes five failed attempts from `192.0.2.10`, so that address should be marked `SUSPICIOUS`. The `192.0.2.0/24` range is reserved for documentation and examples.

## Limitations

This is an educational parser for a supplied log file. It does not monitor a live system, verify that an IP is malicious, or block connections. A threshold is a review signal, not proof of an attack.

## Safe use

Use only logs you are authorized to analyze. All included log events and addresses are fictional examples.
