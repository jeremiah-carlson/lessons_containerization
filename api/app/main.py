from fastapi import FastAPI, Request, Response
import uvicorn
import psycopg2
import random
 
first = ["Bob", "Fred", "Jim", "Leopold"]
last = ["Ross", "Rogers", "Henson", "Stokowski"]

app = FastAPI()

conn = psycopg2.connect(
            database="main",
            user="admin",
            password="test",
            host="demo_db", # demo_db
            port=5432
        )

# DB Setup 
with conn.cursor() as crs:
    crs.execute("""
        create table if not exists public.test (
            name text,
            id smallint
        );
        """)
    
    crs.execute("""
        insert into public.test values (%s, %s); 
        """, (f"{random.choice(first)} {random.choice(last)}", random.randint(1,1_000)))
    
    conn.commit()

@app.get('/')
def read_root(req: Request, resp: Response):
    with conn.cursor() as crs:
        crs.execute("select * from public.test;")
        data = crs.fetchall()
    return set(data)

@app.post('/')
def read_root(req: Request, resp: Response):
    with conn.cursor() as crs:
        user = f"{random.choice(first)} {random.choice(last)}"
    
        crs.execute("""
            insert into public.test values (%s, %s); 
            """, (user, random.randint(1,1_000)))
        
        conn.commit()
    return user


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=80,
        )