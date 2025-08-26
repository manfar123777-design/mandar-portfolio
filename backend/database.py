Perfect! 🎉 Now let's add the `backend/database.py` file - this handles your MongoDB connection:
Action: file_editor view /app/backend/database.py
Observation: /app/backend/database.py:
1|from motor.motor_asyncio import AsyncIOMotorClient
2|import os
3|from typing import Optional
4|
5|class Database:
6|    client: Optional[AsyncIOMotorClient] = None
7|    database = None
8|
9|db = Database()
10|
11|async def get_database():
12|    return db.database
13|
14|async def connect_to_mongo():
15|    """Create database connection"""
16|    mongo_url = os.environ.get('MONGO_URL')
17|    db_name = os.environ.get('DB_NAME', 'portfolio')
18|    
19|    db.client = AsyncIOMotorClient(mongo_url)
20|    db.database = db.client[db_name]
21|    
22|    # Test the connection
23|    try:
24|        await db.client.admin.command('ismaster')
25|        print(f"Connected to MongoDB: {db_name}")
26|    except Exception as e:
27|        print(f"Failed to connect to MongoDB: {e}")
28|        raise e
29|
30|async def close_mongo_connection():
31|    """Close database connection"""
32|    if db.client:
33|        db.client.close()
34|        print("Disconnected from MongoDB")
35|
36|# Collection names
37|COLLECTIONS = {
38|    "personal_info": "personal_info",
39|    "experiences": "experiences", 
40|    "projects": "projects",
41|    "testimonials": "testimonials",
42|    "contact_messages": "contact_messages"
43|}

