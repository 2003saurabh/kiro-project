from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'database-1.czc40uo2ay01.ap-south-1.rds.amazonaws.com'),
    'user': os.getenv('DB_USER', 'admin'),
    'password': os.getenv('DB_PASSWORD', 'Password@123'),
    'database': os.getenv('DB_NAME', 'app_db'),
    'port': int(os.getenv('DB_PORT', 3306))
}

def get_db_connection():
    return pymysql.connect(**DB_CONFIG)

@app.route('/api/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def add_item():
    data = request.get_json()
    name = data.get('name')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO items (name) VALUES (%s)', (name,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'message': 'Item added successfully'}), 201

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM items WHERE id = %s', (item_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'message': 'Item deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
