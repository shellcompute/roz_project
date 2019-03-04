# _*_ coding:utf-8 _*_
from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from . import main
from .. import db


@main.route('/shutdown')
def server_shutdown():
    if not current_app.testing:
        abort(404)
    shutdown = request.environ.get('werkzeug.server.shutdown')
    if not shutdown:
        abort(500)
    shutdown()
    return 'Shutting down...'


@main.route('/', methods=['GET'])
def index():
    """主界面"""
    return render_template('index.html')
