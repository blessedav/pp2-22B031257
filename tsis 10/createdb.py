import psycopg2 as ps

conn = ps.connect(host = 'localhost',
                  database = 'snake',
                  user = 'postgres',
                  password = 'admin',
                  port = '5432'
)

cur = conn.cursor()

cur.execute('''
    CREATE TABLE snake(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    score VARCHAR(255) NOT NULL,
    level VARCHAR(255) NOT NULL
    );
''')

conn.commit()

cur.close()
conn.close()