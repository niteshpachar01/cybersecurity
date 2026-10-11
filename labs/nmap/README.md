# Nmap — Learning Notes

This page records beginner-level Nmap practice through Day 16. Scanning is restricted to my own lab systems or systems for which I have explicit permission.

## Topics covered
- Host discovery and the purpose of identifying live hosts
- Basic port scanning
- Reading the PORT, STATE, and SERVICE columns
- Awareness of options such as -p, -sV, -O, and -Pn
- Comparing a dedicated scanner with a small Python TCP socket scanner

## Commands to understand

```bash
# Discover hosts on an explicitly authorized lab network
nmap -sn <authorized-lab-network>

# Scan selected ports on an authorized lab host
nmap -p 22,80,443 <authorized-lab-host>

# Request service/version detection on an authorized lab host
nmap -sV <authorized-lab-host>

# Treat a host as online when discovery probes may be blocked
nmap -Pn <authorized-lab-host>
```

Replace placeholders with the IP or range assigned to your lab. Do not scan public targets without permission.

## How to read results
- **PORT** — port number and transport protocol, for example 80/tcp
- **STATE** — observed state, such as open, closed, or filtered
- **SERVICE** — service associated with the port; version detection may provide more evidence

An open port does not by itself prove a vulnerability.

## Day 16 lab note
The learning record says TryHackMe Nmap Live Host Discovery and Basic Port Scans were completed, and that the Python scanner was compared conceptually with Nmap on the same authorized VM.

**Evidence limitation:** Exact target details and port-by-port outputs were not retained in the available progress notes. This page does not claim a verified one-to-one comparison or list invented scan results. If the original terminal output is available later, add sanitized screenshots and a factual comparison.

## Future evidence checklist
1. Record lab scope and target type, redacting sensitive details.
2. Record the exact command used.
3. Add sanitized output or a screenshot.
4. Explain what the result means and does not prove.
5. Compare with the Python scanner only if both were run against the same target and ports.

## Responsible use
Use Nmap only on systems you own or have explicit permission to test. Never upload credentials or sensitive security data.
