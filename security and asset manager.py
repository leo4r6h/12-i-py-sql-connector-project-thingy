import mysql.connector
from mysql.connector import Error
import sys

class SecurityManager:
    def __init__(self):
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'security_db'
        }
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(**self.db_config)
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                return True
        except Error as e:
            print(f"Error: {e}")
            return False

    def disconnect(self):
        if self.conn and self.conn.is_connected():
            self.cursor.close()
            self.conn.close()

    def add_asset(self):
        print("\n--- ADD ASSET ---")
        name = input("Name: ")
        type_ = input("Type: ")
        ip = input("IP Address: ")
        owner = input("Owner: ")
        query = "INSERT INTO assets (asset_name, asset_type, ip_address, owner) VALUES (%s, %s, %s, %s)"
        try:
            self.cursor.execute(query, (name, type_, ip, owner))
            self.conn.commit()
            print("Asset Added.")
        except Error as e:
            print(f"Error: {e}")

    def report_vulnerability(self):
        print("\n--- REPORT VULN ---")
        self.view_assets()
        try:
            a_id = int(input("Asset ID: "))
            cve = input("CVE Code: ")
            desc = input("Description: ")
            sev = input("Severity (Low/Medium/High/Critical): ")
            query = "INSERT INTO vulnerabilities (asset_id, cve_code, description, severity) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (a_id, cve, desc, sev))
            self.conn.commit()
            print("Vulnerability Logged.")
        except Error as e:
            print(f"Error: {e}")

    def view_assets(self):
        self.cursor.execute("SELECT * FROM assets")
        for row in self.cursor.fetchall():
            print(row)

    def generate_report(self):
        print("\n--- RISK REPORT ---")
        query = """
        SELECT assets.asset_name, vulnerabilities.cve_code, vulnerabilities.severity 
        FROM assets 
        JOIN vulnerabilities ON assets.asset_id = vulnerabilities.asset_id
        """
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            print(f"Asset: {row[0]} | CVE: {row[1]} | Severity: {row[2]}")

def main():
    app = SecurityManager()
    if app.connect():
        while True:
            print("\n1. Add Asset\n2. Report Vuln\n3. Risk Report\n4. Exit")
            ch = input("Choice: ")
            if ch == '1': app.add_asset()
            elif ch == '2': app.report_vulnerability()
            elif ch == '3': app.generate_report()
            elif ch == '4': break
        app.disconnect()

if __name__ == "__main__":
    main()

    