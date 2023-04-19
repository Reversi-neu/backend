import pymysql

# DESIGN PATTERN: Singleton
class DB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.conn = pymysql.connect(
            host= 'db-mysql-nyc1-85325-do-user-13962965-0.b.db.ondigitalocean.com', 
            port = 25060,
            user = 'doadmin', 
            password = 'AVNS_v0OQGBVJBtwYNqGbtRs',
            db = 'defaultdb',       
        )
    
    # Calls the DB with a statement and data
    def callDB(self, statement, data):
        cursor = self.conn.cursor()
        cursor.execute(statement, data)
        rv = cursor.fetchall()
        self.conn.commit()
        cursor.close()
        return rv