# SSH Log Analyzer

A beginner-friendly Python tool that analyzes a supplied SSH authentication log, counts failed password events by valid IPv4 source address, flags high counts for review, and exports a CSV report.

## Features

- Parses failed-password events and counts attempts by source IPv4 address.
- Validates addresses with Python's standard-library `ipaddress` module; malformed addresses and IPv6 entries are ignored.
- Labels an address `SUSPICIOUS` when its count is at least the configured threshold (default: 5).
- Exports a CSV report with address, count, and review label.
- Supports command-line options for the input file, output report, and threshold.
- Reads the default sample log from the same directory as the script, even when launched from another working directory.
- Reports file errors without a traceback.

## Requirements

- Python 3.8 or newer (standard library only).

## Run it

From this folder:

```powershell
python .\logparser.py
```

The default input is `auth.log` beside the script. The CSV output is `report.csv` in your current working directory.

Choose custom paths or a different threshold:

```powershell
python .\logparser.py --log .\auth.log --output .\report.csv --threshold 5
```

See all options:

```powershell
python .\logparser.py --help
```

The threshold must be a positive whole number. The input and output paths must be different.

## Expected sample result

The included fictional sample contains five failed password events from `192.0.2.10` and one from `192.0.2.25`. With the default threshold, the first address is labelled `SUSPICIOUS` and the second `Normal`. Successful-login events are not counted.

The `192.0.2.0/24` network is reserved for documentation and examples.

## Files

- `logparser.py` — parser, counting logic, CLI, and CSV export.
- `auth.log` — fictional sample authentication events.
- `test_logparser.py` — unit tests.
- `report.csv` — generated output; not committed by default.

## Run tests

```powershell
python -m unittest -v
```

## Limitations and safe use

This is an educational parser for a supplied log file; it does not monitor a live system, block connections, or prove that an address is malicious. A threshold is only a triage signal. Use only logs you are authorized to analyze. The included log events use fictional examples.
