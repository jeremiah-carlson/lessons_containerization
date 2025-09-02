from fastapi import FastAPI, Request, Response
import uvicorn
import psycopg2
import random
import logging

logging.basicConfig(
    filename='./logs/my_application.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

 
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

logging.info("Database connetion established")

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

    logging.info("Database table test initialized")

@app.get('/')
def read_root(req: Request, resp: Response):
    with conn.cursor() as crs:
        crs.execute("select * from public.test;")
        data = crs.fetchall()
        logging.info("User records retrieved")
    return set(data)

@app.post('/')
def read_root(req: Request, resp: Response):
    with conn.cursor() as crs:
        user = f"{random.choice(first)} {random.choice(last)}"
    
        crs.execute("""
            insert into public.test values (%s, %s); 
            """, (user, random.randint(1,1_000)))
        
        conn.commit()
        
        logging.info(f"User record add: {user}")
    return user


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=80,
        )