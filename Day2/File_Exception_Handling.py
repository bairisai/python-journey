file_name = "user_logs.txt"

try:
    print("Attempting to read log files!")
    with open(file_name, "r") as file:
        logs = file.read()
        print(f"Logs loaded successfully: {logs}")

except FileNotFoundError:
    print("File not found, Activating saftey net...")
    print("Creating new logs file...")

    with open(file_name, "w") as file:
        file.write("#The file is created using File handling program\n")
        logs = ""
print("program successfully completed without crashing...")