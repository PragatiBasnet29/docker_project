from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.environ['POSTGRES_HOST']
DB_NAME = os.environ['POSTGRES_DB']
DB_USER = os.environ['POSTGRES_USER']
DB_PASS = os.environ['POSTGRES_PASSWORD']

def get_connection():
    return psycopg2.connect(
        host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
    )

@app.route('/add', methods=['POST'])
def add_name():
    name = request.json.get('name')
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS names (id serial PRIMARY KEY, name text NOT NULL);")
            cur.execute("INSERT INTO names (name) VALUES (%s);", (name,))
    conn.close()
    return jsonify({'status': 'name added', 'name': name})

@app.route('/names', methods=['GET'])
def get_names():
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM names;")
            names = [row[0] for row in cur.fetchall()]
    conn.close()
    return jsonify({'names': names})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
