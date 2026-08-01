import hashlib

def calculate_hash(filename):
    sha256 = hashlib.sha256()

    try:
        with open(filename, "rb") as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        return None


print("=== File Integrity Checker ===")

filename = input("Enter the file name or path: ")

file_hash = calculate_hash(filename)

if file_hash:
    print("\nCurrent SHA-256 Hash:")
    print(file_hash)

    expected_hash = input("\nEnter the expected SHA-256 hash: ").strip().lower()

    if file_hash == expected_hash:
        print("\n✅ File integrity verified!")
        print("The file has not changed.")
    else:
        print("\n⚠️ File integrity check failed!")
        print("The file may have been modified.")

else:
    print("File not found!")