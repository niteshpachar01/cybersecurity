# Security Tools

A collection of small Python utilities and Bash scripts built while learning cybersecurity fundamentals. Each tool has its own folder and README with usage details.

## Available Tools

| Tool | Purpose | Directory |
| --- | --- | --- |
| **File Listing** | Lists files in a selected directory | [filelisting](./filelisting/) |
| **File Hashing** | Calculates file hashes, including MD5 and SHA-256 | [filehashing](./filehashing/) |
| **Threaded TCP Port Scanner** | Checks a specified TCP port range on authorized targets | [portscanner](./portscanner/) |
| **Log Analyzer** | Parses sample authentication logs to identify login-related events | [log-analyzer](./log-analyzer/) |
| **Bash Scripts** | Reports system information and permissions, and backs up directories | [bashscripts](./bashscripts/) |

## Project Layout

```text
tools/
├── bashscripts/
│   ├── directory_backup/
│   ├── permission_report/
│   └── system_info/
├── filehashing/
├── filelisting/
├── log-analyzer/
├── portscanner/
└── README.md
```

## How to Use

Open the README in the relevant tool directory for its requirements, usage examples, implementation notes, and learning objectives. Run scripts only in environments you control.

## Responsible Use

These tools are educational and intended for defensive learning or authorized testing. Do not scan, probe, or analyze systems or data without permission. Use synthetic or appropriately sanitized logs; never commit credentials, tokens, private personal data, or sensitive real-world log contents.
