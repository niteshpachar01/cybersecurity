import hashlib
import secrets

password = "mango123"

# Generate two different random salts
salt1 = secrets.token_hex(16)
salt2 = secrets.token_hex(16)

def salted_hash(password, salt):
    data = (salt + password).encode("utf-8")
    return hashlib.sha256(data).hexdigest()

hash1 = salted_hash(password, salt1)
hash2 = salted_hash(password, salt2)

print("Password:", password)
print("\nSalt 1:", salt1)
print("Hash 1:", hash1)

print("\nSalt 2:", salt2)
print("Hash 2:", hash2)

print("\nSame password?", password == password)
print("Same hash?", hash1 == hash2)
