from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
from app import db

def get(uid):
    if uid:
        parameters = {}
        parameters['id'] = uid
        cmd = text("select * from db_jvm_baseinfo where id = :id")
        result = db.engine.execute(cmd,parameters)
        row=result.first()
        return row

def save(uid,val):
    if uid:
        cmd1=text("delete from db_jvm_baseinfo where id=:id")
        cmd2=text("insert into db_jvm_baseinfo values (:id,:os_name,:os_version,:os_arch,:total_phy_cpu,:total_phy_mem,:init_heap_mem,:max_heap_mem,:vm_name,:vm_version,:max_file_descriptor)")
        try:
            db.engine.execute(cmd1,id=uid)
            db.engine.execute(cmd2,val)
        except Exception,e:
            print e
