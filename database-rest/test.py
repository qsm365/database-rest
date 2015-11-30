from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from _mysql import result

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://cmdb:cmdb@localhost/cmdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/test', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        result = db.engine.execute("select 'test' from dual")
        for row in result:
            for item in row:
                print item
        return "ECHO: GET\n"

if __name__ == '__main__':
    app.run()