import mysql.connector
from mysql.connector import Error
from flask import Flask, jsonify

app = Flask(__name__)

# Database connection configuration
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='database-2.cvdogignyyo9.us-east-1.rds.amazonaws.com',
            user='admin',
            password='12345678',
            database='database_2',  # Ensure correct database name
            ssl_disabled=True  # Disable SSL
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM your_table_name")  # Replace with your actual table name
            rows = cursor.fetchall()
            return jsonify(rows)
        except Error as e:
            print(f"Error while fetching data: {e}")
            return jsonify({"error": "Failed to fetch data"}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        return jsonify({"error": "Failed to connect to the database"}), 500

if __name__ == '__main__':  # Fixed the main block
    app.run(host='0.0.0.0', port=80, debug=True)
