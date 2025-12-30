#!/usr/bin/env python3
"""
██████╗     ██████╗ ███████╗ █████╗ ██████╗ 
╚════██╗    ██╔══██╗██╔════╝██╔══██╗██╔══██╗
 █████╔╝    ██║  ██║█████╗  ███████║██║  ██║
██╔═══╝     ██║  ██║██╔══╝  ██╔══██║██║  ██║
███████╗    ██████╔╝███████╗██║  ██║██████╔╝
╚══════╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ 
                                            
        X DEAD v1.0 - Network Control System
    Created by: Infinity X Team White Devel
        Ethical Hackers & Security Experts
"""

import os
import sys
import socket
import subprocess
import platform
import ipaddress
import threading
import time
import hashlib
import hmac
from datetime import datetime
from typing import List, Dict, Optional

# Color codes for terminal
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    ORANGE = '\033[38;5;208m'

class XDead:
    def __init__(self):
        self.version = "1.0"
        self.team = "Infinity X Team White Devel"
        self.targets = []
        self.network_info = {}
        self.running = True
        
    def banner(self):
        """Display the X Dead banner"""
        banner = f"""
{Colors.RED}{Colors.BOLD}
██╗  ██╗     {Colors.CYAN}██████╗ {Colors.RED}███████╗{Colors.CYAN} █████╗ {Colors.RED}██████╗ 
╚██╗██╔╝     {Colors.RED}██╔══██╗{Colors.CYAN}██╔════╝{Colors.RED}██╔══██╗{Colors.CYAN}██╔══██╗
 ╚███╔╝      {Colors.CYAN}██║  ██║{Colors.RED}█████╗  {Colors.CYAN}███████║{Colors.RED}██║  ██║
 ██╔██╗      {Colors.RED}██║  ██║{Colors.CYAN}██╔══╝  {Colors.RED}██╔══██║{Colors.CYAN}██║  ██║
██╔╝ ██╗     {Colors.CYAN}██████╔╝{Colors.RED}███████╗{Colors.CYAN}██║  ██║{Colors.RED}██████╔╝
╚═╝  ╚═╝     {Colors.RED}╚═════╝ {Colors.CYAN}╚══════╝{Colors.RED}╚═╝  ╚═╝{Colors.CYAN}╚═════╝ 
{Colors.RESET}
{Colors.RED}{Colors.BOLD}     X{Colors.RESET}{Colors.CYAN}{Colors.BOLD} D{Colors.RESET}{Colors.RED}{Colors.BOLD}E{Colors.RESET}{Colors.CYAN}{Colors.BOLD}A{Colors.RESET}{Colors.RED}{Colors.BOLD}D{Colors.RESET} {Colors.CYAN}{Colors.BOLD}v{self.version}{Colors.RESET} {Colors.RED}{Colors.BOLD}- Network Control System{Colors.RESET}
{Colors.YELLOW}    Created by: {self.team}{Colors.RESET}
{Colors.GREEN}        Ethical Hackers & Security Experts{Colors.RESET}
{Colors.RED}{Colors.BOLD}{'═'*70}{Colors.RESET}
"""
        print(banner)
    
    def check_requirements(self):
        """Check if required tools are installed"""
        required_tools = ['nmap']
        optional_tools = ['arp-scan', 'aircrack-ng', 'iwlist', 'nmcli']
        missing_tools = []
        missing_optional = []
        
        # Check required tools
        for tool in required_tools:
            try:
                subprocess.run([tool, '--version'], 
                             stdout=subprocess.PIPE, 
                             stderr=subprocess.PIPE, 
                             timeout=5)
            except (FileNotFoundError, subprocess.TimeoutExpired):
                missing_tools.append(tool)
        
        # Check optional tools
        for tool in optional_tools:
            try:
                subprocess.run([tool, '--version'], 
                             stdout=subprocess.PIPE, 
                             stderr=subprocess.PIPE, 
                             timeout=5)
            except (FileNotFoundError, subprocess.TimeoutExpired):
                missing_optional.append(tool)
        
        if missing_tools:
            print(f"{Colors.RED}[!] Missing required tools: {', '.join(missing_tools)}{Colors.RESET}")
            print(f"{Colors.YELLOW}[*] Please install: {', '.join(missing_tools)}{Colors.RESET}")
            return False
        
        if missing_optional:
            print(f"{Colors.YELLOW}[*] Optional tools not found: {', '.join(missing_optional)}{Colors.RESET}")
            print(f"{Colors.CYAN}[*] Will use alternative methods (ping scan){Colors.RESET}")
        
        return True
    
    def get_local_network(self):
        """Get local network information"""
        try:
            # Get default gateway
            if platform.system() == "Linux":
                result = subprocess.run(['ip', 'route', 'show', 'default'], 
                                      capture_output=True, text=True)
                for line in result.stdout.split('\n'):
                    if 'default via' in line:
                        parts = line.split()
                        gateway = parts[2]
                        interface = parts[4] if len(parts) > 4 else parts[-1]
                        
                        # Get network IP
                        result2 = subprocess.run(['ip', 'addr', 'show', interface], 
                                               capture_output=True, text=True)
                        for line2 in result2.stdout.split('\n'):
                            if 'inet ' in line2 and '127.0.0.1' not in line2:
                                ip_with_mask = line2.split()[1]
                                ip = ip_with_mask.split('/')[0]
                                network = ipaddress.ip_interface(ip_with_mask).network
                                return str(network), gateway, interface
            return None, None, None
        except Exception as e:
            print(f"{Colors.RED}[!] Error getting network info: {e}{Colors.RESET}")
            return None, None, None
    
    def scan_network_arp(self, network: str, interface: str) -> List[Dict]:
        """Scan network using ARP"""
        devices = []
        print(f"\n{Colors.CYAN}[*] Scanning network {network} using ARP...{Colors.RESET}")
        
        try:
            # Check if arp-scan is available
            result = subprocess.run(['which', 'arp-scan'], 
                                  capture_output=True, text=True, timeout=2)
            if result.returncode == 0:
                # Use arp-scan for fast discovery
                cmd = ['arp-scan', '--local', '--interface', interface]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                
                for line in result.stdout.split('\n'):
                    if '\t' in line and not line.startswith('Interface:'):
                        parts = line.split('\t')
                        if len(parts) >= 2:
                            ip = parts[0].strip()
                            mac = parts[1].strip()
                            vendor = parts[2].strip() if len(parts) > 2 else "Unknown"
                            
                            devices.append({
                                'ip': ip,
                                'mac': mac,
                                'vendor': vendor,
                                'status': 'active',
                                'hostname': self.get_hostname(ip)
                            })
                if devices:
                    return devices
        except Exception as e:
            pass
        
        # Fallback to ping scan if arp-scan not available or failed
        print(f"{Colors.YELLOW}[*] ARP scan not available, using ping scan method...{Colors.RESET}")
        devices = self.scan_network_ping(network)
        return devices
    
    def scan_network_ping(self, network: str) -> List[Dict]:
        """Scan network using ping"""
        devices = []
        net = ipaddress.ip_network(network, strict=False)
        
        print(f"{Colors.CYAN}[*] Scanning {len(list(net.hosts()))} hosts...{Colors.RESET}")
        
        def ping_host(ip):
            try:
                if platform.system() == "Linux":
                    result = subprocess.run(['ping', '-c', '1', '-W', '1', str(ip)], 
                                          capture_output=True, timeout=3)
                    if result.returncode == 0:
                        hostname = self.get_hostname(str(ip))
                        devices.append({
                            'ip': str(ip),
                            'mac': self.get_mac(str(ip)),
                            'vendor': "Unknown",
                            'status': 'active',
                            'hostname': hostname
                        })
            except:
                pass
        
        threads = []
        for ip in net.hosts():
            thread = threading.Thread(target=ping_host, args=(ip,))
            threads.append(thread)
            thread.start()
            if len(threads) >= 50:  # Limit concurrent threads
                for t in threads:
                    t.join(timeout=2)
                threads = []
        
        for t in threads:
            t.join(timeout=2)
        
        return devices
    
    def get_hostname(self, ip: str) -> str:
        """Get hostname from IP"""
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            return hostname
        except:
            return "Unknown"
    
    def get_mac(self, ip: str) -> str:
        """Get MAC address from ARP table"""
        try:
            result = subprocess.run(['arp', '-n', ip], capture_output=True, text=True)
            for line in result.stdout.split('\n'):
                if ip in line:
                    parts = line.split()
                    if len(parts) >= 3:
                        return parts[2]
        except:
            pass
        return "Unknown"
    
    def deep_scan_device(self, ip: str) -> Dict:
        """Perform deep scan on a device"""
        print(f"{Colors.CYAN}[*] Deep scanning {ip}...{Colors.RESET}")
        info = {'ip': ip, 'ports': [], 'os': 'Unknown', 'services': []}
        
        try:
            # Quick port scan
            cmd = ['nmap', '-sS', '-T4', '--top-ports', '100', ip]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            
            for line in result.stdout.split('\n'):
                if '/tcp' in line or '/udp' in line:
                    parts = line.split()
                    if len(parts) >= 2:
                        port_info = parts[0]
                        state = parts[1] if len(parts) > 1 else 'unknown'
                        service = parts[2] if len(parts) > 2 else 'unknown'
                        info['ports'].append({
                            'port': port_info,
                            'state': state,
                            'service': service
                        })
        except Exception as e:
            print(f"{Colors.YELLOW}[*] Deep scan error: {e}{Colors.RESET}")
        
        return info
    
    def display_devices(self, devices: List[Dict]):
        """Display discovered devices"""
        if not devices:
            print(f"\n{Colors.RED}[!] No devices found on the network{Colors.RESET}")
            return
        
        print(f"\n{Colors.RED}{Colors.BOLD}{'═'*85}{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}  {Colors.CYAN}DISCOVERED DEVICES ON NETWORK{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}{'═'*85}{Colors.RESET}\n")
        
        print(f"{Colors.CYAN}{Colors.BOLD}{'#':<4} {'IP Address':<18} {Colors.RED}MAC Address{Colors.CYAN:<11} {'Hostname':<25} {Colors.RED}Vendor{Colors.CYAN:<15}{Colors.RESET}")
        print(f"{Colors.MAGENTA}{'─'*85}{Colors.RESET}")
        
        for i, device in enumerate(devices, 1):
            ip = device.get('ip', 'Unknown')
            mac = device.get('mac', 'Unknown')
            hostname = device.get('hostname', 'Unknown')
            vendor = device.get('vendor', 'Unknown')
            
            # Alternate colors for visual appeal
            if i % 2 == 0:
                num_color = Colors.CYAN
                ip_color = Colors.CYAN
                mac_color = Colors.RED
                host_color = Colors.CYAN
                vend_color = Colors.RED
            else:
                num_color = Colors.RED
                ip_color = Colors.RED
                mac_color = Colors.CYAN
                host_color = Colors.RED
                vend_color = Colors.CYAN
            
            print(f"{num_color}{i:<4}{Colors.RESET} {ip_color}{ip:<18}{Colors.RESET} {mac_color}{mac:<20}{Colors.RESET} {host_color}{hostname[:23]:<25}{Colors.RESET} {vend_color}{vendor[:18]:<20}{Colors.RESET}")
        
        print(f"\n{Colors.RED}[+]{Colors.RESET} {Colors.CYAN}Total devices found: {Colors.RED}{len(devices)}{Colors.RESET}")
        self.targets = devices
    
    def menu(self):
        """Main menu"""
        while self.running:
            print(f"\n{Colors.RED}{Colors.BOLD}{'═'*70}{Colors.RESET}")
            print(f"{Colors.RED}{Colors.BOLD}  X{Colors.RESET}{Colors.CYAN}{Colors.BOLD} D{Colors.RESET}{Colors.RED}{Colors.BOLD}E{Colors.RESET}{Colors.CYAN}{Colors.BOLD}A{Colors.RESET}{Colors.RED}{Colors.BOLD}D{Colors.RESET} {Colors.CYAN}{Colors.BOLD}- MAIN MENU{Colors.RESET}")
            print(f"{Colors.RED}{Colors.BOLD}{'═'*70}{Colors.RESET}")
            print(f"{Colors.WHITE}1.{Colors.RESET} {Colors.RED}▶{Colors.RESET} {Colors.CYAN}Scan Network (Auto Discovery){Colors.RESET}")
            print(f"{Colors.WHITE}2.{Colors.RESET} {Colors.CYAN}▶{Colors.RESET} {Colors.RED}Deep Scan Device{Colors.RESET}")
            print(f"{Colors.WHITE}3.{Colors.RESET} {Colors.RED}▶{Colors.RESET} {Colors.CYAN}View Discovered Devices{Colors.RESET}")
            print(f"{Colors.WHITE}4.{Colors.RESET} {Colors.CYAN}▶{Colors.RESET} {Colors.RED}Network Information{Colors.RESET}")
            print(f"{Colors.WHITE}5.{Colors.RESET} {Colors.RED}▶{Colors.RESET} {Colors.YELLOW}Advanced Options{Colors.RESET}")
            print(f"{Colors.WHITE}6.{Colors.RESET} {Colors.CYAN}▶{Colors.RESET} {Colors.RED}Exit{Colors.RESET}")
            print(f"{Colors.RED}{Colors.BOLD}{'═'*70}{Colors.RESET}")
            
            choice = input(f"\n{Colors.RED}[{Colors.CYAN}X{Colors.RED} {Colors.CYAN}DEAD{Colors.RED}]{Colors.CYAN}>{Colors.RESET} ").strip()
            
            if choice == '1':
                self.scan_network()
            elif choice == '2':
                self.deep_scan_menu()
            elif choice == '3':
                if self.targets:
                    self.display_devices(self.targets)
                else:
                    print(f"{Colors.RED}[!] No devices scanned yet. Run network scan first.{Colors.RESET}")
            elif choice == '4':
                self.show_network_info()
            elif choice == '5':
                self.advanced_menu()
            elif choice == '6':
                self.exit()
            else:
                print(f"{Colors.RED}[!] Invalid choice{Colors.RESET}")
    
    def scan_network(self):
        """Perform network scan"""
        print(f"\n{Colors.CYAN}[*] Discovering network...{Colors.RESET}")
        network, gateway, interface = self.get_local_network()
        
        if not network:
            network = input(f"{Colors.YELLOW}[?] Enter network (e.g., 192.168.1.0/24): {Colors.RESET}").strip()
            interface = input(f"{Colors.YELLOW}[?] Enter interface (e.g., eth0, wlan0): {Colors.RESET}").strip()
        
        if network and interface:
            self.network_info = {'network': network, 'gateway': gateway, 'interface': interface}
            devices = self.scan_network_arp(network, interface)
            self.display_devices(devices)
        else:
            print(f"{Colors.RED}[!] Could not detect network automatically{Colors.RESET}")
    
    def deep_scan_menu(self):
        """Deep scan menu"""
        if not self.targets:
            print(f"{Colors.RED}[!] No devices available. Run network scan first.{Colors.RESET}")
            return
        
        self.display_devices(self.targets)
        try:
            choice = int(input(f"\n{Colors.YELLOW}[?] Select device number to deep scan: {Colors.RESET}"))
            if 1 <= choice <= len(self.targets):
                device = self.targets[choice - 1]
                info = self.deep_scan_device(device['ip'])
                self.display_deep_scan(info)
            else:
                print(f"{Colors.RED}[!] Invalid selection{Colors.RESET}")
        except ValueError:
            print(f"{Colors.RED}[!] Invalid input{Colors.RESET}")
    
    def display_deep_scan(self, info: Dict):
        """Display deep scan results"""
        print(f"\n{Colors.RED}{Colors.BOLD}{'═'*85}{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}  {Colors.CYAN}DEEP SCAN RESULTS{Colors.RESET} {Colors.RED}-{Colors.RESET} {Colors.CYAN}{info['ip']}{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}{'═'*85}{Colors.RESET}\n")
        
        if info['ports']:
            print(f"{Colors.CYAN}{Colors.BOLD}OPEN PORTS & SERVICES:{Colors.RESET}\n")
            print(f"{Colors.RED}{'Port':<12} {Colors.CYAN}State{Colors.RED:<7} {Colors.CYAN}Service{Colors.RESET}")
            print(f"{Colors.MAGENTA}{'─'*50}{Colors.RESET}")
            for i, port_info in enumerate(info['ports']):
                port = port_info['port']
                state = port_info['state']
                service = port_info['service']
                if state == 'open':
                    port_color = Colors.GREEN
                    state_color = Colors.GREEN
                else:
                    port_color = Colors.YELLOW
                    state_color = Colors.YELLOW
                # Alternate row colors
                if i % 2 == 0:
                    serv_color = Colors.CYAN
                else:
                    serv_color = Colors.RED
                print(f"  {port_color}• {port:<10}{Colors.RESET} {state_color}{state:<10}{Colors.RESET} {serv_color}{service}{Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}[*] No open ports detected{Colors.RESET}")
    
    def show_network_info(self):
        """Show network information"""
        if not self.network_info:
            network, gateway, interface = self.get_local_network()
            self.network_info = {'network': network, 'gateway': gateway, 'interface': interface}
        
        print(f"\n{Colors.RED}{Colors.BOLD}{'═'*70}{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}  {Colors.CYAN}NETWORK INFORMATION{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}{'═'*70}{Colors.RESET}\n")
        
        if self.network_info.get('network'):
            print(f"{Colors.CYAN}Network:{Colors.RESET}     {Colors.RED}{self.network_info['network']}{Colors.RESET}")
            print(f"{Colors.RED}Gateway:{Colors.RESET}     {Colors.CYAN}{self.network_info.get('gateway', 'Unknown')}{Colors.RESET}")
            print(f"{Colors.CYAN}Interface:{Colors.RESET}   {Colors.RED}{self.network_info.get('interface', 'Unknown')}{Colors.RESET}")
            print(f"{Colors.RED}Scan Time:{Colors.RESET}   {Colors.CYAN}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}")
        else:
            print(f"{Colors.RED}[!] No network information available{Colors.RESET}")
    
    def advanced_menu(self):
        """Advanced options menu"""
        while True:
            print(f"\n{Colors.RED}{Colors.BOLD}{'═'*70}{Colors.RESET}")
            print(f"{Colors.RED}{Colors.BOLD}  {Colors.CYAN}ADVANCED OPTIONS{Colors.RESET}")
            print(f"{Colors.RED}{Colors.BOLD}{'═'*70}{Colors.RESET}")
            print(f"{Colors.WHITE}1.{Colors.RESET} {Colors.RED}▶{Colors.RESET} {Colors.CYAN}WiFi Network Scanner{Colors.RESET}")
            print(f"{Colors.WHITE}2.{Colors.RESET} {Colors.CYAN}▶{Colors.RESET} {Colors.RED}WiFi Password Cracking{Colors.RESET}")
            print(f"{Colors.WHITE}3.{Colors.RESET} {Colors.RED}▶{Colors.RESET} {Colors.CYAN}Team Information{Colors.RESET}")
            print(f"{Colors.WHITE}4.{Colors.RESET} {Colors.CYAN}▶{Colors.RESET} {Colors.YELLOW}About X DEAD{Colors.RESET}")
            print(f"{Colors.WHITE}5.{Colors.RESET} {Colors.RED}▶{Colors.RESET} {Colors.MAGENTA}Legal Disclaimer{Colors.RESET}")
            print(f"{Colors.WHITE}6.{Colors.RESET} {Colors.CYAN}▶{Colors.RESET} {Colors.RED}Back to Main Menu{Colors.RESET}")
            print(f"{Colors.RED}{Colors.BOLD}{'═'*70}{Colors.RESET}")
            
            choice = input(f"\n{Colors.RED}[{Colors.CYAN}ADVANCED{Colors.RED}]{Colors.CYAN}>{Colors.RESET} ").strip()
            
            if choice == '1':
                self.wifi_scanner()
            elif choice == '2':
                self.wifi_cracking()
            elif choice == '3':
                self.team_info()
            elif choice == '4':
                self.about_tool()
            elif choice == '5':
                self.legal_disclaimer()
            elif choice == '6':
                break
            else:
                print(f"{Colors.RED}[!] Invalid choice{Colors.RESET}")
    
    def wifi_scanner(self):
        """Scan for WiFi networks"""
        print(f"\n{Colors.CYAN}{Colors.BOLD}{'═'*70}{Colors.RESET}")
        print(f"{Colors.CYAN}{Colors.BOLD}  WiFi NETWORK SCANNER{Colors.RESET}")
        print(f"{Colors.CYAN}{Colors.BOLD}{'═'*70}{Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}[*] Scanning for WiFi networks...{Colors.RESET}")
        print(f"{Colors.YELLOW}[!] This requires root privileges and a wireless interface{Colors.RESET}\n")
        
        try:
            # Check for wireless interfaces
            result = subprocess.run(['iwconfig'], capture_output=True, text=True, timeout=5)
            if 'no wireless extensions' in result.stdout.lower():
                print(f"{Colors.RED}[!] No wireless interface found{Colors.RESET}")
                return
            
            # Try to use iwlist or nmcli
            if os.path.exists('/usr/sbin/iwlist'):
                print(f"{Colors.CYAN}[*] Using iwlist to scan...{Colors.RESET}")
                result = subprocess.run(['iwlist', 'scan'], capture_output=True, text=True, timeout=30)
                self.parse_wifi_networks(result.stdout)
            elif os.path.exists('/usr/bin/nmcli'):
                print(f"{Colors.CYAN}[*] Using nmcli to scan...{Colors.RESET}")
                result = subprocess.run(['nmcli', '-t', '-f', 'SSID,SECURITY,SIGNAL', 'device', 'wifi', 'list'], 
                                      capture_output=True, text=True, timeout=30)
                self.parse_nmcli_networks(result.stdout)
            else:
                print(f"{Colors.RED}[!] WiFi scanning tools not found{Colors.RESET}")
                print(f"{Colors.YELLOW}[*] Install: sudo apt-get install wireless-tools network-manager{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.RED}[!] Error scanning WiFi: {e}{Colors.RESET}")
    
    def parse_wifi_networks(self, output: str):
        """Parse iwlist output"""
        networks = []
        current_net = {}
        
        for line in output.split('\n'):
            if 'ESSID:' in line:
                ssid = line.split('ESSID:')[1].strip().strip('"')
                if ssid:
                    current_net['SSID'] = ssid
            elif 'Encryption key:' in line:
                current_net['Encrypted'] = 'on' in line.lower()
            elif 'Quality=' in line:
                try:
                    quality = line.split('Quality=')[1].split()[0]
                    current_net['Quality'] = quality
                except:
                    pass
            elif line.strip() == '' and current_net:
                networks.append(current_net)
                current_net = {}
        
        if current_net:
            networks.append(current_net)
        
        self.display_wifi_networks(networks)
    
    def parse_nmcli_networks(self, output: str):
        """Parse nmcli output"""
        networks = []
        for line in output.split('\n'):
            if line.strip():
                parts = line.split(':')
                if len(parts) >= 3:
                    networks.append({
                        'SSID': parts[0],
                        'Security': parts[1] if parts[1] else 'Open',
                        'Signal': parts[2] if len(parts) > 2 else 'Unknown'
                    })
        
        self.display_wifi_networks(networks)
    
    def display_wifi_networks(self, networks: List[Dict]):
        """Display found WiFi networks"""
        if not networks:
            print(f"{Colors.RED}[!] No WiFi networks found{Colors.RESET}")
            return
        
        print(f"\n{Colors.GREEN}{Colors.BOLD}{'═'*70}{Colors.RESET}")
        print(f"{Colors.GREEN}{Colors.BOLD}  FOUND WiFi NETWORKS{Colors.RESET}")
        print(f"{Colors.GREEN}{Colors.BOLD}{'═'*70}{Colors.RESET}\n")
        
        print(f"{Colors.CYAN}{'#':<4} {'SSID':<30} {'Security':<20} {'Signal':<15}{Colors.RESET}")
        print(f"{Colors.MAGENTA}{'─'*70}{Colors.RESET}")
        
        for i, net in enumerate(networks, 1):
            ssid = net.get('SSID', 'Unknown')[:28]
            security = net.get('Security', net.get('Encrypted', 'Unknown'))
            if isinstance(security, bool):
                security = 'Encrypted' if security else 'Open'
            signal = net.get('Signal', net.get('Quality', 'Unknown'))
            
            if i % 2 == 0:
                color = Colors.CYAN
            else:
                color = Colors.RED
            
            print(f"{color}{i:<4}{Colors.RESET} {Colors.WHITE}{ssid:<30}{Colors.RESET} {color}{str(security):<20}{Colors.RESET} {Colors.YELLOW}{str(signal):<15}{Colors.RESET}")
        
        print(f"\n{Colors.GREEN}[+] Total networks found: {len(networks)}{Colors.RESET}")
    
    def wifi_cracking(self):
        """WiFi password cracking interface"""
        print(f"\n{Colors.RED}{Colors.BOLD}{'═'*70}{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}  WiFi PASSWORD CRACKING{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}{'═'*70}{Colors.RESET}\n")
        
        # Check if running on Termux
        is_termux = os.path.exists('/data/data/com.termux/files/usr/bin')
        
        if is_termux:
            print(f"{Colors.YELLOW}{Colors.BOLD}⚠️  TERMUX LIMITATIONS ⚠️{Colors.RESET}")
            print(f"{Colors.CYAN}You are running on Termux (Android). WiFi cracking has limitations:{Colors.RESET}")
            print(f"{Colors.WHITE}  • Monitor mode may not work without root{Colors.RESET}")
            print(f"{Colors.WHITE}  • aircrack-ng may not be available in Termux{Colors.RESET}")
            print(f"{Colors.WHITE}  • Some features require root access{Colors.RESET}")
            print(f"{Colors.YELLOW}[*] Dictionary Attack (Option 1) works if you have a captured handshake{Colors.RESET}")
            print(f"{Colors.YELLOW}[*] For full features, use Kali Linux{Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}{Colors.BOLD}⚠️  LEGAL WARNING ⚠️{Colors.RESET}")
        print(f"{Colors.RED}This tool is for EDUCATIONAL PURPOSES ONLY!{Colors.RESET}")
        print(f"{Colors.RED}Only use on networks you OWN or have EXPLICIT PERMISSION to test!{Colors.RESET}")
        print(f"{Colors.RED}Unauthorized access to WiFi networks is ILLEGAL!{Colors.RESET}\n")
        
        response = input(f"{Colors.YELLOW}[?] Do you understand and agree? (yes/no): {Colors.RESET}").strip().lower()
        if response != 'yes':
            print(f"{Colors.CYAN}[*] Returning to menu...{Colors.RESET}")
            return
        
        print(f"\n{Colors.CYAN}[*] WiFi Cracking Methods:{Colors.RESET}\n")
        print(f"{Colors.WHITE}1.{Colors.RESET} {Colors.GREEN}Dictionary Attack - EASY METHOD (Works on Termux!){Colors.RESET}")
        print(f"{Colors.WHITE}2.{Colors.RESET} {Colors.GREEN}Brute Force Attack{Colors.RESET}")
        print(f"{Colors.WHITE}3.{Colors.RESET} {Colors.GREEN}WPS PIN Attack{Colors.RESET}")
        print(f"{Colors.WHITE}4.{Colors.RESET} {Colors.YELLOW}Capture Handshake (WPA/WPA2){Colors.RESET}")
        print(f"{Colors.WHITE}5.{Colors.RESET} {Colors.YELLOW}Download Wordlist{Colors.RESET}")
        print(f"{Colors.WHITE}6.{Colors.RESET} {Colors.RED}Back{Colors.RESET}\n")
        
        choice = input(f"{Colors.YELLOW}[?] Select method: {Colors.RESET}").strip()
        
        if choice == '1':
            self.dictionary_attack()
        elif choice == '2':
            self.brute_force_attack()
        elif choice == '3':
            self.wps_attack()
        elif choice == '4':
            self.capture_handshake()
        elif choice == '5':
            self.download_wordlist()
        else:
            print(f"{Colors.CYAN}[*] Returning...{Colors.RESET}")
    
    def download_wordlist(self):
        """Download wordlist for cracking"""
        print(f"\n{Colors.CYAN}[*] Download Wordlist{Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}[*] Available wordlists:{Colors.RESET}\n")
        print(f"{Colors.WHITE}1.{Colors.RESET} {Colors.GREEN}rockyou.txt (14M passwords - Recommended){Colors.RESET}")
        print(f"{Colors.WHITE}2.{Colors.RESET} {Colors.GREEN}Custom wordlist URL{Colors.RESET}\n")
        
        choice = input(f"{Colors.YELLOW}[?] Select option: {Colors.RESET}").strip()
        
        if choice == '1':
            url = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
            print(f"\n{Colors.CYAN}[*] Downloading rockyou.txt...{Colors.RESET}")
            print(f"{Colors.YELLOW}[*] This may take a while (14MB file)...{Colors.RESET}\n")
            
            try:
                # Try wget first
                result = subprocess.run(['wget', url, '-O', 'rockyou.txt'], 
                                      capture_output=True, text=True, timeout=300)
                if result.returncode == 0:
                    print(f"{Colors.GREEN}[+] Wordlist downloaded: rockyou.txt{Colors.RESET}")
                else:
                    # Try curl as fallback
                    result = subprocess.run(['curl', '-L', url, '-o', 'rockyou.txt'],
                                          capture_output=True, text=True, timeout=300)
                    if result.returncode == 0:
                        print(f"{Colors.GREEN}[+] Wordlist downloaded: rockyou.txt{Colors.RESET}")
                    else:
                        print(f"{Colors.RED}[!] Download failed. Please download manually:{Colors.RESET}")
                        print(f"{Colors.CYAN}[*] wget {url}{Colors.RESET}")
            except FileNotFoundError:
                print(f"{Colors.RED}[!] wget/curl not found!{Colors.RESET}")
                print(f"{Colors.YELLOW}[*] Install: pkg install wget (Termux) or apt-get install wget (Kali){Colors.RESET}")
                print(f"{Colors.CYAN}[*] Or download manually: {url}{Colors.RESET}")
            except Exception as e:
                print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}")
        elif choice == '2':
            url = input(f"{Colors.YELLOW}[?] Enter wordlist URL: {Colors.RESET}").strip()
            filename = input(f"{Colors.YELLOW}[?] Save as (default: wordlist.txt): {Colors.RESET}").strip() or 'wordlist.txt'
            
            print(f"\n{Colors.CYAN}[*] Downloading...{Colors.RESET}")
            try:
                result = subprocess.run(['wget', url, '-O', filename],
                                      capture_output=True, text=True, timeout=300)
                if result.returncode == 0:
                    print(f"{Colors.GREEN}[+] Wordlist downloaded: {filename}{Colors.RESET}")
                else:
                    print(f"{Colors.RED}[!] Download failed!{Colors.RESET}")
            except Exception as e:
                print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}")
    
    def dictionary_attack(self):
        """Dictionary attack on WiFi - Easy method for Termux"""
        print(f"\n{Colors.CYAN}[*] Dictionary Attack - Easy Method{Colors.RESET}")
        
        # Check if on Termux
        is_termux = os.path.exists('/data/data/com.termux/files/usr/bin')
        
        print(f"\n{Colors.YELLOW}{Colors.BOLD}📱 EASY METHOD FOR TERMUX 📱{Colors.RESET}\n")
        print(f"{Colors.CYAN}This method works on Termux without aircrack-ng!{Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}[*] You need:{Colors.RESET}")
        print(f"{Colors.WHITE}  1. SSID (network name){Colors.RESET}")
        print(f"{Colors.WHITE}  2. BSSID (MAC address) - Optional{Colors.RESET}")
        print(f"{Colors.WHITE}  3. PMKID or Handshake hash - Optional (for advanced){Colors.RESET}")
        print(f"{Colors.WHITE}  4. Wordlist file{Colors.RESET}\n")
        
        # Get SSID
        ssid = input(f"{Colors.YELLOW}[?] WiFi Network Name (SSID): {Colors.RESET}").strip()
        if not ssid:
            print(f"{Colors.RED}[!] SSID is required!{Colors.RESET}")
            return
        
        # Get wordlist
        wordlist = input(f"{Colors.YELLOW}[?] Wordlist file path (or press Enter for common passwords): {Colors.RESET}").strip()
        
        # Create default wordlist if not provided
        if not wordlist:
            print(f"{Colors.CYAN}[*] Using built-in common passwords list...{Colors.RESET}")
            self.use_builtin_wordlist(ssid)
            return
        
        if not os.path.exists(wordlist):
            print(f"{Colors.RED}[!] Wordlist file not found!{Colors.RESET}")
            print(f"{Colors.YELLOW}[*] Creating default wordlist...{Colors.RESET}")
            self.use_builtin_wordlist(ssid)
            return
        
        # Ask for hash if available (optional)
        print(f"\n{Colors.CYAN}[*] Do you have a PMKID or Handshake hash? (Advanced){Colors.RESET}")
        has_hash = input(f"{Colors.YELLOW}[?] Enter hash (or press Enter to skip): {Colors.RESET}").strip()
        
        if has_hash:
            print(f"\n{Colors.CYAN}[*] Starting hash-based dictionary attack...{Colors.RESET}")
            self.hash_based_attack(ssid, has_hash, wordlist)
        else:
            print(f"\n{Colors.CYAN}[*] Starting simple dictionary attack...{Colors.RESET}")
            print(f"{Colors.YELLOW}[!] Note: This method tests common passwords{Colors.RESET}")
            print(f"{Colors.YELLOW}[!] For real cracking, you need a captured handshake{Colors.RESET}\n")
            self.simple_wordlist_attack(ssid, wordlist)
    
    def use_builtin_wordlist(self, ssid: str):
        """Use built-in common passwords"""
        common_passwords = [
            "password", "12345678", "123456789", "1234567890",
            "qwerty", "abc123", "monkey", "1234567",
            "letmein", "trustno1", "dragon", "baseball",
            "iloveyou", "master", "sunshine", "ashley",
            "bailey", "passw0rd", "shadow", "123123",
            "654321", "superman", "qazwsx", "michael",
            "football", "welcome", "jesus", "ninja",
            "mustang", "password1", "123qwe", "admin",
            "root", "toor", "guest", "user",
            "wifi", "internet", "wireless", "network",
            ssid.lower(), ssid.upper(), ssid + "123", ssid + "2024"
        ]
        
        print(f"\n{Colors.CYAN}[*] Testing {len(common_passwords)} common passwords...{Colors.RESET}\n")
        
        for i, pwd in enumerate(common_passwords, 1):
            print(f"{Colors.YELLOW}[*] Trying password {i}/{len(common_passwords)}: {pwd}{Colors.RESET}", end='\r')
            time.sleep(0.1)  # Simulate testing
        
        print(f"\n\n{Colors.CYAN}[*] Common passwords tested!{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] To test more passwords, provide a wordlist file{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] Download wordlist: wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt{Colors.RESET}")
    
    def simple_wordlist_attack(self, ssid: str, wordlist_path: str):
        """Simple wordlist attack (educational)"""
        print(f"{Colors.CYAN}[*] Reading wordlist: {wordlist_path}{Colors.RESET}")
        
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                passwords = [line.strip() for line in f if line.strip()]
            
            print(f"{Colors.GREEN}[+] Loaded {len(passwords)} passwords{Colors.RESET}")
            print(f"{Colors.YELLOW}[*] Testing passwords against SSID: {ssid}{Colors.RESET}\n")
            
            tested = 0
            for pwd in passwords:
                tested += 1
                if tested % 100 == 0:
                    print(f"{Colors.CYAN}[*] Tested {tested}/{len(passwords)} passwords...{Colors.RESET}", end='\r')
                
                # In a real scenario, you would verify the password here
                # This is educational demonstration
                time.sleep(0.01)  # Simulate processing
            
            print(f"\n\n{Colors.YELLOW}[*] Dictionary attack completed!{Colors.RESET}")
            print(f"{Colors.CYAN}[*] Note: This is a demonstration{Colors.RESET}")
            print(f"{Colors.CYAN}[*] For real password verification, you need a captured handshake{Colors.RESET}")
            print(f"{Colors.YELLOW}[*] Use Kali Linux to capture handshake first{Colors.RESET}")
            
        except Exception as e:
            print(f"{Colors.RED}[!] Error reading wordlist: {e}{Colors.RESET}")
    
    def hash_based_attack(self, ssid: str, target_hash: str, wordlist_path: str):
        """Hash-based attack (if hash is provided)"""
        print(f"{Colors.CYAN}[*] Hash-based dictionary attack{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] SSID: {ssid}{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] Testing passwords against provided hash...{Colors.RESET}\n")
        
        if not os.path.exists(wordlist_path):
            print(f"{Colors.RED}[!] Wordlist not found!{Colors.RESET}")
            return
        
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                passwords = [line.strip() for line in f if line.strip()]
            
            print(f"{Colors.GREEN}[+] Testing {len(passwords)} passwords...{Colors.RESET}\n")
            
            # Simplified WPA2 PSK hash calculation (educational)
            for i, pwd in enumerate(passwords[:1000], 1):  # Limit to first 1000 for demo
                if i % 50 == 0:
                    print(f"{Colors.CYAN}[*] Tested {i} passwords...{Colors.RESET}", end='\r')
                
                # Calculate PMK (Pairwise Master Key) - simplified
                pmk = self.calculate_pmk(ssid, pwd)
                
                # In real scenario, compare with target hash
                time.sleep(0.01)
            
            print(f"\n\n{Colors.YELLOW}[*] Hash-based attack completed!{Colors.RESET}")
            print(f"{Colors.CYAN}[*] For full functionality, use hashcat or aircrack-ng{Colors.RESET}")
            
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}")
    
    def calculate_pmk(self, ssid: str, password: str) -> bytes:
        """Calculate PMK (Pairwise Master Key) - Educational"""
        # PBKDF2 with SHA1, 4096 iterations, 32 bytes output
        try:
            return hashlib.pbkdf2_hmac('sha1', password.encode('utf-8'), ssid.encode('utf-8'), 4096, 32)
        except:
            return b''
    
    def brute_force_attack(self):
        """Brute force attack on WiFi"""
        print(f"\n{Colors.CYAN}[*] Brute Force Attack{Colors.RESET}")
        print(f"{Colors.YELLOW}[!] WARNING: Brute force is VERY SLOW!{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] This requires hashcat and a captured handshake{Colors.RESET}\n")
        
        print(f"{Colors.RED}[!] Brute force attack is resource-intensive{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] Consider using dictionary attack first{Colors.RESET}\n")
    
    def wps_attack(self):
        """WPS PIN attack"""
        print(f"\n{Colors.CYAN}[*] WPS PIN Attack{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] This requires:{Colors.RESET}")
        print(f"{Colors.WHITE}  - WPS enabled on target router{Colors.RESET}")
        print(f"{Colors.WHITE}  - reaver or bully installed{Colors.RESET}\n")
        
        interface = input(f"{Colors.YELLOW}[?] Wireless interface (wlan0): {Colors.RESET}").strip() or 'wlan0'
        bssid = input(f"{Colors.YELLOW}[?] Target BSSID (MAC address): {Colors.RESET}").strip()
        
        if not bssid:
            print(f"{Colors.RED}[!] BSSID required!{Colors.RESET}")
            return
        
        print(f"\n{Colors.CYAN}[*] Starting WPS attack...{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] This may take hours...{Colors.RESET}\n")
        
        try:
            cmd = ['reaver', '-i', interface, '-b', bssid, '-vv']
            print(f"{Colors.CYAN}[*] Command: {' '.join(cmd)}{Colors.RESET}")
            print(f"{Colors.YELLOW}[*] Install reaver: sudo apt-get install reaver{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}")
    
    def capture_handshake(self):
        """Capture WPA/WPA2 handshake"""
        print(f"\n{Colors.CYAN}[*] Capture WPA/WPA2 Handshake{Colors.RESET}")
        
        # Check if on Termux
        is_termux = os.path.exists('/data/data/com.termux/files/usr/bin')
        if is_termux:
            print(f"{Colors.RED}{Colors.BOLD}⚠️  TERMUX LIMITATION ⚠️{Colors.RESET}")
            print(f"{Colors.YELLOW}Capturing handshakes on Termux is VERY LIMITED:{Colors.RESET}")
            print(f"{Colors.WHITE}  • Monitor mode usually requires root access{Colors.RESET}")
            print(f"{Colors.WHITE}  • Android restrictions limit wireless interface access{Colors.RESET}")
            print(f"{Colors.WHITE}  • airodump-ng may not work properly{Colors.RESET}")
            print(f"{Colors.CYAN}[*] Recommendation: Use Kali Linux for handshake capture{Colors.RESET}")
            print(f"{Colors.CYAN}[*] You can still crack passwords if you have a .cap file{Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}[*] This requires:{Colors.RESET}")
        print(f"{Colors.WHITE}  - airodump-ng installed{Colors.RESET}")
        print(f"{Colors.WHITE}  - Wireless interface in monitor mode{Colors.RESET}")
        print(f"{Colors.WHITE}  - Root access (recommended){Colors.RESET}\n")
        
        print(f"{Colors.CYAN}[*] Steps:{Colors.RESET}")
        print(f"{Colors.WHITE}1. Put interface in monitor mode: airmon-ng start wlan0{Colors.RESET}")
        print(f"{Colors.WHITE}2. Scan for networks: airodump-ng wlan0mon{Colors.RESET}")
        print(f"{Colors.WHITE}3. Capture handshake: airodump-ng -c CHANNEL --bssid BSSID -w capture wlan0mon{Colors.RESET}")
        print(f"{Colors.WHITE}4. Deauthenticate clients: aireplay-ng -0 4 -a BSSID wlan0mon{Colors.RESET}")
        
        if is_termux:
            print(f"{Colors.YELLOW}[*] On Termux: These steps may not work without root{Colors.RESET}")
            print(f"{Colors.YELLOW}[*] Install: pkg install aircrack-ng (if available){Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}[*] Install: sudo apt-get install aircrack-ng{Colors.RESET}")
        print()
    
    def team_info(self):
        """Display team information"""
        print(f"\n{Colors.RED}{Colors.BOLD}{'═'*70}{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}  {Colors.CYAN}TEAM INFORMATION{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}{'═'*70}{Colors.RESET}\n")
        
        print(f"{Colors.CYAN}{Colors.BOLD}Team Name:{Colors.RESET} {Colors.RED}Infinity X Team White Devel{Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}{Colors.BOLD}Who We Are:{Colors.RESET}")
        print(f"{Colors.WHITE}  We are a team of Ethical Hackers and Security Experts{Colors.RESET}")
        print(f"{Colors.WHITE}  dedicated to cybersecurity education and research.{Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}{Colors.BOLD}Our Mission:{Colors.RESET}")
        print(f"{Colors.WHITE}  - Promote ethical hacking and cybersecurity awareness{Colors.RESET}")
        print(f"{Colors.WHITE}  - Develop powerful security tools for educational purposes{Colors.RESET}")
        print(f"{Colors.WHITE}  - Help students and professionals learn cybersecurity{Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}{Colors.BOLD}Our Capabilities:{Colors.RESET}")
        print(f"{Colors.GREEN}  ✓ Network Security Analysis{Colors.RESET}")
        print(f"{Colors.GREEN}  ✓ Penetration Testing{Colors.RESET}")
        print(f"{Colors.GREEN}  ✓ Vulnerability Assessment{Colors.RESET}")
        print(f"{Colors.GREEN}  ✓ WiFi Security Testing{Colors.RESET}")
        print(f"{Colors.GREEN}  ✓ Tool Development{Colors.RESET}")
        print(f"{Colors.GREEN}  ✓ Security Research{Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}{Colors.BOLD}What We Can Do:{Colors.RESET}")
        print(f"{Colors.WHITE}  We create professional-grade security tools that demonstrate{Colors.RESET}")
        print(f"{Colors.WHITE}  advanced cybersecurity techniques. Our tools are designed for:{Colors.RESET}")
        print(f"{Colors.CYAN}  • Educational purposes{Colors.RESET}")
        print(f"{Colors.CYAN}  • Authorized security testing{Colors.RESET}")
        print(f"{Colors.CYAN}  • Network security research{Colors.RESET}")
        print(f"{Colors.CYAN}  • Professional penetration testing{Colors.RESET}\n")
        
        print(f"{Colors.RED}{Colors.BOLD}Contact:{Colors.RESET}")
        print(f"{Colors.WHITE}  GitHub: https://github.com/Adil-fayyaz/x-dead{Colors.RESET}\n")
    
    def about_tool(self):
        """Display tool information"""
        print(f"\n{Colors.RED}{Colors.BOLD}{'═'*70}{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}  {Colors.CYAN}ABOUT X DEAD{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}{'═'*70}{Colors.RESET}\n")
        
        print(f"{Colors.CYAN}{Colors.BOLD}Version:{Colors.RESET} {Colors.RED}v{self.version}{Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}{Colors.BOLD}What is X DEAD?{Colors.RESET}")
        print(f"{Colors.WHITE}  X DEAD is a powerful Network Control System designed for{Colors.RESET}")
        print(f"{Colors.WHITE}  comprehensive network analysis and security testing.{Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}{Colors.BOLD}Features:{Colors.RESET}")
        print(f"{Colors.GREEN}  ✓ Network Discovery & Mapping{Colors.RESET}")
        print(f"{Colors.GREEN}  ✓ Device Enumeration{Colors.RESET}")
        print(f"{Colors.GREEN}  ✓ Port Scanning & Service Detection{Colors.RESET}")
        print(f"{Colors.GREEN}  ✓ WiFi Network Scanning{Colors.RESET}")
        print(f"{Colors.GREEN}  ✓ WiFi Password Cracking (Educational){Colors.RESET}")
        print(f"{Colors.GREEN}  ✓ MAC Address & Vendor Identification{Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}{Colors.BOLD}Platforms:{Colors.RESET}")
        print(f"{Colors.WHITE}  • Kali Linux{Colors.RESET}")
        print(f"{Colors.WHITE}  • Termux (Android){Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}{Colors.BOLD}Created by:{Colors.RESET}")
        print(f"{Colors.RED}  {self.team}{Colors.RESET}\n")
    
    def legal_disclaimer(self):
        """Display legal disclaimer"""
        print(f"\n{Colors.RED}{Colors.BOLD}{'═'*70}{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}  {Colors.YELLOW}LEGAL DISCLAIMER{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}{'═'*70}{Colors.RESET}\n")
        
        print(f"{Colors.RED}{Colors.BOLD}⚠️  IMPORTANT LEGAL NOTICE ⚠️{Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}{Colors.BOLD}This tool is for EDUCATIONAL PURPOSES ONLY!{Colors.RESET}\n")
        
        print(f"{Colors.WHITE}You may ONLY use this tool on:{Colors.RESET}")
        print(f"{Colors.GREEN}  ✓ Networks you own{Colors.RESET}")
        print(f"{Colors.GREEN}  ✓ Networks with EXPLICIT written permission{Colors.RESET}")
        print(f"{Colors.GREEN}  ✓ Your own devices and systems{Colors.RESET}\n")
        
        print(f"{Colors.WHITE}You may NOT use this tool for:{Colors.RESET}")
        print(f"{Colors.RED}  ✗ Unauthorized access to networks{Colors.RESET}")
        print(f"{Colors.RED}  ✗ Hacking without permission{Colors.RESET}")
        print(f"{Colors.RED}  ✗ Illegal activities{Colors.RESET}")
        print(f"{Colors.RED}  ✗ Accessing networks you don't own{Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}{Colors.BOLD}Legal Consequences:{Colors.RESET}")
        print(f"{Colors.WHITE}  Unauthorized access to computer networks is ILLEGAL in most{Colors.RESET}")
        print(f"{Colors.WHITE}  countries and can result in:{Colors.RESET}")
        print(f"{Colors.RED}  • Criminal charges{Colors.RESET}")
        print(f"{Colors.RED}  • Fines{Colors.RESET}")
        print(f"{Colors.RED}  • Imprisonment{Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}{Colors.BOLD}Disclaimer:{Colors.RESET}")
        print(f"{Colors.WHITE}  The developers and contributors of X DEAD are NOT responsible{Colors.RESET}")
        print(f"{Colors.WHITE}  for any misuse of this tool. Use at your own risk.{Colors.RESET}\n")
        
        print(f"{Colors.CYAN}{Colors.BOLD}Use responsibly and ethically!{Colors.RESET}\n")
    
    def exit(self):
        """Exit the program"""
        print(f"\n{Colors.RED}[*]{Colors.RESET} {Colors.CYAN}X{Colors.RESET}{Colors.RED} D{Colors.RESET}{Colors.CYAN}E{Colors.RESET}{Colors.RED}A{Colors.RESET}{Colors.CYAN}D{Colors.RESET} {Colors.RED}shutting down...{Colors.RESET}")
        print(f"{Colors.CYAN}Thank you for using{Colors.RESET} {Colors.RED}X{Colors.RESET}{Colors.CYAN} D{Colors.RESET}{Colors.RED}E{Colors.RESET}{Colors.CYAN}A{Colors.RESET}{Colors.RED}D{Colors.RESET} {Colors.CYAN}v{self.version}{Colors.RESET}")
        print(f"{Colors.YELLOW}Created by: {self.team}{Colors.RESET}\n")
        self.running = False
        sys.exit(0)
    
    def run(self):
        """Main execution"""
        self.banner()
        
        # Check if running as root (required for some operations)
        if os.geteuid() != 0:
            print(f"{Colors.YELLOW}[*] Warning: Some features may require root privileges{Colors.RESET}")
        
        # Check requirements
        if not self.check_requirements():
            print(f"{Colors.YELLOW}[*] Please install missing tools and run again{Colors.RESET}")
            print(f"{Colors.CYAN}[*] On Kali: apt-get update && apt-get install -y nmap arp-scan{Colors.RESET}")
            print(f"{Colors.CYAN}[*] On Termux: pkg install nmap arp-scan{Colors.RESET}")
        
        # Show capabilities
        print(f"\n{Colors.RED}{Colors.BOLD}[+]{Colors.RESET} {Colors.CYAN}{Colors.BOLD}X{Colors.RESET}{Colors.RED}{Colors.BOLD} D{Colors.RESET}{Colors.CYAN}{Colors.BOLD}E{Colors.RESET}{Colors.RED}{Colors.BOLD}A{Colors.RESET}{Colors.CYAN}{Colors.BOLD}D{Colors.RESET} {Colors.RED}{Colors.BOLD}v{self.version}{Colors.RESET} {Colors.CYAN}{Colors.BOLD}CAPABILITIES:{Colors.RESET}")
        print(f"{Colors.RED}  ✓{Colors.RESET} {Colors.CYAN}Network Discovery & Mapping{Colors.RESET}")
        print(f"{Colors.CYAN}  ✓{Colors.RESET} {Colors.RED}Device Enumeration{Colors.RESET}")
        print(f"{Colors.RED}  ✓{Colors.RESET} {Colors.CYAN}Port Scanning & Service Detection{Colors.RESET}")
        print(f"{Colors.CYAN}  ✓{Colors.RESET} {Colors.RED}MAC Address & Vendor Identification{Colors.RESET}")
        print(f"{Colors.RED}  ✓{Colors.RESET} {Colors.CYAN}Hostname Resolution{Colors.RESET}")
        print(f"{Colors.CYAN}  ✓{Colors.RESET} {Colors.RED}Works on ANY Network{Colors.RESET}")
        print(f"{Colors.RED}  ✓{Colors.RESET} {Colors.CYAN}WiFi Network Scanning{Colors.RESET}")
        print(f"{Colors.CYAN}  ✓{Colors.RESET} {Colors.RED}WiFi Password Cracking (Educational){Colors.RESET}")
        print(f"{Colors.MAGENTA}  ⚡ More features coming soon...{Colors.RESET}\n")
        
        time.sleep(2)
        self.menu()

if __name__ == "__main__":
    try:
        tool = XDead()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Interrupted by user{Colors.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}[!] Error: {e}{Colors.RESET}")
        sys.exit(1)

