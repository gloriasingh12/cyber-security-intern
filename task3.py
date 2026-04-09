# =================================================================
# PROJECT: Modular Penetration Testing Toolkit
# DESCRIPTION: Multi-module security tool (Port Scanner & Brute-forcer).
# DELIVERABLE: Python-based toolkit with modular architecture.
# =================================================================

import socket
import time

class PenTestToolkit:
    def __init__(self, target):
        self.target = target
        print(f"🛠️  PenTest Toolkit Loaded. Target: {self.target}")

    # MODULE 1: Port Scanner
    def port_scanner(self, ports):
        """Checks which ports are open on the target system."""
        print(f"\n🔍 [Module 1] Starting Port Scan on {self.target}...")
        open_ports = []
        for port in ports:
            # Simulating a socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            # result = s.connect_ex((self.target, port)) # Real connection
            result = 0 if port in [80, 443] else 1 # Simulated results
            
            if result == 0:
                open_ports.append(port)
                print(f"   [+] Port {port}: OPEN")
            s.close()
        return open_ports

    # MODULE 2: Simple Brute-forcer
    def brute_forcer(self, username, password_list):
        """Simulates a dictionary attack on a login portal."""
        print(f"\n🔑 [Module 2] Starting Brute-force Attack for User: {username}")
        correct_password = "password123" # Simulated target password
        
        for password in password_list:
            print(f"   [*] Testing: {password}...")
            time.sleep(0.2) # Adding realism
            if password == correct_password:
                print(f"   [!] SUCCESS: Password found -> {password}")
                return True
        print("   [-] Brute-force failed. Password not in list.")
        return False

    # MODULE 3: Security Header Checker
    def header_checker(self):
        """Checks for missing security headers like X-Frame-Options."""
        print(f"\n🛡️ [Module 3] Analyzing Security Headers for {self.target}...")
        # Simulated headers
        headers = ["Content-Type", "Server"]
        secure_headers = ["X-Frame-Options", "Content-Security-Policy"]
        
        for header in secure_headers:
            if header not in headers:
                print(f"   [!] MISSING: {header} (Risk: High)")
        print("   [+] Analysis Complete.")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Target setup
    target_host = "192.168.1.105"
    toolkit = PenTestToolkit(target_host)

    # 1. Run Port Scanner (Deliverable)
    toolkit.port_scanner([21, 22, 80, 443, 3
