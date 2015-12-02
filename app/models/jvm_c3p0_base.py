from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
from app import db

def get(uid):
    if uid:
        parameters = {}
        parameters['id'] = uid
        cmd = text("select * from db_jvm_c3p0_baseinfo where id = :id")
        result = db.engine.execute(cmd,parameters)
        row=result.first()
        return row

def save(uid,val):
    if uid:
        cmd1=text("delete from db_jvm_c3p0_baseinfo where id=:id and name=:name")
        cmd2=text("insert into db_jvm_c3p0_baseinfo values (:id,:name,:initial_pool_size,:max_pool_size,:min_pool_size)")
        try:
            db.engine.execute(cmd1,id=uid,name=val['name'])
            db.engine.execute(cmd2,val)
        except Exception,e:
            print e
