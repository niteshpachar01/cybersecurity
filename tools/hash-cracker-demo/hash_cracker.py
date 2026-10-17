import hashlib

def generate_hash(text, algorithm):
    encoded = text.encode("utf-8")

    if algorithm == "sha256":
        return hashlib.sha256(encoded).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(encoded).hexdigest()
    elif algorithm == "md5":
        return hashlib.md5(encoded).hexdigest()
    else:
        return None


print("=== Hash Cracker Demo ===")
print("For authorized learning and test hashes only.\n")

print("Choose hash algorithm:")
print("1. SHA-256")
print("2. SHA-1")
print("3. MD5")

choice = input("Enter choice (1-3): ").strip()

algorithms = {
    "1": "sha256",
    "2": "sha1",
    "3": "md5"
}

algorithm = algorithms.get(choice)

if not algorithm:
    print("Invalid choice.")
    raise SystemExit

print("\nDemo wordlist:")
wordlist = [
    "hello123",
    "password",
    "mango123",
    "python123",
    "cyber123"
]

# Optional: generate a sample hash for the demo
demo_password = "mango123"
sample_hash = generate_hash(demo_password, algorithm)

print("Sample password for this demo: mango123")
print("Sample hash:", sample_hash)

target_hash = input(
    "\nPaste a hash to test (or press Enter to use sample): "
).strip().lower()

if not target_hash:
    target_hash = sample_hash

if len(target_hash) != len(sample_hash):
    print("Hash length does not match the selected algorithm.")
    raise SystemExit

print("\nSearching demo wordlist...")

found = False

for word in wordlist:
    candidate_hash = generate_hash(word, algorithm)

    if candidate_hash == target_hash:
        print("Match found:", word)
        found = True
        break

if not found:
    print("No match found in this demo wordlist.")
    print("This does not prove the original password is secure.")
