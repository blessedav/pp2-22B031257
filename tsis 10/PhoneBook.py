import psycopg2
from config import config
import csv

#эта функция прописывает что csv файл будет открыть для чтения и все данные в нем будут считываться в нужном нам порядке в нужную таблицу в нашей базе данных
def open_csv(filename):
    with open(filename,'r') as f:
        reader = csv.reader(f,delimiter = ';')
        for row in reader:
            name,id,phone=row
            cur.execute(
                'INSERT INTO phone(name,id,phone) VALUES(%s,%s,%s)',
                (name,id,phone,)
            )
            conn.commit()
            print("data uploaded succesfully from",filename)
 
#прописываем функции в sql
sql_insert = '''
    INSERT INTO phone VALUES(%s, %s, %s);
'''

sql_delete_name = '''
    DELETE FROM phone WHERE name = %s;
'''

sql_update_phone = '''
    UPDATE phone SET phone = %s WHERE id = %s;
'''

sql_update_name = '''
    UPDATE phone SET name = %s WHERE id = %s;
'''

sql_query_all = '''
    SELECT * FROM phone;
'''

sql_query_by_name = '''
    SELECT * FROM phone WHERE name = %s;
'''

sql_query_by_phone = '''
    SELECT * FROM phone WHERE phone = %s;
'''

sql_query_by_id = '''
    SELECT * FROM phone WHERE id = %s;
'''



conn = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password = 'admin',
    database = 'phonebook',
    port = 5432
)

cur = conn.cursor()#создаем курсор который вызывает функции sql 

def create_table():#создаем таблицу в базе данных с нужными столбиками
    cur.execute(
        '''
        CREATE TABLE phone(
        name TEXT NOT NULL,
        id SERIAL PRIMARY KEY,
        phone TEXT NOT NULL
        );
        '''
    )

def insert_data():
    name = input('Input name: ')
    id = input('Input id: ')
    phone = input('Input number: ')

    cur.execute(sql_insert, (name, id, phone))

def delete_data():
    name = input('Enter name of user you want to delete: ')
    cur.execute(sql_delete_name, (name,))
def update_data():
    command = input('What do you want to change: ')
    id = input('Enter the id of the person to update: ')
    if command == 'phone':
        phone = input('Enter the new phone of the user: ')
        cur.execute(sql_update_phone, (phone, id))
    elif command == 'name':
        name = input('Enter new name of the user: ')
        cur.execute(sql_update_name, (name, id))
    else:
        print('Error')

def query_data():
    command = input('What kind of query you want to exectude? [all/name/phone]: ')
    if command == 'all':
        cur.execute(sql_query_all)
        print(cur.fetchall())
    elif command == 'name':
        cur.execute(sql_query_by_name)
        print(cur.fetchall())
    elif command == 'phone':
        cur.execute(sql_query_by_phone)
        print(cur.fetchall)
    else:
        print('Error')



action = int(input('0 - create db, 1 - insert data, 2 - delete data, 3 - query data, 4 - update data,5- open CSV: \n'))
if action == 0:
    create_table()
elif action == 1:
    insert_data()
elif action == 2:
    delete_data()
elif action == 3:
    query_data()
elif action == 4:
    update_data()
elif action == 5:
    open_csv('phone.csv')
else:
    print('error')


conn.commit()


cur.close()
conn.close()