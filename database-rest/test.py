from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
#app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://user:pass@oracle_host/oracle_sid'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 5

db = SQLAlchemy(app)

@app.route('/jvm_base', methods = ['GET', 'POST'])
def api_jvm_base():
    if request.method == 'GET':
        parameters = {}
        parameters['id'] = request.args['id']
        cmd = text("select * from db_jvm_baseinfo where id = :id")
        result = db.engine.execute(cmd,parameters)
        row=result.fetchone()
        result.close()
        return jsonify(row)
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            val=request.json
            uid=val['id']
            save_jvm_base(uid,val)
            return "ok"

@app.route('/jvm_bes_base', methods = ['GET', 'POST'])
def api_jvm_bes_base():
    if request.method == 'GET':
        parameters = {}
        parameters['id'] = request.args['id']
        cmd = text("select * from db_jvm_bes_baseinfo where id = :id")
        result = db.engine.execute(cmd,parameters)
        row=result.fetchone()
        result.close()
        return jsonify(row)
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            val=request.json
            uid=val['id']
            save_jvm_bes_base(uid,val)
            return "ok"

@app.route('/jvm_tomcat_base', methods = ['GET', 'POST'])
def api_jvm_tomcat_base():
    if request.method == 'GET':
        parameters = {}
        parameters['id'] = request.args['id']
        cmd = text("select * from db_jvm_tomcat_baseinfo where id = :id")
        result = db.engine.execute(cmd,parameters)
        row=result.fetchone()
        result.close()
        return jsonify(row)
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            val=request.json
            uid=val['id']
            save_jvm_tomcat_base(uid,val)
            return "ok"

@app.route('/jvm_c3p0_base', methods = ['GET', 'POST'])
def api_jvm_c3p0_base():
    if request.method == 'GET':
        parameters = {}
        parameters['id'] = request.args['id']
        cmd = text("select * from db_jvm_c3p0_baseinfo where id = :id")
        result = db.engine.execute(cmd,parameters)
        row=result.fetchone()
        result.close()
        return jsonify(row)
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            val=request.json
            uid=val['id']
            save_jvm_c3p0_base(uid,val)
            return "ok"

@app.route('/jvm_monitor', methods = ['GET', 'POST'])
def api_jvm_monitor():
    if request.method == 'GET':
        parameters = {}
        parameters['id'] = request.args['id']
        cmd = text("select * from db_jvm_monitor where id = :id order by monitor_time desc")
        result = db.engine.execute(cmd,parameters)
        row=result.fetchone()
        result.close()
        return jsonify(row)
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            val=request.json
            uid=val['id']
            save_jvm_monitor(uid,val)
            return "ok"

@app.route('/jvm_bes_monitor', methods = ['GET', 'POST'])
def api_jvm_bes_monitor():
    if request.method == 'GET':
        parameters = {}
        parameters['id'] = request.args['id']
        cmd = text("select * from db_jvm_bes_monitor where id = :id order by monitor_time desc")
        result = db.engine.execute(cmd,parameters)
        row=result.fetchone()
        result.close()
        return jsonify(row)
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            val=request.json
            uid=val['id']
            save_jvm_bes_monitor(uid,val)
            return "ok"

@app.route('/jvm_tomcat_monitor', methods = ['GET', 'POST'])
def api_jvm_tomcat_monitor():
    if request.method == 'GET':
        parameters = {}
        parameters['id'] = request.args['id']
        cmd = text("select * from db_jvm_tomcat_monitor where id = :id order by monitor_time desc")
        result = db.engine.execute(cmd,parameters)
        row=result.fetchone()
        result.close()
        return jsonify(row)
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            val=request.json
            uid=val['id']
            save_jvm_tomcat_monitor(uid,val)
            return "ok"

@app.route('/jvm_c3p0_monitor', methods = ['GET', 'POST'])
def api_jvm_c3p0_monitor():
    if request.method == 'GET':
        parameters = {}
        parameters['id'] = request.args['id']
        cmd = text("select * from db_jvm_c3p0_monitor where id = :id order by monitor_time desc")
        result = db.engine.execute(cmd,parameters)
        row=result.fetchone()
        result.close()
        return jsonify(row)
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            val=request.json
            uid=val['id']
            save_jvm_c3p0_monitor(uid,val)
            return "ok"

