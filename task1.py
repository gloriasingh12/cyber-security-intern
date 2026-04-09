# =================================================================
# PROJECT: File Integrity Checker
# DESCRIPTION: Monitoring file changes using SHA-256 hashing logic.
# DELIVERABLE: Python script using 'hashlib' to ensure data integrity.
# =================================================================

import hashlib
import os

class IntegrityChecker:
    def __init__(self):
        # Database to store original file hashes: {filename: hash_value}
        self.reference_hashes = {}
        print("🛡️ Integrity Monitoring System Initialized...")

    def calculate_hash(self, content):
        """Calculates the SHA-256 hash of given content."""
        return hashlib.sha256(content.encode()).hexdigest()

    def register_file(self, filename, content):
        """Stores the initial 'Gold Standard' hash of a file."""
        file_hash = self.calculate_hash(content)
        self.reference_hashes[filename] = file_hash
        print(f"✅ Registered: '{filename}' [Hash: {file_hash[:16]}...]")

    def verify_integrity(self, filename, current_content):
        """Compares current hash with stored hash to detect tampering."""
        if filename not in self.reference_hashes:
            print(f"⚠️ Error: File '{filename}' is not registered in the system.")
            return

        current_hash = self.calculate_hash(current_content)
        original_hash = self.reference_hashes[filename]

        print(f"\n🔍 Checking Integrity for: {filename}")
        if current_hash == original_hash:
            print(f"🟢 STATUS: SAFE. No changes detected.")
        else:
            print(f"🔴 ALERT: TAMPERING DETECTED! File content has been modified.")
            print(f"   Original Hash: {original_hash[:16]}...")
            print(f"   Current Hash:  {current_hash[:16]}...")

# --- MAIN EXECUTION (Simulation) ---
if __name__ == "__main__":
    checker = IntegrityChecker()

    # 1. Simulating original files (The "Safe" State)
    file_a_content = "User Data: Aditya Tripathi, ID: 101, Status: Active"
    file_b_content = "Config: Server_Port=8080, Auth=Enabled"

    print("--- 📥 Registering Secure Files ---")
    checker.register_file("user_records.db", file_a_content)
    checker.register_file("server_config.sys", file_b_content)

    # 2. Verifying File A (No changes)
    checker.verify_integrity("user_records.db", file_a_content)

    # 3. Simulating an Attack on File B (Hacker changes Auth to Disabled)
    print("\n⚠️ [Simulating Cyber Attack] ...")
    hacked_b_content = "Config: Server_Port=8080, Auth=Disabled" # Modifying one word
    
    checker.verify_integrity("server_config.sys", hacked_b_content)

    print("\n" + "="*45)
    print("✅ Task 37 Complete: File Integrity Logic Verified.")
    print("="*45)
