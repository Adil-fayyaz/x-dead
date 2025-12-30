# 📥 X DEAD Installation Guide - For Beginners

## 🎯 Complete Step-by-Step Installation

This guide will help you install X DEAD even if you've never used a terminal before!

---

## 📱 INSTALLATION ON TERMUX (Android)

### ⚡ Quick Method (Copy & Paste)

Open Termux and paste this command:

```bash
pkg update && pkg upgrade -y && pkg install python3 nmap arp-scan -y && python3 x_dead.py
```

**Done!** The tool will start automatically.

---

### 📝 Detailed Method (Step-by-Step)

#### Step 1: Open Termux
- Open the **Termux** app on your Android phone
- You'll see a black screen with text - this is normal!

#### Step 2: Update Termux
Copy and paste this command, then press **Enter**:
```bash
pkg update && pkg upgrade -y
```
**What happens:** Termux downloads updates (this takes 1-2 minutes)
**Wait for:** The command to finish (you'll see `$` again)

#### Step 3: Install Python
Copy and paste:
```bash
pkg install python3 -y
```
**What happens:** Python 3 is installed
**Wait for:** Installation to complete

#### Step 4: Install nmap
Copy and paste:
```bash
pkg install nmap -y
```
**What happens:** nmap (network scanner) is installed
**Wait for:** Installation to complete

#### Step 5: Install arp-scan
Copy and paste:
```bash
pkg install arp-scan -y
```
**What happens:** arp-scan (network discovery tool) is installed
**Wait for:** Installation to complete

#### Step 6: Go to the Tool Folder
If you downloaded `x_dead.py` to Downloads folder:
```bash
cd ~/storage/downloads
```

If it's in the home folder:
```bash
cd ~
```

#### Step 7: Start X DEAD
```bash
python3 x_dead.py
```

**🎉 Done! The tool is running!**

---

## 🐧 INSTALLATION ON KALI LINUX

### ⚡ Quick Method (Copy & Paste)

Open terminal and paste this command:

```bash
sudo apt-get update && sudo apt-get install -y python3 python3-pip nmap arp-scan && sudo python3 x_dead.py
```

**Done!** The tool will start automatically.

---

### 📝 Detailed Method (Step-by-Step)

#### Step 1: Open Terminal
- Press `Ctrl + Alt + T` OR
- Search for "Terminal" in the menu and click it
- You'll see a window with text - this is the terminal!

#### Step 2: Update the System
Copy and paste:
```bash
sudo apt-get update
```
**What happens:** System downloads package lists
**You'll be asked:** Your password (type it and press Enter - you won't see the password as you type, this is normal!)
**Wait for:** Update to finish (1-2 minutes)

#### Step 3: Install Python
Copy and paste:
```bash
sudo apt-get install -y python3 python3-pip
```
**What happens:** Python 3 and pip are installed
**You'll be asked:** Password (if needed)
**Wait for:** Installation to complete

#### Step 4: Install nmap
Copy and paste:
```bash
sudo apt-get install -y nmap
```
**What happens:** nmap (network scanner) is installed
**Wait for:** Installation to complete

#### Step 5: Install arp-scan
Copy and paste:
```bash
sudo apt-get install -y arp-scan
```
**What happens:** arp-scan (network discovery tool) is installed
**Wait for:** Installation to complete

#### Step 6: Go to the Tool Folder
If you saved `x_dead.py` on Desktop:
```bash
cd ~/Desktop/kali\ linux\ tool
```

Or if it's in another folder, go there:
```bash
cd /path/to/your/folder
```

#### Step 7: Make Executable (Optional)
```bash
chmod +x x_dead.py
```

#### Step 8: Start X DEAD
```bash
sudo python3 x_dead.py
```

**🎉 Done! The tool is running!**

---

## ❓ Frequently Asked Questions

### Q: What does "sudo" mean?
**A:** `sudo` means "Super User Do" - it gives you administrator permissions. On Kali Linux it's needed for some features.

### Q: Why do I need to enter my password?
**A:** When you use `sudo`, the system asks for your password for security. This is normal!

### Q: What if I see "Command not found"?
**A:** This means the program isn't installed. Follow the installation steps for dependencies.

### Q: Can I use the tool without root/sudo?
**A:** Yes, but some features might not work. Try without sudo first, if it doesn't work use sudo.

### Q: How do I find my network?
**A:** Run this command:
```bash
ip route show
```
Look for a line starting with an IP address like `192.168.x.x` or `10.0.x.x`

### Q: What if the installation is slow?
**A:** This is normal! Installation can take 2-5 minutes depending on your internet speed.

### Q: Can I close the terminal after starting the tool?
**A:** No, keep the terminal open while using the tool. Close it when you're done.

---

## 🆘 Common Problems

### ❌ "Permission denied"

**Solution:** Use `sudo` before the command:
```bash
sudo python3 x_dead.py
```

### ❌ "nmap: command not found"

**Solution:** Install nmap:
- Termux: `pkg install nmap -y`
- Kali: `sudo apt-get install nmap -y`

### ❌ "No devices found"

**Solution:** 
1. Make sure you're connected to WiFi
2. Try entering the network manually when prompted

### ❌ "Network not detected"

**Solution:** Enter manually:
- Network: `192.168.1.0/24` (replace `192.168.1` with your network)
- Interface: `wlan0` (WiFi) or `eth0` (Ethernet)

### ❌ "Python not found"

**Solution:**
- Termux: `pkg install python3 -y`
- Kali: `sudo apt-get install python3 -y`

---

## ✅ Verify Installation

After installation, verify everything works:

```bash
# Check Python
python3 --version
# Should show: Python 3.x.x

# Check nmap
nmap --version
# Should show: Nmap version x.x.x

# Check arp-scan
arp-scan --version
# Should show: arp-scan version x.x.x
```

If all commands work, you're ready! 🚀

---

## 📞 Need More Help?

1. Re-read this guide carefully
2. Check you followed all steps
3. Make sure you have an active internet connection
4. Verify all dependencies are installed

---

## 🎯 Next Steps

After installation:
1. Run `python3 x_dead.py`
2. Select option **1** to scan your network
3. Explore the menu options
4. Have fun discovering devices on your network!

---

**Good luck with your installation! 🎉**

*Created by: Infinity X Team White Devel*
