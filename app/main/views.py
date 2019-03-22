# _*_ coding:utf-8 _*_
from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from . import main
from .. import db


@main.route('/shutdown')
def server_shutdown():
    # if not current_app.testing:
    #    abort(404)
    shutdown = request.environ.get('werkzeug.server.shutdown')
    if not shutdown:
        abort(500)
    shutdown()
    return 'Shutting down...'


@main.route('/index', methods=['GET'])
def index():
    return index_main()


@main.route('/', methods=['GET'])
def index_main():
    """主界面"""
    return render_template('index.html')


@main.route('/rpt/<int:rpt_id>', methods=['GET'])
def get_report_by_id(rpt_id):
    print("You're requesting for report of ID " + str(rpt_id))
    if rpt_id in (1, 3, ):
        return render_template('reports/daily_dev.html')
    else:
        abort(404)
