#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import eventlet

eventlet.monkey_patch()
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from logzero import logger
from flask_socketio import SocketIO

app = Flask(__name__)

# # See http://flask.pocoo.org/docs/latest/config/
app.config.from_object(os.environ["APP_SETTINGS"])

# Setup cors headers to allow all domains
# https://flask-cors.readthedocs.io/en/latest/
CORS(app)

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
# async_mode = "eventlet"

socketio = SocketIO(
    app, cors_allowed_origins="*", transports=["websocket"]
)  # , async_mode=async_mode)


@app.route("/send_event", methods=["POST"])
def event_sender():
    params = request.get_json(force=True)
    logger.info("/event_sender/%s", params)
    if params.get("event") is None:
        return jsonify(
            {"message": "Please specify a event to be sent", "status_code": 202}
        )
    socketio.emit(params.get("event"), params.get("data"), broadcast=True)
    logger.info("Notification sent for event: %s", params["event"])
    data = {
        "message": "Event sent",
    }
    resp = jsonify(data)
    resp.status_code = 200
    return resp


if __name__ == "__main__":
    socketio.run(app, host=os.getenv("HOST", "0.0.0.0"), port=os.getenv("PORT", 8080))
