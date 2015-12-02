from flask import request,jsonify,Blueprint
from models import jvm_base,jvm_bes_base,jvm_tomcat_base,jvm_c3p0_base,jvm_monitor,jvm_bes_monitor,jvm_tomcat_monitor,jvm_c3p0_monitor
from . import app

profile = Blueprint('profile', __name__)

@app.route('/jvm/<uid>', methods = ['GET', 'POST'])
def api_jvm_base(uid):
    if request.method == 'GET':
        return jsonify(jvm_base.get(uid))
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            val=request.json
            jvm_base.save(uid,val)
            return "ok",201

@app.route('/jvm/<uid>/bes', methods = ['GET', 'POST'])
def api_jvm_bes_base(uid):
    if request.method == 'GET':
        return jsonify(jvm_bes_base.get(uid))
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            val=request.json
            jvm_bes_base.save(uid,val)
            return "ok",201

@app.route('/jvm/<uid>/tomcat', methods = ['GET', 'POST'])
def api_jvm_tomcat_base(uid):
    if request.method == 'GET':
        return jsonify(jvm_tomcat_base.get(uid))
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            val=request.json
            uid=val['id']
            jvm_tomcat_base.save(uid,val)
            return "ok",201

@app.route('/jvm/<uid>/c3p0', methods = ['GET', 'POST'])
def api_jvm_c3p0_base(uid):
    if request.method == 'GET':
        return jsonify(jvm_c3p0_base.get(uid))
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            val=request.json
            uid=val['id']
            jvm_c3p0_base.save(uid,val)
            return "ok",201

@app.route('/jvm/<uid>/monitor', methods = ['GET', 'POST'])
def api_jvm_monitor(uid):
    if request.method == 'GET':
        return jsonify(jvm_monitor.get(uid))
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            val=request.json
            uid=val['id']
            jvm_monitor.save(uid,val)
            return "ok",201

@app.route('/jvm/<uid>/bes/monitor', methods = ['GET', 'POST'])
def api_jvm_bes_monitor(uid):
    if request.method == 'GET':
        return jsonify(jvm_bes_monitor.get(uid))
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            val=request.json
            uid=val['id']
            jvm_bes_monitor.save(uid,val)
            return "ok",201

@app.route('/jvm/<uid>/tomcat/monitor', methods = ['GET', 'POST'])
def api_jvm_tomcat_monitor(uid):
    if request.method == 'GET':
        return jsonify(jvm_tomcat_monitor.get(uid))
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            val=request.json
            uid=val['id']
            jvm_tomcat_monitor.save(uid,val)
            return "ok",201

@app.route('/jvm/<uid>/c3p0/monitor', methods = ['GET', 'POST'])
def api_jvm_c3p0_monitor(uid):
    if request.method == 'GET':
        return jsonify(jvm_c3p0_monitor.get(uid))
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            val=request.json
            uid=val['id']
            jvm_c3p0_monitor.save(uid,val)
            return "ok",201
