import sqlite3


class DisasterDatabase:

    def __init__(self):

        self.connection = sqlite3.connect(
            "disaster.db",
            check_same_thread=False
        )

        self.create_tables()

    # ==========================================
    # Create Tables
    # ==========================================
    def create_tables(self):

        cursor = self.connection.cursor()

        cursor.execute("""

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

    # ==========================================
    # Save Incident
    # ==========================================
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

        cursor = self.connection.cursor()

        cursor.execute("""

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

    # ==========================================
    # Get All Incidents
    # ==========================================
    def get_all_incidents(self):

        cursor = self.connection.cursor()

        cursor.execute("""

        SELECT *

        FROM incidents

        ORDER BY id DESC

        """)

        rows = cursor.fetchall()

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

    # ==========================================
    # Total Incidents
    # ==========================================
    def total_incidents(self):

        cursor = self.connection.cursor()

        cursor.execute("""

        SELECT COUNT(*)

        FROM incidents

        """)

        return cursor.fetchone()[0]

    # ==========================================
    # Disaster Statistics
    # ==========================================
    def disaster_statistics(self):

        cursor = self.connection.cursor()

        cursor.execute("""

        SELECT disaster,

        COUNT(*)

        FROM incidents

        GROUP BY disaster

        """)

        rows = cursor.fetchall()

        stats = {}

        for row in rows:

            stats[row[0]] = row[1]

        return stats