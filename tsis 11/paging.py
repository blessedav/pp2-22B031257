import psycopg2 as ps

sql = '''
SELECT * FROM phonebook;
'''

conn = ps.connect(host = 'localhost',
                  dbname = 'phone_book2',
                  user = 'postgres',
                  password = 'admin',
                  port = '5432' 
)

cur = conn.cursor()

print("Need offset? yes/no:")
mode=input()
if mode=="yes":
    print("Enter offset:")
    offset=int(input())
    sql+=" OFFSET {}".format(offset)
print("Need limit? yes/no:")
mode=input()
if mode=="yes":
    print("Enter limit:")
    limit=int(input())
    sql+=" LIMIT {}".format(limit)
sql +=";"
cur.execute(sql)
print(cur.fetchall())

    
conn.commit()


cur.close()
conn.close()