# TryHackMe — Wireshark: The Basics

**Status in learning log:** Reported completed on Day 14.

## Learning summary
- Understand Wireshark's role as a packet-analysis tool.
- Select an appropriate interface and inspect a capture.
- Use packet list, packet details, and packet bytes panes.
- Apply display filters to narrow visible traffic.
- Recognize DNS and TCP traffic in a beginner lab.

## Filters reviewed

    dns
    tcp
    http
    ip.addr == <address>
    tcp.port == <port>

Replace placeholders with values from an authorized lab capture. Filters are examples, not evidence that a particular capture is committed.

## Key lesson
Packet analysis is most useful when the analyst connects the packet fields to a question: who is communicating, which protocol is involved, and what the capture can or cannot establish.

## Evidence note
Detailed notes were maintained in Notion. This public write-up is a concise summary; this repository audit did not independently verify the room-completion dashboard or recover a room-specific screenshot.
