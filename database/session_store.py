import sqlite3
from datetime import datetime
class SessionStore:


    def __init__(self): 
        self.conn = sqlite3.connect('repsense.db') 
        self.cursor = self.conn.cursor() 
        self._create_table()


    def _create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id INTEGER,
            exercise  TEXT,
            reps      INTEGER,
            feedback  TEXT,
            timestamp TEXT
        )
    """)
        self.conn.commit()
        
    def save_session(self, person_id, exercise, reps, feedback):
        timestamp = datetime.now().isoformat()
        self.cursor.execute("""INSERT INTO sessions (person_id, exercise, reps, feedback, timestamp)
        VALUES (?, ?, ?, ?, ?)""" , (person_id, exercise, reps, feedback, timestamp))
        self.conn.commit()