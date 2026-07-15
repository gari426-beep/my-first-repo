print("=== Log Analyzer ===")

filename = input("Enter log file name: ")

try:
    with open(filename, "r") as file:
        failed = 0
        successful = 0

        for line in file:
            if "Failed" in line:
                failed += 1
            elif "Success" in line:
                successful += 1

    print("\nAnalysis Complete")
    print(f"Failed Logins : {failed}")
    print(f"Successful Logins : {successful}")

except FileNotFoundError:
    print("Log file not found!")