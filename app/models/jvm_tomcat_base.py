from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
from app import db

def get(uid):
    if uid:
        parameters = {}
        parameters['id'] = uid
        cmd = text("select * from db_jvm_tomcat_baseinfo where id = :id")
        result = db.engine.execute(cmd,parameters)
        row=result.first()
        return row

def save(uid,val):
    if uid:
        cmd1=text("delete from db_jvm_tomcat_baseinfo where id=:id")
        cmd2=text("insert into db_jvm_tomcat_baseinfo values (:id,:basedir,:http_io_mode,:ajp_io_mode,:max_http_threads,:max_ajp_threads,:http_port,:ajp_port,:http_keepalive_timeout,:app_context)")
        try:
            db.engine.execute(cmd1,id=uid)
            db.engine.execute(cmd2,val)
        except Exception,e:
            print e
