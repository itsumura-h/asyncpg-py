import asyncio
import asyncpg
from inspect import getmembers
from pprint import pprint

async def main():
    conn = await asyncpg.connect(
        user='benchmarkdbuser',
        password='benchmarkdbpass',
        database='hello_world',
        host='pg'
    )
    print('======')
    print(conn)
    rows = await conn.fetch('SELECT * FROM world')
    print(rows[0])
    print(rows[0]['id'])
    print(rows[0]['randomnumber'])
    await conn.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
