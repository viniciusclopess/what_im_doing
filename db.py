import mysql.connector

def insert(date, watch, answer):
    def connect():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="whatimdoing"
        )
    datetime = f'{date} {watch}'
    conn = connect()
    cursor = conn.cursor()
    sql = "INSERT INTO history (date, answer) VALUES (%s, %s)"
    values = (datetime, answer)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
