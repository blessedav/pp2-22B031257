import psycopg2 as ps

conn = ps.connect(host = 'localhost',
                  database = 'phone_book2',
                  user = 'postgres',
                  password = 'admin',
                  port = '5432'
)

cur = conn.cursor()

cur.execute('''
    CREATE TABLE phonebook(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL
    );
''')

conn.commit()

cur.close()
conn.close()