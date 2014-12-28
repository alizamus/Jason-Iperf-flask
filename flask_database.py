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
	return render_template('start_page.html')

@app.route('/result_row')
def test_entries():
    #cur = g.db.execute('select id, name')
    cur = g.db.execute("select * from test")
    entries = [dict(title=str(row[0]), text1=str(row[1]), text2=str(row[2]), text3=str(row[3]), text4=str(row[4]), text5=str(row[5]), text6=str(row[6]), text7=str(row[7]), text8=str(row[8]), text9=str(row[9]), text10=str(row[10]), text11=str(row[11]), text12=str(row[12]), text13=str(row[13]), text14=str(row[14]), text15=str(row[15]), text16=str(row[16]), text17=str(row[17]), text18=str(row[18]), text19=str(row[19]), text20=str(row[20]), text21=str(row[21]), text22=str(row[22]), text23=str(row[23]), text24=str(row[24]), text25=str(row[25]), text26=str(row[26]), text27=str(row[27]), text28=str(row[28]), text29=str(row[29]), text30=str(row[30]), text31=str(row[31]), text32=str(row[32]), text33=str(row[33]), text34=str(row[34]), text35=str(row[35]), text36=str(row[36]), text37=str(row[37]), text38=str(row[38]), text39=str(row[39]), text40=str(row[40]), text41=str(row[41]), text42=str(row[42]), text43=str(row[43]), text44=str(row[44]), text45=str(row[45]), text46=str(row[46]), text47=str(row[47]), text48=str(row[48]), text49=str(row[49]), text50=str(row[50]), text51=str(row[51]), text52=str(row[52]), text53=str(row[53]), text54=str(row[54]), text55=str(row[55]), current_date_time= str(row[56])) for row in cur.fetchall()]
    return render_template('table.html', entries=entries)


@app.route('/result_column')
def test_entries2():
    #cur = g.db.execute('select id, name')
    cur = g.db.execute("select * from test")
    entries = [dict(title=str(row[0]), text1=str(row[1]), text2=str(row[2]), text3=str(row[3]), text4=str(row[4]), text5=str(row[5]), text6=str(row[6]), text7=str(row[7]), text8=str(row[8]), text9=str(row[9]), text10=str(row[10]), text11=str(row[11]), text12=str(row[12]), text13=str(row[13]), text14=str(row[14]), text15=str(row[15]), text16=str(row[16]), text17=str(row[17]), text18=str(row[18]), text19=str(row[19]), text20=str(row[20]), text21=str(row[21]), text22=str(row[22]), text23=str(row[23]), text24=str(row[24]), text25=str(row[25]), text26=str(row[26]), text27=str(row[27]), text28=str(row[28]), text29=str(row[29]), text30=str(row[30]), text31=str(row[31]), text32=str(row[32]), text33=str(row[33]), text34=str(row[34]), text35=str(row[35]), text36=str(row[36]), text37=str(row[37]), text38=str(row[38]), text39=str(row[39]), text40=str(row[40]), text41=str(row[41]), text42=str(row[42]), text43=str(row[43]), text44=str(row[44]), text45=str(row[45]), text46=str(row[46]), text47=str(row[47]), text48=str(row[48]), text49=str(row[49]), text50=str(row[50]), text51=str(row[51]), text52=str(row[52]), text53=str(row[53]), text54=str(row[54]), text55=str(row[55]), current_date_time= str(row[56])) for row in cur.fetchall()]
    return render_template('table_2.html', entries=entries)




if __name__ == '__main__':
    app.run()
