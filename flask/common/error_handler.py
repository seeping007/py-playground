#!/usr/bin/python3

from flask import json


def error_response(_type, message):
    return json.dumps({
        "status": _type,
        "message": message
    })


def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return error_response("BAD_REQUEST", e.description), 400

    @app.errorhandler(404)
    def not_found(e):
        return error_response("NOT_FOUND", e.description), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return error_response("INTERNAL_SERVER_ERROR", e.description), 500
