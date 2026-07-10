import json
import os
import sqlite3 as sql

STORAGE_DB = 'storage.db'
ASSETS_DB = 'assets.db'
CONFIG_FILE = 'user_config.json'

VERSION = '1.3'


def safe_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        raise SystemExit(0)


def init_db(db_name=STORAGE_DB):
    print("\nDatabase is being initialized...")
    conn = sql.connect(db_name)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS storage (
        id INTEGER PRIMARY KEY,
        amount REAL,
        category TEXT,
        type TEXT,
        created_at TEXT
    )
    """)
    conn.commit()
    return conn


def init_assets_db(db_name=ASSETS_DB):
    print("\nDatabase is being intialized...")
    conn = sql.connect(db_name)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS assets (
        id INTEGER PRIMARY KEY,
        name TEXT,
        asset_type TEXT,
        amount REAL,
        created_at TEXT
    )
    """)
    conn.commit()
    return conn


def load_user_name(config_file=CONFIG_FILE):
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            name = data.get('name')
            if name and isinstance(name, str):
                return name
        except Exception:
            return None
    return None


def save_user_name(name, config_file=CONFIG_FILE):
    try:
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump({'name': name}, f)
        return True
    except Exception:
        return False
