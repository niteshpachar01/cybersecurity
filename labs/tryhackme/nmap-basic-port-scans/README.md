# TryHackMe — Nmap: Basic Port Scans

**Status in learning log:** Reported completed on Day 16.

## Learning summary
- Understand what a port scan attempts to determine.
- Read Nmap's PORT, STATE, and SERVICE fields.
- Recognize that open, closed, and filtered describe different observations.
- Know that service/version detection provides additional evidence but is not a guarantee of vulnerability.

## Command patterns

    nmap -p 22,80,443 <authorized-lab-host>
    nmap -sV <authorized-lab-host>

Use only an authorized lab target. Replace the placeholder with the host assigned to your lab.

## Python scanner comparison
The learning record says a Python TCP socket scanner was compared with Nmap on the same authorized VM. The exact target, port range, and paired outputs were not preserved in the available notes, so this write-up does not claim a verified per-port comparison.

## Evidence note
Detailed personal notes were maintained in Notion. This concise summary reflects the reported learning scope; this audit did not independently inspect the platform completion dashboard.
