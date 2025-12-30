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
        required_tools = ['nmap', 'arp-scan']
        missing_tools = []
        
        for tool in required_tools:
            try:
                subprocess.run([tool, '--version'], 
                             stdout=subprocess.PIPE, 
                             stderr=subprocess.PIPE, 
                             timeout=5)
            except (FileNotFoundError, subprocess.TimeoutExpired):
                missing_tools.append(tool)
        
        if missing_tools:
            print(f"{Colors.RED}[!] Missing tools: {', '.join(missing_tools)}{Colors.RESET}")
            print(f"{Colors.YELLOW}[*] Installing required tools...{Colors.RESET}")
            return False
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
        except Exception as e:
            print(f"{Colors.YELLOW}[*] ARP scan failed, trying alternative method...{Colors.RESET}")
            # Fallback to ping scan
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
        print(f"\n{Colors.CYAN}{Colors.BOLD}  ADVANCED OPTIONS{Colors.RESET}")
        print(f"{Colors.CYAN}{'='*60}{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] Advanced features coming in v2.0...{Colors.RESET}")
        print(f"{Colors.MAGENTA}    - Network Traffic Analysis{Colors.RESET}")
        print(f"{Colors.MAGENTA}    - Vulnerability Assessment{Colors.RESET}")
        print(f"{Colors.MAGENTA}    - Exploit Framework Integration{Colors.RESET}")
        print(f"{Colors.MAGENTA}    - Automated Attack Vectors{Colors.RESET}")
    
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

