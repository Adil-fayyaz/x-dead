# 🔴 X DEAD v1.0 - Network Control System

<div align="center">

**Created by: Infinity X Team White Devel**  
**Ethical Hackers & Security Experts**

[![Version](https://img.shields.io/badge/version-1.0-red.svg)](https://github.com/Adil-fayyaz/x-dead)
[![Platform](https://img.shields.io/badge/platform-Kali%20Linux%20%7C%20Termux-blue.svg)](https://github.com/Adil-fayyaz/x-dead)
[![Python](https://img.shields.io/badge/python-3.6+-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

</div>

---

## 📖 Description

**X DEAD** is a powerful network discovery and control tool designed for **Kali Linux** and **Termux**. It provides comprehensive network scanning, device enumeration, and advanced network analysis capabilities.

Perfect for:
- 🎓 **Students** learning cybersecurity
- 🔒 **Security professionals** testing their networks
- 🏠 **Home users** discovering devices on their network
- 🏢 **Network administrators** mapping their infrastructure

### ⚡ Key Features

- ✅ **Network Discovery**: Automatic network detection and mapping
- ✅ **Device Enumeration**: Complete device discovery with IP, MAC, hostname, and vendor information
- ✅ **Port Scanning**: Advanced port scanning with service detection
- ✅ **Multi-Platform**: Works on Kali Linux and Termux (Android)
- ✅ **Interactive Interface**: Beautiful, color-coded CLI interface
- ✅ **Real-time Scanning**: Fast ARP and ping-based network scanning
- ✅ **Easy to Use**: Simple menu system - perfect for beginners

---

## 🚀 Quick Start

### 📱 On Termux (Android)

**Copy and paste this single command:**

```bash
pkg update && pkg upgrade -y && pkg install python3 nmap arp-scan -y && python3 x_dead.py
```

### 🐧 On Kali Linux

**Copy and paste this single command:**

```bash
sudo apt-get update && sudo apt-get install -y python3 python3-pip nmap arp-scan && sudo python3 x_dead.py
```

**That's it!** The tool will start automatically.

---

## 📋 Installation Guide

### For Beginners (Step-by-Step)

👉 **See [INSTALL.md](INSTALL.md) for detailed installation instructions**

The installation guide includes:
- 📝 Step-by-step instructions
- 🖼️ What to expect at each step
- ❓ Troubleshooting common problems
- ✅ Verification steps

### Quick Installation

#### Termux (Android)

1. Open Termux app
2. Run: `pkg update && pkg upgrade -y`
3. Run: `pkg install python3 nmap arp-scan -y`
4. Run: `python3 x_dead.py`

#### Kali Linux

1. Open terminal (Ctrl+Alt+T)
2. Run: `sudo apt-get update`
3. Run: `sudo apt-get install -y python3 python3-pip nmap arp-scan`
4. Run: `sudo python3 x_dead.py`

---

## 🎯 How to Use

### 1️⃣ Start the Tool

After installation, simply run:
```bash
python3 x_dead.py
# or on Kali Linux:
sudo python3 x_dead.py
```

### 2️⃣ Main Menu

You'll see a menu with these options:

```
1. Scan Network (Auto Discovery)    - Automatically scan your network
2. Deep Scan Device                 - Detailed analysis of a device
3. View Discovered Devices          - View all found devices
4. Network Information               - Show network details
5. Advanced Options                  - Advanced features (v2.0)
6. Exit                              - Exit the program
```

### 3️⃣ Scan Your Network

1. Select option **1** from the menu
2. The tool will automatically detect your network
3. If it can't, you'll be asked to enter:
   - **Network**: Example `192.168.1.0/24` (replace with your network)
   - **Interface**: Example `wlan0` or `eth0`

### 4️⃣ View Discovered Devices

After scanning, you'll see all connected devices with:
- 📍 IP Address
- 🔢 MAC Address
- 🏷️ Hostname
- 🏭 Vendor/Manufacturer

### 5️⃣ Deep Scan

1. Select option **2** from the menu
2. Choose the device number to analyze
3. The tool will perform a deep port scan

---

## 📋 Requirements

### Software Dependencies:
- **Python 3.6+** (usually pre-installed on Kali/Termux)
- **nmap** (port scanner)
- **arp-scan** (ARP scanning)

### Permissions:
- **Root/Sudo** (recommended for full functionality)
- **Network permissions** (for scanning)

---

## 🔧 Troubleshooting

### ❌ Problem: "Command not found: nmap"

**Solution:**
```bash
# On Termux:
pkg install nmap -y

# On Kali Linux:
sudo apt-get install nmap -y
```

### ❌ Problem: "Permission denied"

**Solution:**
```bash
# On Kali Linux, use sudo:
sudo python3 x_dead.py

# On Termux, if needed:
su
python3 x_dead.py
```

### ❌ Problem: "No devices found"

**Solutions:**
1. Make sure you're connected to WiFi
2. Check your network interface:
   ```bash
   ip addr show
   ```
3. Enter the network manually when prompted

### ❌ Problem: "Network not detected"

**Solution:**
Enter manually:
- **Network**: `192.168.1.0/24` (replace `192.168.1` with your network)
- **Interface**: `wlan0` (WiFi) or `eth0` (Ethernet)

To find your network:
```bash
ip route show
```

---

## 📸 Screenshots

```
██████╗     ██████╗ ███████╗ █████╗ ██████╗ 
╚════██╗    ██╔══██╗██╔════╝██╔══██╗██╔══██╗
 █████╔╝    ██║  ██║█████╗  ███████║██║  ██║
██╔═══╝     ██║  ██║██╔══╝  ██╔══██║██║  ██║
███████╗    ██████╔╝███████╗██║  ██║██████╔╝
╚══════╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ 

     X DEAD v1.0 - Network Control System
    Created by: Infinity X Team White Devel
        Ethical Hackers & Security Experts
```

---

## 🔮 Coming Soon (v2.0)

- 🔍 Network Traffic Analysis
- 🛡️ Vulnerability Assessment
- ⚔️ Exploit Framework Integration
- 🤖 Automated Attack Vectors
- 📊 Advanced Reporting
- 🌐 Web Interface

---

## ⚠️ Legal Disclaimer

**IMPORTANT:** This tool is for **EDUCATIONAL PURPOSES and AUTHORIZED TESTING ONLY**.

- ✅ Use only on networks you own
- ✅ Use only with explicit authorization
- ❌ Do NOT use on networks without permission
- ❌ Unauthorized access is illegal

The developers are **NOT responsible** for misuse of this tool.

---

## 👥 Credits

**Infinity X Team White Devel**  
*Ethical Hackers & Security Experts*

---

## 📝 License

This project is released under the MIT License. See [LICENSE](LICENSE) file for details.

**Use responsibly and ethically.**

---

## 🆘 Support

If you have problems or questions:
1. Check the "Troubleshooting" section above
2. Read [INSTALL.md](INSTALL.md) for detailed installation help
3. Verify you've installed all dependencies
4. Make sure you have the necessary permissions

---

## 🌟 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 📝 Improve documentation
- 🔧 Submit pull requests

---

<div align="center">

**⭐ If this tool was helpful, please give it a star on GitHub! ⭐**

Made with ❤️ by **Infinity X Team White Devel**

[🔗 View on GitHub](https://github.com/Adil-fayyaz/x-dead)

</div>
