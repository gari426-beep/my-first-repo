# Port Scanner

## Overview
This project is a Python-based Port Scanner that checks whether common TCP ports on a target IP address are open or closed. It helps demonstrate basic network scanning concepts used in cybersecurity.

## Features
- Scans common TCP ports
- Displays whether ports are open or closed
- Identifies common services running on each port
- Validates IP addresses before scanning
- Measures total scan time
- Beginner-friendly and easy to understand

## Technologies Used
- Python
- Socket Module
- Time Module

## Project Structure
```
port-scanner/
├── port_scanner.py
└── README.md
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/my-first-repo.git
   ```

2. Navigate to the project folder:
   ```bash
   cd port-scanner
   ```

3. Run the program:
   ```bash
   python port_scanner.py
   ```

## Example Output

```
========================================
        Simple Port Scanner
========================================

Enter IP address: 127.0.0.1

Scanning 127.0.0.1...

[OPEN ] Port 22    (ssh)
[CLOSED] Port 80    (http)
[OPEN ] Port 443   (https)

Scan completed.
Time taken: 2.15 seconds
```

## Learning Outcomes
Through this project, I learned:
- Python socket programming
- TCP/IP networking basics
- Port scanning concepts
- Exception handling using `try` and `except`
- Working with loops and lists
- Measuring execution time in Python

## Disclaimer
This project is intended for educational purposes only. Only scan systems that you own or have explicit permission to test.