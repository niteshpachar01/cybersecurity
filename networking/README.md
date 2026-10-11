# Networking Fundamentals — Days 7–8

These notes summarize concepts practiced during the learning plan. They are study notes, not a record of a production network assessment.

## OSI model quick reference

| Layer | Main idea | Example |
| --- | --- | --- |
| 7 — Application | Network services used by applications | HTTP, DNS |
| 6 — Presentation | Data representation and encryption concepts | TLS-related representation concepts |
| 5 — Session | Establishing and managing communication sessions | Session management concepts |
| 4 — Transport | End-to-end delivery and ports | TCP, UDP |
| 3 — Network | Logical addressing and routing | IP |
| 2 — Data Link | Local-link delivery | Ethernet, MAC addresses |
| 1 — Physical | Signals and transmission media | Cable, radio |

The OSI model is a learning model; real protocol stacks do not always map neatly to one layer.

## Core concepts
- **IP address:** logical address used to route packets between networks.
- **MAC address:** link-layer address used for local network delivery.
- **Port:** identifies an application/service endpoint at the transport layer.
- **TCP:** connection-oriented transport with sequencing and acknowledgements.
- **UDP:** connectionless transport with lower protocol overhead and no built-in delivery guarantee.
- **Router:** forwards packets between networks.
- **DNS:** resolves names such as a domain to associated records, often including IP addresses.
- **HTTP:** application protocol for web requests and responses.

## Commands practiced

    ip addr
    ping <authorized-host>
    nslookup example.com
    dig example.com
    curl -I https://example.com

Use public domains for ordinary DNS/HTTP learning and only test hosts within an authorized scope. Command availability depends on the operating system.

## HTTP status code examples
- **200 OK:** request succeeded.
- **301/302:** redirection.
- **400:** bad request.
- **401:** authentication required or failed.
- **403:** server refuses the request.
- **404:** resource not found.
- **500:** server-side error.

A status code alone does not explain the full cause; interpret it alongside the request and server context.

## Day 7–8 practice record
The learning log records study of the OSI model, IP/MAC, ports, TCP/UDP, routing, DNS, HTTP, nslookup/dig/curl, and common HTTP status codes. Detailed personal notes were kept in Notion; this file is the concise public portfolio summary.
