import pymysql

try:
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='')
    cursor = connection.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS db_adoptme')
    print("Database db_adoptme berhasil dibuat atau sudah ada.")
    connection.close()
except Exception as e:
    print("Gagal membuat database:", e)
