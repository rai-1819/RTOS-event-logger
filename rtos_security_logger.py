import psutil
import os
import time
import logging
from datetime import datetime

# Configuration
LOG_FILE = "/var/log/rtos_security.log"
LOG_RETENTION_DAYS = 7  # Number of days to keep the log file

# Setup Logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

def delete_old_log():
    """Delete the log file if it's older than LOG_RETENTION_DAYS."""
    if os.path.exists(LOG_FILE):
        file_mod_time = os.path.getmtime(LOG_FILE)
        current_time = time.time()
        age_in_days = (current_time - file_mod_time) / (60 * 60 * 24)
        if age_in_days > LOG_RETENTION_DAYS:
            os.remove(LOG_FILE)
            print(f"[INFO] Old log file deleted: {LOG_FILE}")

def monitor_failed_logins():
    """Monitor and log failed login attempts."""
    auth_log = "/var/log/auth.log"
    if os.path.exists(auth_log):
        with open(auth_log, "r") as f:
            lines = f.readlines()
            for line in lines[-10:]:  # Check the last 10 lines
                if "Failed password" in line:
                    logging.info("[FAILED LOGIN] " + line.strip())

def monitor_processes():
    """Monitor and log running processes."""
    for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
        logging.info(f"[PROCESS] PID: {proc.info['pid']}, Name: {proc.info['name']}, User: {proc.info['username']}")

def monitor_network():
    """Monitor and log active network connections."""
    for conn in psutil.net_connections(kind='inet'):
        logging.info(f"[NETWORK] PID: {conn.pid}, Status: {conn.status}, IP: {conn.laddr}")

def monitor_system():
    """Main function to continuously monitor system events."""
    logging.info("=== RTOS Security Logger Started ===")
    last_delete_check = time.time()

    while True:
        monitor_failed_logins()
        monitor_processes()
        monitor_network()
        time.sleep(10)  # Sleep for 10 seconds

        # Check log file age once a day
        if time.time() - last_delete_check >= 86400:  # 86400 seconds = 1 day
            delete_old_log()
            last_delete_check = time.time()

if __name__ == "__main__":
    monitor_system()
