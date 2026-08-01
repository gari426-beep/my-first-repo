print("=== Log Analyzer ===")

filename = input("Enter log file name: ")

try:
    with open(filename, "r") as file:
        failed = 0
        successful = 0
        failed_users = {}

        for line in file:
            if "Failed" in line:
                failed += 1

                parts = line.split()
                username = parts[-1]

                failed_users[username] = failed_users.get(username, 0) + 1

            elif "Success" in line:
                successful += 1

        print("\nAnalysis Complete")
        print(f"Failed Logins : {failed}")
        print(f"Successful Logins : {successful}")

        print("\nFailed Login Attempts by User:")

        for username, count in failed_users.items():
            print(f"{username} : {count}")

except FileNotFoundError:
    print("Log file not found.")