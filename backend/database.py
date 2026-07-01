import sqlite3


class DisasterDatabase:

    def __init__(self):

        self.connection = sqlite3.connect(
            "disaster.db",
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS incidents(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            disaster TEXT,

            latitude REAL,

            longitude REAL,

            ambulance TEXT,

            hospital TEXT,

            eta INTEGER,

            distance REAL,

            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP

        )

        """)

        self.connection.commit()

    def save_incident(

        self,

        disaster,

        latitude,

        longitude,

        ambulance,

        hospital,

        eta,

        distance

    ):

        self.cursor.execute("""

        INSERT INTO incidents(

            disaster,

            latitude,

            longitude,

            ambulance,

            hospital,

            eta,

            distance

        )

        VALUES(?,?,?,?,?,?,?)

        """,

        (

            disaster,

            latitude,

            longitude,

            ambulance,

            hospital,

            eta,

            distance

        )

        )

        self.connection.commit()

    def get_all_incidents(self):

        self.cursor.execute("""

        SELECT *

        FROM incidents

        ORDER BY id DESC

        """)

        rows = self.cursor.fetchall()

        data = []

        for row in rows:

            data.append({

                "id": row[0],

                "disaster": row[1],

                "latitude": row[2],

                "longitude": row[3],

                "ambulance": row[4],

                "hospital": row[5],

                "eta": row[6],

                "distance": row[7],

                "timestamp": row[8]

            })

        return data

    def total_incidents(self):

        self.cursor.execute("""

        SELECT COUNT(*)

        FROM incidents

        """)

        return self.cursor.fetchone()[0]

    def disaster_statistics(self):

        self.cursor.execute("""

        SELECT disaster,

        COUNT(*)

        FROM incidents

        GROUP BY disaster

        """)

        rows = self.cursor.fetchall()

        stats = {}

        for row in rows:

            stats[row[0]] = row[1]

        return stats