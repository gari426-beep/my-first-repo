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
    print("\nSHA-256 Hash:")
    print(file_hash)
else:
    print("File not found!")