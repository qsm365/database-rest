from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
from .. import app

db = SQLAlchemy(app)

def get(uid):
    if uid:
        parameters = {}
        parameters['id'] = uid
        cmd = text("select * from db_jvm_c3p0_monitor where id = :id order by monitor_time desc")
        result = db.engine.execute(cmd,parameters)
        row=result.first()
        return row

def save(uid,val):
    if uid:
        cmd=text("insert into db_jvm_c3p0_monitor values (:id,TO_DATE ('01/01/1970','MM/DD/YYYY')+:monitor_time/(1000*60*60*24)+8/24,:name,:num_connections,:num_busy_connections,:thread_pool_size,:thread_pool_num_idle_threads)")
        try:
            db.engine.execute(cmd,val)
        except Exception,e:
            print e