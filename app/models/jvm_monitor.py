from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
from app import db

def get(uid):
    if uid:
        parameters = {}
        parameters['id'] = uid
        cmd = text("select * from db_jvm_monitor where id = :id order by monitor_time desc")
        result = db.engine.execute(cmd,parameters)
        row=result.first()
        return row

def save(uid,val):
    if uid:
        cmd=text("insert into db_jvm_monitor values (:id,TO_DATE ('01/01/1970','MM/DD/YYYY')+:monitor_time/(1000*60*60*24)+8/24,:used_heap_mem,:used_nonheap_mem,:thread_count,:cpu_load,:class_count,:open_file_descriptor)")
        try:
            db.engine.execute(cmd,val)
        except Exception,e:
            print e
