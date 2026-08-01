import hashlib

print("=== Hash Generator & Verifier ===")

text = input("Enter text: ")

md5_hash = hashlib.md5(text.encode()).hexdigest()
sha1_hash = hashlib.sha1(text.encode()).hexdigest()
sha256_hash = hashlib.sha256(text.encode()).hexdigest()

print("\nGenerated Hashes")
print("---------------------------")
print("MD5     :", md5_hash)
print("SHA-1   :", sha1_hash)
print("SHA-256 :", sha256_hash)

print("\nHash Verification")
user_hash = input("Enter a SHA-256 hash to verify: ").strip().lower()

if user_hash == sha256_hash:
    print("✅ Hash matches!")
else:
    print("❌ Hash does not match.")