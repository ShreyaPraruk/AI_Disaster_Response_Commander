import math


class AIEngine:

    def __init__(self):

        self.ambulances = [

            {
                "id": "A1",
                "lat": 12.9716,
                "lng": 77.5946,
                "available": True
            },

            {
                "id": "A2",
                "lat": 12.9810,
                "lng": 77.6050,
                "available": False
            },

            {
                "id": "A3",
                "lat": 12.9615,
                "lng": 77.5800,
                "available": True
            },

            {
                "id": "A4",
                "lat": 12.9500,
                "lng": 77.6100,
                "available": True
            }

        ]

        self.hospitals = [

            {
                "id": "H1",
                "lat": 12.9645,
                "lng": 77.5930,
                "capacity": 50,
                "occupied": 20
            },

            {
                "id": "H2",
                "lat": 12.9850,
                "lng": 77.6200,
                "capacity": 30,
                "occupied": 30
            },

            {
                "id": "H3",
                "lat": 12.9505,
                "lng": 77.5820,
                "capacity": 40,
                "occupied": 12
            },

            {
                "id": "H4",
                "lat": 12.9755,
                "lng": 77.5700,
                "capacity": 25,
                "occupied": 25
            }

        ]

    # ==========================================
    # Distance Calculation
    # ==========================================
    def distance(self, lat1, lon1, lat2, lon2):

        R = 6371

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)

        a = (

            math.sin(dlat / 2) ** 2 +

            math.cos(math.radians(lat1))

            *

            math.cos(math.radians(lat2))

            *

            math.sin(dlon / 2) ** 2

        )

        c = 2 * math.atan2(
            math.sqrt(a),
            math.sqrt(1 - a)
        )

        return R * c

    # ==========================================
    # Nearest Ambulance
    # ==========================================
    def nearest_ambulance(self, lat, lng):

        available = [

            a

            for a in self.ambulances

            if a["available"]

        ]

        nearest = min(

            available,

            key=lambda a:

            self.distance(

                lat,

                lng,

                a["lat"],

                a["lng"]

            )

        )

        return nearest

    # ==========================================
    # Nearest Hospital
    # ==========================================
    def nearest_hospital(self, lat, lng):

        available = [

            h

            for h in self.hospitals

            if h["occupied"] < h["capacity"]

        ]

        nearest = min(

            available,

            key=lambda h:

            self.distance(

                lat,

                lng,

                h["lat"],

                h["lng"]

            )

        )

        return nearest
       # ==========================================
    # Resources Required
    # ==========================================
    def resources(self, disaster):

        if disaster == "Fire":
            return {
                "ambulances": 1,
                "teams": 1
            }

        elif disaster == "Flood":
            return {
                "ambulances": 2,
                "teams": 3
            }

        elif disaster == "Earthquake":
            return {
                "ambulances": 3,
                "teams": 5
            }

        return {
            "ambulances": 1,
            "teams": 1
        }

    # ==========================================
    # Disaster Severity
    # ==========================================
    def severity(self, disaster):

        if disaster == "Fire":
            return "Medium"

        elif disaster == "Flood":
            return "High"

        elif disaster == "Earthquake":
            return "Critical"

        return "Low"

    # ==========================================
    # AI Confidence
    # ==========================================
    def confidence(self, distance):

        if distance < 2:
            return 98

        elif distance < 5:
            return 94

        return 88

    # ==========================================
    # AI Decision
    # ==========================================
    def make_decision(self, lat, lng, disaster):

        ambulance = self.nearest_ambulance(lat, lng)

        hospital = self.nearest_hospital(lat, lng)

        resources = self.resources(disaster)

        distance = self.distance(

            lat,

            lng,

            ambulance["lat"],

            ambulance["lng"]

        )

        eta = max(1, round(distance * 2))

        severity = self.severity(disaster)

        confidence = self.confidence(distance)

        reason = [

            f"Nearest available ambulance selected ({ambulance['id']})",

            f"Nearest available hospital selected ({hospital['id']})",

            f"{resources['ambulances']} ambulance(s) allocated",

            f"{resources['teams']} rescue team(s) allocated",

            f"Severity classified as {severity}"

        ]

        return {

            "ambulance": ambulance,

            "hospital": hospital,

            "resources": resources,

            "distance": round(distance, 2),

            "eta": eta,

            "severity": severity,

            "confidence": confidence,

            "reason": reason

        }