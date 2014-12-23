import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash


DATABASE = '/home/ali/simple/example.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])



@app.before_request
def before_request():
    g.db = connect_db()





def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db



@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def show_entries():
    #cur = g.db.execute('select id, name')
    cur = g.db.execute("select * from test")
    myrows = g.db.execute("select * from test")
    for row in myrows:
	print row
    entries = [dict(title=str(row[0]), text1=str(row[1]), text2=str(row[2]), text3=str(row[3]), text4=str(row[4]), text5=str(row[5]), text6=str(row[6]) ) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)
    #entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    #return (str(row))



if __name__ == '__main__':
    app.run()
