import pymysql

def connect_db():
    connection = None
    try:
        connection = pymysql.connect(
            host='localhost',
            user="root",
            password="root@",
            database='kavya_db',
            port=3306,
            charset="utf8"
        )
        print('Database Connected')
    except Exception as e:
        print('Database Connection Failed:', e)
    return connection

def disconnect_db(connection):
    try:
        connection.close()
        print('DB disconnected')
    except Exception as e:
        print('DB disconnection failed:', e)

def create_db():
    query = 'CREATE DATABASE IF NOT EXISTS kavya_db'
    try:
        
        connection = pymysql.connect(
            host='localhost',
            user="root",
            password="root@",
            port=3306,
            charset="utf8"
        )
        cursor = connection.cursor()
        cursor.execute(query)
        print('Database created')
        cursor.close()
        disconnect_db(connection)
    except Exception as e:
        print('Database creation failed:', e)

def create_table():
    query = '''
    CREATE TABLE IF NOT EXISTS employees (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        designation VARCHAR(30),
        phone_number BIGINT UNIQUE,
        salary FLOAT,
        commission FLOAT DEFAULT 0,
        years_of_experience TINYINT,
        technology VARCHAR(30) NOT NULL
    )
    '''
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print('Table created')
        cursor.close()
        disconnect_db(connection)
    except Exception as e:
        print('Table creation failed:', e)

def read_all_employees():
    query = 'SELECT * FROM employees'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()  
        for row in rows:
            print(row)
        print('All rows retrieved')
        cursor.close()
        disconnect_db(connection)
    except Exception as e:
        print('Rows retrieval failed:', e)


connection = connect_db()
create_table()
disconnect_db(connection)
