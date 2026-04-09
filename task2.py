# =================================================================
# PROJECT: Web Application Vulnerability Scanner
# DESCRIPTION: Scanning for SQL Injection (SQLi) and XSS vulnerabilities.
# DELIVERABLE: Python script using 'requests' and 'BeautifulSoup' logic.
# =================================================================

import requests
from bs4 import BeautifulSoup

class WebScanner:
    def __init__(self):
        # Common payloads to test for vulnerabilities
        self.xss_payload = "<script>alert('XSS')</script>"
        self.sqli_payload = "' OR '1'='1"
        print("🔍 Web Vulnerability Scanner Initialized...")

    def scan_xss(self, url, html_content):
        """Simulates checking if a script payload is reflected in the page."""
        print(f"📡 Testing for XSS on: {url}")
        # Logic: If the payload is rendered back without escaping, it's vulnerable
        if self.xss_payload in html_content:
            return "🔴 VULNERABLE (Cross-Site Scripting Detected)"
        return "🟢 SECURE (No XSS reflected)"

    def scan_sqli(self, url):
        """Simulates checking for SQL Injection by appending payloads to parameters."""
        print(f"📡 Testing for SQL Injection on: {url}?id={self.sqli_payload}")
        # In a real scanner, we check for database error messages in the response
        simulated_response = "SQL Syntax Error near '1'='1'" 
        
        if "SQL Syntax Error" in simulated_response:
            return "🔴 VULNERABLE (SQL Injection Detected)"
        return "🟢 SECURE (No SQL errors found)"

    def run_full_scan(self, target_url):
        print("\n" + "="*50)
        print(f"🛡️  VULNERABILITY REPORT FOR: {target_url}")
        print("="*50)

        # 1. Fetching page content (Simulated)
        simulated_html = f"<html><body>Search Results for {self.xss_payload}</body></html>"
        
        # 2. XSS Check
        xss_result = self.scan_xss(target_url, simulated_html)
        print(f"   - XSS Status:  {xss_result}")

        # 3. SQLi Check
        sqli_result = self.scan_sqli(target_url)
        print(f"   - SQLi Status: {sqli_result}")

        print("="*50)

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    scanner = WebScanner()

    # Target URL for the scan
    target = "http://aditya-test-app.soit.edu"

    # Execute the scan (Deliverable)
    scanner.run_full_scan(target)

    print("\n
