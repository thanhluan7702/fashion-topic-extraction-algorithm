import sqlite3
import pandas as pd 

def create_table(cursor): 
    query = '''CREATE TABLE IF NOT EXISTS REVIEWS(
    category text,
    sub_category text,
    name_product text,
    star int, 
    title text, 
    comment text)'''
    
    cursor.execute(query)
    return

def create_table_cleaned(cursor): 
    query = '''CREATE TABLE IF NOT EXISTS REVIEWS_CLEANED(
    category text,
    sub_category text,
    name_product text,
    star int, 
    title text, 
    comment text,
    label text)'''
    
    cursor.execute(query)
    return

def insert_data(data, conn, cursor): 
    ## check 
    cursor.execute("SELECT * FROM REVIEWS WHERE title = ? and comment = ?", (data[2], data[3]))
    existing_record = cursor.fetchone()

    if existing_record is None: 
        query = "INSERT OR IGNORE INTO REVIEWS VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (data))
        conn.commit()
    return

def delete_table(conn, cursor, table_name): 
    cursor.execute(f"DELETE FROM {table_name};")
    conn.commit()
    conn.close()
    return

def init(): 
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    return conn, cursor

def extract_all_data(conn, cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    return cursor.fetchall()
    
def save_to_csv(data, namefile, data_type, conn, cursor): 
    if data_type == 'original': 
        columns = ['category', 'sub_category', 'name_product', 'star', 'title', 'comment']
    else: 
        columns = ['category', 'sub_category', 'name_product', 'star', 'title', 'comment', 'label']
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(f'{namefile}.csv', index=False)
    return

conn, cursor = init()
source = extract_all_data(conn, cursor, 'REVIEWS')
save_to_csv(source, 'data', 'original', conn, cursor)
cleaned = extract_all_data(conn, cursor, 'REVIEWS_CLEANED')
save_to_csv(cleaned, 'data_cleaned', 'cleaned', conn, cursor)