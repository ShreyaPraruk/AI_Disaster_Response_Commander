from flask import Blueprint, request, jsonify

from ai_engine import AIEngine
from database import DisasterDatabase

api = Blueprint("api", __name__)

engine = AIEngine()
database = DisasterDatabase()


# =====================================
# AI Dispatch
# =====================================
@api.route("/dispatch", methods=["POST"])
def dispatch():

    data = request.get_json()

    lat = data["lat"]
    lng = data["lng"]
    disaster = data["disaster"]

    result = engine.make_decision(
        lat,
        lng,
        disaster
    )

    database.save_incident(

        disaster,

        lat,

        lng,

        result["ambulance"]["id"],

        result["hospital"]["id"],

        result["eta"],

        result["distance"]

    )

    return jsonify(result)


# =====================================
# Incident History
# =====================================
@api.route("/history", methods=["GET"])
def history():

    return jsonify(

        database.get_all_incidents()

    )


# =====================================
# Dashboard Statistics
# =====================================
@api.route("/statistics", methods=["GET"])
def statistics():

    return jsonify({

        "total_incidents":

        database.total_incidents(),

        "disaster_statistics":

        database.disaster_statistics()

    })