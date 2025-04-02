# RTOS-event-logger
This project focuses on developing a real-time security event logger for Linux systems, designed to improve system security monitoring and incident response. It provides administrators with instant insights into security-related events, enabling proactive threat detection and response.



![Untitled Diagram drawio](https://github.com/user-attachments/assets/4296111a-4fda-48c5-90dc-931fb75f8a61)


Overview
The RTOS Security Event Logger is a real-time security monitoring tool designed to detect and log OS-level security events such as:
✔ Failed login attempts
✔ Running process monitoring
✔ Active network connections tracking

It helps in identifying vulnerabilities, making it useful for cybersecurity professionals and system admins.

Features
🔹 Monitors failed login attempts to detect brute-force attacks.
🔹 Logs all running processes (PID, Name, User).
🔹 Tracks active network connections (IP, Status, Port).
🔹 Stores logs persistently in /var/log/rtos_security.log.
🔹 Runs as a background service on Kali Linux.

Installation
Step 1: Clone Repository
bash
Copy
Edit
git clone https://github.com/your-username/RTOS-Security-Logger.git
cd RTOS-Security-Logger
Step 2: Install Dependencies
bash
Copy
Edit
sudo apt update
sudo apt install python3-pip
pip3 install psutil
Step 3: Run the Logger
bash
Copy
Edit
sudo python3 security_logger.py
📜 Usage
🔹 Running the Logger
Simply execute the script to start monitoring security events:

bash
Copy
Edit
sudo python3 security_logger.py
🔹 Viewing Logs
Logs are stored in:

bash
Copy
Edit
cat /var/log/rtos_security.log
🔹 Running as a Background Service (systemd)
1️⃣ Copy the service file:

bash
Copy
Edit
sudo cp rtos_logger.service /etc/systemd/system/
2️⃣ Enable and start the service:

bash
Copy
Edit
sudo systemctl enable rtos_logger.service
sudo systemctl start rtos_logger.service
3️⃣ Check service status:

bash
Copy
Edit
sudo systemctl status rtos_logger
🛠️ Technologies Used
✅ Python 3
✅ Psutil (Process & Network Monitoring)
✅ Systemd (Background Service Management)
✅ Logging Module (Persistent Log Storage)

📌 Project Flowchart
(Refer to the flowchart in the documentation or draw.io file.)

🚀 Future Improvements
📡 Real-time alerts via email for security breaches

🤖 AI-powered anomaly detection

📊 Web-based log dashboard for visualization

📝 License
This project is licensed under the MIT License – feel free to modify and use it.

🤝 Contributing
Feel free to fork, submit issues, or create pull requests! Let's make cybersecurity stronger together. 🔥

📩 Contact
📧 Email: your-email@example.com
🔗 GitHub: your-username

🔥 Made for Kali Linux – Stay Secure! 🔥
