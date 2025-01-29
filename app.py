import mysql.connector
from mysql.connector import Error
from flask import Flask, jsonify
app = Flask(_name_)

# Database connection configuration

def get_db_connection():
    try:
        connection = mysql.connector.connect(
    host='database-2.cvdogignyyo9.us-east-1.rds.amazonaws.com'
,
    user='admin',
    password='12345678',
    database='database-2',
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
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM your_table_name")  # Replace 'your_table' with your actual table name
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(rows)
    else:
        return jsonify({"error": "Failed to connect to the database."}), 500

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=80,debug=True)