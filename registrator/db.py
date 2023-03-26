from config import DB_HOST, DB_PORT, DB_NAME, DB_USERNAME, DB_PASSWORD
import psycopg2
from datetime import datetime, timedelta


conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USERNAME,
    password=DB_PASSWORD
)      
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS all_users (name varchar(20) NOT NULL, surname varchar(20) NOT NULL, uuid varchar(30) NOT NULL, connection_date date NOT NULL, PRIMARY KEY (uuid))")
conn.commit()

#Добавляем пользователя в БД
def add_user(name: str, surname: str, uuid: str, connection_date):
    cursor.execute("INSERT INTO all_users (name, surname, uuid, connection_date) VALUES (%s, %s, %s, %s) ON CONFLICT (uuid) DO NOTHING", (name, surname, uuid, connection_date))
    conn.commit()