# Wireshark — Packet Analysis Notes

This page summarizes Wireshark exercises recorded through Day 15. Captures should come only from my own device, lab, or an environment where I have permission.

## Topics practiced
- Inspecting DNS traffic
- Recognizing the TCP three-way handshake: SYN, SYN-ACK, ACK
- Identifying HTTP requests and responses in an appropriate unencrypted lab capture
- Applying display filters
- Using **Follow TCP Stream**
- Learning when **Export Objects** can be useful

## Useful display filters

    dns
    http
    tcp
    tcp.port == 80
    ip.addr == 192.168.1.10

The IP above is only an example. Replace it with an address visible in your own capture. A display filter narrows what Wireshark shows; it does not change the original capture.

## Basic workflow
1. Select the correct capture interface and capture authorized traffic.
2. Generate a simple test request or DNS lookup.
3. Stop the capture and save it only if it contains no sensitive information.
4. Apply a filter such as dns or tcp.
5. Inspect packet details and use Follow TCP Stream when relevant.
6. Interpret what is visible and note capture limitations.

## Day 9 observations recorded

The learning notes describe a DNS query for google.com using resolver 1.1.1.1, a TCP handshake sequence (SYN → SYN-ACK → ACK), and an HTTP GET with a 200 OK response.

These are observations reported in the learning log, not a claim that the original packet capture is included in this repository.

## Day 14–15 practice
- Wireshark: The Basics
- Wireshark: Packet Operations
- Display filters including ip.addr, tcp.port, http, and dns
- Follow TCP Stream and Export Objects

## Evidence and privacy

The Day 17 blog includes screenshots of Nmap output, Wireshark filters, and Follow TCP Stream / Export Objects. The progress record does not confirm a committed raw capture or a dedicated TCP-handshake screenshot in this repository.

Before sharing captures, inspect them for cookies, authorization headers, personal data, private hostnames, internal IPs, and other sensitive information. Do not upload a raw capture publicly unless it has been reviewed and safely sanitized.
