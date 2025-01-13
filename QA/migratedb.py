import psycopg2
from flask import g


def connect_db():
    sql=conn= psycopg2.connect(
    host ="localhost",
    dbname="flaskdb",
    user='postgres',
    password="root"
)
    conn.autocommit = True
    sql = conn.cursor()
    return conn, sql
def get_db():
    db = connect_db()

    if not hasattr(g, 'postgres_db_conn'):
        g.postgres_db_conn = db[0]

    if not hasattr(g, 'postgres_db_cur'):
        g.postgres_db_cur = db[1]

    return g.postgres_db_cur

def init_db():
    db = connect_db()

    db[1].execute(open('schema.sql', 'r').read())
    db[1].close()

    db[0].close()

def init_admin():
    db = connect_db()

    db[1].execute('update users set admin = True where name = %s', ('admin', ))

    db[1].close()
    db[0].close()
#     cur = conn.cursor()

#     cur.execute("""
# CREATE TABLE myuser (
#     id SERIAL PRIMARY KEY,
#     name TEXT NOT NULL,
#     password TEXT NOT NULL,
#     expert BOOLEAN NOT NULL,
#     admin BOOLEAN NOT NULL
# )
# """)

#     conn.commit()