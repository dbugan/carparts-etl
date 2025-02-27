import os 
import pandas as pd
import urllib.parse
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version(), inet_server_addr();"))  # PostgreSQL version check
        print(result.fetchone())  # Print database version
    print("Database connection successful!")
except Exception as e:
    print(f"Error connecting to database: {e}")
    