# RTOS Event Logger  

This project is a real-time monitoring tool designed to **track OS-level security events** on Kali Linux. It focuses on developing a **real-time security event logger** to enhance system security monitoring and **incident response**.  

### 🔍 **What It Logs?**  
✅ **Failed login attempts** 🚫🔑  
✅ **Running processes** 🖥️👀  
✅ **Active network connections** 🌍📡  

These logs are stored in **`/var/log/rtos_security.log`** for future analysis.  

![Project Overview](https://github.com/user-attachments/assets/4296111a-4fda-48c5-90dc-931fb75f8a61)  

---

## 📂 **Project Structure**  

```bash
 ├── 📄 rtos_security_logger.py    # Main security logger script
 ├── 📄 README.md                  # Project documentation
 ├── 📄 rtos_logger.service        # Script to run logger in background
 ├── 📄 logs.txt                   # Folder for storing logs
 ├── 📂 documentaion               # Documentation (flowcharts, report, etc.)
```

---

## ⚙️ **Features**  

🔹 **Real-time monitoring** of OS security logs  
🔹 **Automated logging of suspicious activity**  
🔹 **Runs as a systemd service for background execution**  
🔹 **Lightweight and optimized for Kali Linux**  

---

## 📥 **Installation**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/rai-1819/RTOS-event-logger.git
cd RTOS-event-logger
```


2️⃣ Install Dependencies
```bash
sudo apt update
sudo apt install python3 python3-pip
pip install psutil
```

3️⃣ Run the Logger
```bash
sudo python3 rtos_security_logger.py
```

🔥 Stay Safe, Stay Secure!
Contributions are welcome! Fork the repo and submit a PR! 💪<br>
🚀 Repo Link:https://github.com/rai-1819/RTOS-event-logger

📩 Contact<br>
📧 Email: rai1819.dox.com
🔗 GitHub: rai-1819

🔥 Made for Kali Linux – Stay Secure! 🔥