def save_jvm_base(uid,val):
    if uid:
        cmd1=text("delete from db_jvm_baseinfo where id=:id")
        cmd2=text("insert into db_jvm_baseinfo values (:id,:os_name,:os_version,:os_arch,:total_phy_cpu,:total_phy_mem,:init_heap_mem,:max_heap_mem,:vm_name,:vm_version,:max_file_descriptor)")
        try:
            db.engine.execute(cmd1,id=uid)
            db.engine.execute(cmd2,val)
        except Exception,e:
            print e
            
def save_jvm_bes_base(uid,val):
    if uid:
        cmd1=text("delete from db_jvm_bes_baseinfo where id=:id")
        cmd2=text("insert into db_jvm_bes_baseinfo values (:id,:instance_name,:instance_basedir,:port,:app_context,:io_mode,:max_http_threads,:max_queued,:keepalive_timeout)")
        try:
            db.engine.execute(cmd1,id=uid)
            db.engine.execute(cmd2,val)
        except Exception,e:
            print e

def save_jvm_tomcat_base(uid,val):
    if uid:
        cmd1=text("delete from db_jvm_tomcat_baseinfo where id=:id")
        cmd2=text("insert into db_jvm_tomcat_baseinfo values (:id,:basedir,:http_io_mode,:ajp_io_mode,:max_http_threads,:max_ajp_threads,:http_port,:ajp_port,:http_keepalive_timeout,:app_context)")
        try:
            db.engine.execute(cmd1,id=uid)
            db.engine.execute(cmd2,val)
        except Exception,e:
            print e

def save_jvm_c3p0_base(uid,val):
    if uid:
        cmd1=text("delete from db_jvm_c3p0_baseinfo where id=:id and name=:name")
        cmd2=text("insert into db_jvm_c3p0_baseinfo values (:id,:name,:initial_pool_size,:max_pool_size,:min_pool_size)")
        try:
            db.engine.execute(cmd1,id=uid,name=val['name'])
            db.engine.execute(cmd2,val)
        except Exception,e:
            print e

def save_jvm_monitor(uid,val):
    if uid:
        cmd=text("insert into db_jvm_monitor values (:id,TO_DATE ('01/01/1970','MM/DD/YYYY')+:monitor_time/(1000*60*60*24)+8/24,:used_heap_mem,:used_nonheap_mem,:thread_count,:cpu_load,:class_count,:open_file_descriptor)")
        try:
            db.engine.execute(cmd,val)
        except Exception,e:
            print e

def save_jvm_bes_monitor(uid,val):
    if uid:
        cmd=text("insert into db_jvm_bes_monitor values (:id,TO_DATE ('01/01/1970','MM/DD/YYYY')+:monitor_time/(1000*60*60*24)+8/24,:http_total_threads,:http_idle_threads,:http_busy_threads,:session_active,:queued)")
        try:
            db.engine.execute(cmd,val)
        except Exception,e:
            print e

def save_jvm_tomcat_monitor(uid,val):
    if uid:
        cmd=text("insert into db_jvm_tomcat_monitor values (:id,TO_DATE ('01/01/1970','MM/DD/YYYY')+:monitor_time/(1000*60*60*24)+8/24,:http_total_threads,:http_busy_threads,:ajp_total_threads,:ajp_busy_threads,:session_active)")
        try:
            db.engine.execute(cmd,val)
        except Exception,e:
            print e

def save_jvm_c3p0_monitor(uid,val):
    if uid:
        cmd=text("insert into db_jvm_c3p0_monitor values (:id,TO_DATE ('01/01/1970','MM/DD/YYYY')+:monitor_time/(1000*60*60*24)+8/24,:name,:num_connections,:num_busy_connections,:thread_pool_size,:thread_pool_num_idle_threads)")
        try:
            db.engine.execute(cmd,val)
        except Exception,e:
            print e

if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    app.run()