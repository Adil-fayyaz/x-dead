#!/data/data/com.termux/files/usr/bin/bash
# X DEAD - Quick Start Script for Termux
# Created by: Infinity X Team White Devel

echo "========================================="
echo "  X DEAD v1.0 - Termux Quick Start"
echo "  Created by: Infinity X Team White Devel"
echo "========================================="
echo ""

# Colors
RED='\033[0;91m'
CYAN='\033[0;96m'
GREEN='\033[0;92m'
YELLOW='\033[0;93m'
RESET='\033[0m'

echo -e "${CYAN}[*] Checking dependencies...${RESET}"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}[*] Installing Python3...${RESET}"
    pkg install python3 -y
fi

# Check nmap
if ! command -v nmap &> /dev/null; then
    echo -e "${YELLOW}[*] Installing nmap...${RESET}"
    pkg install nmap -y
fi

# Check arp-scan
if ! command -v arp-scan &> /dev/null; then
    echo -e "${YELLOW}[*] Installing arp-scan...${RESET}"
    pkg install arp-scan -y
fi

echo -e "${GREEN}[+] Dependencies installed!${RESET}"
echo ""
echo -e "${CYAN}[*] Starting X DEAD...${RESET}"
echo ""

# Check if x_dead.py exists
if [ -f "x_dead.py" ]; then
    python3 x_dead.py
else
    echo -e "${RED}[!] Error: x_dead.py not found!${RESET}"
    echo -e "${YELLOW}[*] Make sure you're in the correct directory${RESET}"
    echo -e "${CYAN}[*] Current directory: $(pwd)${RESET}"
fi

