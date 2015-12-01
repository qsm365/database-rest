from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
from .. import app

db = SQLAlchemy(app)

def get(uid):
    if uid:
        parameters = {}
        parameters['id'] = uid
        cmd = text("select * from db_jvm_bes_baseinfo where id = :id")
        result = db.engine.execute(cmd,parameters)
        row=result.first()
        return row

def save(uid,val):
    if uid:
        cmd1=text("delete from db_jvm_bes_baseinfo where id=:id")
        cmd2=text("insert into db_jvm_bes_baseinfo values (:id,:instance_name,:instance_basedir,:port,:app_context,:io_mode,:max_http_threads,:max_queued,:keepalive_timeout)")
        try:
            db.engine.execute(cmd1,id=uid)
            db.engine.execute(cmd2,val)
        except Exception,e:
            print e