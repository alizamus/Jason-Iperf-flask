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
	return "begin"

@app.route('/test')
def test_entries():
    #cur = g.db.execute('select id, name')
    cur = g.db.execute("select * from test")
    myrows = g.db.execute("select * from test")
    for row in myrows:
	print row
    entries = [dict(title=str(row[0]), text1=str(row[1]), text2=str(row[2]), text3=str(row[3]), text4=str(row[4]), text5=str(row[5]), text6=str(row[6]), text7=str(row[7]), text8=str(row[8]), text9=str(row[9]), text10=str(row[10]), text11=str(row[11]), text12=str(row[12]), text13=str(row[13]), text14=str(row[14]), text15=str(row[15]), text16=str(row[16]), text17=str(row[17]), text18=str(row[18]), text19=str(row[19]), text20=str(row[20]), text21=str(row[21])) for row in cur.fetchall()]
    return render_template('table.html', entries=entries)
    #entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    #return (str(row))

@app.route('/test2')
def test_entries2():
    #cur = g.db.execute('select id, name')
    cur = g.db.execute("select * from test")
    myrows = g.db.execute("select * from test")
    for row in myrows:
	print row
    entries = [dict(title=str(row[0]), text1=str(row[1]), text2=str(row[2]), text3=str(row[3]), text4=str(row[4]), text5=str(row[5]), text6=str(row[6]), text7=str(row[7]), text8=str(row[8]), text9=str(row[9]), text10=str(row[10]), text11=str(row[11]), text12=str(row[12]), text13=str(row[13]), text14=str(row[14]), text15=str(row[15]), text16=str(row[16]), text17=str(row[17]), text18=str(row[18]), text19=str(row[19]), text20=str(row[20]), text21=str(row[21])) for row in cur.fetchall()]
    return render_template('table_2.html', entries=entries)
    #entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    #return (str(row))



if __name__ == '__main__':
    app.run()
