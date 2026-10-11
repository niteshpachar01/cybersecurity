# TryHackMe — Wireshark: Packet Operations

**Status in learning log:** Reported completed on Day 15.

## Learning summary
- Use Follow TCP Stream to inspect the contents and direction of a conversation when the protocol data is visible.
- Understand that Export Objects can extract supported objects from certain protocol dissections.
- Apply filters to focus on relevant packets before deeper inspection.
- Treat captured data as potentially sensitive.

## Important limitations
- Encrypted application payloads are not automatically readable just because a TCP stream is followed.
- Export Objects is available only for supported protocols and objects.
- Captures may contain credentials, cookies, personal data, internal hostnames, and other sensitive information.

## Safe workflow
1. Use a capture from your own lab or an approved exercise.
2. Filter to the relevant protocol or conversation.
3. Follow the stream and inspect only what is necessary.
4. Do not publish extracted files or packet captures until sensitive data has been reviewed and removed.

## Evidence note
The learning record says Follow TCP Stream and Export Objects were practiced. Detailed notes were kept in Notion; this audit did not independently verify the room-completion dashboard or recover a room-specific screenshot.
