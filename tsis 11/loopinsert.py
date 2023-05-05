import psycopg2 as ps

sql = """
INSERT INTO phonebook VALUES(DEFAULT, %s, %s);
"""

conn = ps.connect(host = 'localhost',
                  dbname = 'phone_book2',
                  user = 'postgres',
                  password = 'admin',
                  port = '5432' 
)

cur = conn.cursor()


banned=[]
while True:
    print("Want to enter a person's data? yes/no")
    mode=input()
    if mode=="no":
        break
    person=input().split()
    if len(person)>2:
        banned.append(person)
        continue
    if not person[1].isdigit():
        banned.append(person)
        continue

    cur.execute(sql,(person))
    
conn.commit()


cur.close()
conn.close()