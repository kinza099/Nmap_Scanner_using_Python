# Nmap Automation Tool

## Description
This is a Python-based Nmap automation tool that allows users to scan a given IP address using different scanning techniques. It leverages the `nmap` library to perform SYN ACK, UDP, and comprehensive scans.

## Features
- Perform **SYN ACK Scan** to detect open TCP ports.
- Perform **UDP Scan** to detect open UDP ports.
- Perform **Comprehensive Scan** to get detailed information including OS detection and service versions.
- Displays scan results in a structured manner.

## Requirements
Ensure you have the following dependencies installed:
- Python 3
- `nmap` (Python library)
- `pyfiglet`

### Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/kinza099/Nmap-Automation-Tool.git
   cd Nmap-Automation-Tool
   ```
2. Install dependencies:
   ```sh
   pip install python-nmap pyfiglet
   ```

## Usage
Run the script with:
```sh
python3 nmap_scanner.py
```
Follow the on-screen instructions to select the scan type and analyze the results.

## Screenshot
![image](https://github.com/user-attachments/assets/cc551bff-cf15-491a-bf63-685942023282)
![image](https://github.com/user-attachments/assets/d61fd2c4-0b8f-41f7-9f0c-255c325e47a8)



## Disclaimer
This tool is intended for educational and authorized security testing purposes only. Unauthorized scanning of networks is illegal.

## License
This project is open-source and licensed under the MIT License.

