# RTOS-event-logger
This project is a real-time monitoring tool designed to track OS-level security events on Kali Linux and focuses on developing a real-time security event logger for Linux systems, designed to improve system security monitoring and incident response. It provides administrators with instant insights into security-related events, enabling proactive threat detection and response ,it logs:
✅ Failed login attempts
✅ Running processes
✅ Active network connections

These logs are stored in /var/log/rtos_security.log for future analysis.



![Untitled Diagram drawio](https://github.com/user-attachments/assets/4296111a-4fda-48c5-90dc-931fb75f8a61)


 Project Structure
 ├── 📄 rtos_security_logger.py    # Main security logger script
 ├── 📄 README.md                  # Project documentation
 ├── 📄 rtos_logger.service        # Script to run logger in background
 ├── 📂 logs.txt                   # Folder for storing logs
 ├── 📂 documentaion               # Documentation (flowcharts, report, etc.)

⚙️ Features
🔹 Real-time monitoring of OS security logs
🔹 Automated logging of suspicious activity
🔹 Runs as a systemd service for background execution
🔹 Lightweight and optimized for Kali Linux

📥 Installation
1️⃣ Clone the Repository
git clone https://github.com/rai-1819/RTOS-event-logger.git
cd RTOS-event-logger

2️⃣ Install Dependencies
sudo apt update
sudo apt install python3 python3-pip
pip install psutil

3️⃣ Run the Logger
sudo python3 rtos_security_logger.py

🔥 Stay Safe, Stay Secure!
Contributions are welcome! Fork the repo and submit a PR! 💪
🚀 Repo Link:https://github.com/rai-1819/RTOS-event-logger

📩 Contact
📧 Email: rai1819.dox.com
🔗 GitHub: rai-1819

🔥 Made for Kali Linux – Stay Secure! 🔥
