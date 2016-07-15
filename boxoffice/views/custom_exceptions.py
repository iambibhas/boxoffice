# -*- coding: utf-8 -*-

from .. import mail, app
from flask.ext.mail import Message
from flask import make_response, jsonify


class APIError(Exception):

    def __init__(self, message, status_code, response_message):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.response_message = response_message


@app.errorhandler(APIError)
def handle_api_error(error):
    msg = Message(subject='API Error', recipients=app.config['ADMINS'])
    msg.body = error.message
    mail.send(msg)
    return make_response(jsonify(message=error.response_message), error.status_code)
