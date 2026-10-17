# Hash Cracker Demo

## Overview
A beginner-friendly Python project demonstrating dictionary-based hash matching using test passwords and common hashing algorithms.

## Features
- Interactive hash algorithm selection
- Supports MD5, SHA-1, and SHA-256 for educational comparison
- Generates a sample hash for testing
- Matches hashes against a small, predefined demo wordlist
- Demonstrates how different salts produce different hashes for the same password

## Files
- `hash_cracker.py` — interactive dictionary-matching demonstration
- `salt_demo.py` — demonstrates salted hashing

## How to Run
Requires Python 3.

```bash
python hash_cracker.py
python salt_demo.py
```

## Learning Outcomes
- Understand hash matching and dictionary-based guessing
- Compare common hash algorithms
- Understand the purpose of salts in password storage

## Security Note
Use this project only for authorized educational testing. MD5, SHA-1, and plain SHA-256 are not recommended for password storage. Real applications should use Argon2id, scrypt, or bcrypt with appropriate parameters.

The salted SHA-256 example is for learning only; production password storage should use a dedicated password-hashing algorithm.

## Status
Completed as a beginner cybersecurity learning project.
