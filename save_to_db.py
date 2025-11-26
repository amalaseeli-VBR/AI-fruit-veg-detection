from db_utils import DatabaseConnector
import pyodbc

db = DatabaseConnector()

def save_detected_product(json_txt):
    connection = db.create_connection()
    if connection is None:
        print("Warning: Database connection not established. Skipping save.")
        return
    try:
        cursor = None
        cursor = connection.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = 'AITransaction'
        """)

        if cursor.fetchone()[0] == 0:
            cursor.execute("""
            CREATE TABLE AITransaction (
                AIJsonTxt NVARCHAR(MAX) NOT NULL
            )
            """)
            cursor.execute("INSERT INTO AITransaction (AIJsonTxt) VALUES (?)", (json_txt,))
            connection.commit()
        else:
            cursor.execute("SELECT COUNT(*) FROM AITransaction")
            row_count = cursor.fetchone()[0]
            if row_count == 0:
                cursor.execute("INSERT INTO AITransaction (AIJsonTxt) VALUES (?)", (json_txt,))
            else:
                cursor.execute("UPDATE TOP (1) AITransaction SET AIJsonTxt = ?", (json_txt,))
            connection.commit()
    except pyodbc.Error as e:
        print(f"Error: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


def clear_database():
    connection = db.create_connection()
    if connection is None:
        print("Warning: Database connection not established. Skipping clear.")
        return
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
            IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'AITransaction')
            BEGIN
                CREATE TABLE AITransaction (AIJsonTxt NVARCHAR(MAX) NOT NULL);
                INSERT INTO AITransaction (AIJsonTxt) VALUES ('[]');
            END
            ELSE IF EXISTS (SELECT 1 FROM AITransaction)
                UPDATE TOP (1) AITransaction SET AIJsonTxt = '[]';
            ELSE
                INSERT INTO AITransaction (AIJsonTxt) VALUES ('[]');
        """)
        connection.commit()
    except pyodbc.Error as e:
        print(f"Error clearing DB payload: {e}")
    finally:
        if cursor:
            cursor.close()
        connection.close()

    
