import psutil
import os
import time
import logging
from datetime import datetime

# Log File Setup
LOG_FILE = "/var/log/rtos_security.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

# Function to Monitor Failed Login Attempts (Linux Only)
def monitor_failed_logins():
    auth_log = "/var/log/auth.log"
    if os.path.exists(auth_log):
        with open(auth_log, "r") as f:
            lines = f.readlines()
            for line in lines[-10:]:  # Read last 10 lines for new attempts
                if "Failed password" in line:
                    logging.info("[FAILED LOGIN] " + line.strip())

# Function to Monitor Running Processes
def monitor_processes():
    for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
        logging.info(f"[PROCESS] PID: {proc.info['pid']}, Name: {proc.info['name']}, User: {proc.info['username']}")

# Function to Monitor Network Connections
def monitor_network():
    for conn in psutil.net_connections(kind='inet'):
        logging.info(f"[NETWORK] PID: {conn.pid}, Status: {conn.status}, IP: {conn.laddr}")

# Main Function to Continuously Monitor
def monitor_system():
    logging.info("=== RTOS Security Logger Started ===")
    while True:
        monitor_failed_logins()
        monitor_processes()
        monitor_network()
        time.sleep(10)  # Log every 10 seconds

if __name__ == "__main__":
    monitor_system()
