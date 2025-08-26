import os
from dotenv import load_dotenv
from mysql.connector import pooling, Error

load_dotenv()  # reads .env

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "database": os.getenv("DB_NAME"),
}

pool = pooling.MySQLConnectionPool(pool_name="mainpool", pool_size=5, **DB_CONFIG)

def query_all(sql, params=None):
    conn = pool.get_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute(sql, params or ())
        rows = cur.fetchall()
        return rows
    finally:
        cur.close(); conn.close()

def execute(sql, params=None):
    conn = pool.get_connection()
    try:
        cur = conn.cursor()
        cur.execute(sql, params or ())
        conn.commit()
        return cur.lastrowid, cur.rowcount
    finally:
        cur.close(); conn.close()
