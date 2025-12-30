#!/bin/bash
# X DEAD Installation Script
# Created by: Infinity X Team White Devel

echo "========================================="
echo "  X DEAD v1.0 - Installation Script"
echo "  Created by: Infinity X Team White Devel"
echo "========================================="
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo "[!] Please run as root (use sudo)"
    exit 1
fi

# Detect OS
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
else
    echo "[!] Cannot detect OS"
    exit 1
fi

echo "[*] Detected OS: $OS"
echo "[*] Installing dependencies..."

# Install based on OS
if [ "$OS" == "kali" ] || [ "$OS" == "debian" ] || [ "$OS" == "ubuntu" ]; then
    apt-get update
    apt-get install -y python3 python3-pip nmap arp-scan
elif [ "$OS" == "android" ] || command -v pkg &> /dev/null; then
    pkg update && pkg upgrade -y
    pkg install -y python3 nmap arp-scan
else
    echo "[!] Unsupported OS. Please install manually:"
    echo "    - Python 3"
    echo "    - nmap"
    echo "    - arp-scan"
fi

# Make script executable
chmod +x x_dead.py

echo ""
echo "[+] Installation complete!"
echo "[*] Run with: sudo python3 x_dead.py"
echo ""

