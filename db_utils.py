import yaml
import pyodbc
import os
from pathlib import Path

class DatabaseConnector:
    def _select_driver(self):
        """Pick an available SQL Server ODBC driver, preferring newer ones."""
        try:
            available = set(pyodbc.drivers())
        except Exception as e:
            print(f"Error enumerating ODBC drivers: {e}")
            return None

        preferred = [
            "ODBC Driver 18 for SQL Server",
            "ODBC Driver 17 for SQL Server",
            "SQL Server",
        ]
        for name in preferred:
            if name in available:
                return name
        print(f"No preferred SQL Server ODBC driver found. Available: {sorted(available)}")
        return None
    def read_yaml(self):
        base_dir = Path(__file__).resolve().parent
        cred_path = base_dir / 'db_cred.yaml'
        try:
            with open(cred_path, 'r', encoding='utf-8') as file:
                credentials = yaml.safe_load(file)
                if not isinstance(credentials, dict):
                    print(f"Error: db_cred.yaml did not contain a mapping at {cred_path}")
                    return None
                return credentials
        except FileNotFoundError:
            print(f"Error: db_cred.yaml not found at {cred_path}")
            return None
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file at {cred_path}: {e}")
            return None
    
    def create_connection(self):
        credentials = self.read_yaml()
        if credentials is None:
            return None
        
        server = credentials.get("server")
        database = credentials.get("database")
        username = credentials.get("username")
        password = credentials.get("password")

        if not all([server, database, username, password]):
            print("Error: Missing database credentials in YAML file.")
            return None
        try:
            driver = self._select_driver()
            if not driver:
                return None

            conn_str = (
                f"DRIVER={{{driver}}};"
                f"SERVER={server};"
                f"DATABASE={database};"
                f"UID={username};"
                f"PWD={password};"
                f"TrustServerCertificate=Yes;"
                f"Connection Timeout=5;"
            )
            connection  = pyodbc.connect(conn_str)
            return connection
        except pyodbc.Error as e:
            print(f"Database connection error: {e}")
            print("Please verify server, database, user, password, and ODBC driver.")
            print(f"Attempted server='{server}', database='{database}', user='{username}', driver='{driver}'")
            return None
