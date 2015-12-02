from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
from app import db

def get(uid):
    if uid:
        parameters = {}
        parameters['id'] = uid
        cmd = text("select * from db_jvm_tomcat_monitor where id = :id order by monitor_time desc")
        result = db.engine.execute(cmd,parameters)
        row=result.first()
        return row
    
def save(uid,val):
    if uid:
        cmd=text("insert into db_jvm_tomcat_monitor values (:id,TO_DATE ('01/01/1970','MM/DD/YYYY')+:monitor_time/(1000*60*60*24)+8/24,:http_total_threads,:http_busy_threads,:ajp_total_threads,:ajp_busy_threads,:session_active)")
        try:
            db.engine.execute(cmd,val)
        except Exception,e:
            print e
