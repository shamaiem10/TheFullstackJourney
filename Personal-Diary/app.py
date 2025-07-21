from flask import Flask,render_template,url_for,request,redirect
import sqlite3

app=Flask(__name__)

def get_db_connection():
    conn=sqlite3.connect('data.db')
    conn.row_factory=sqlite3.Row
    return conn
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        conn = get_db_connection()
        title = request.form.get('title')
        content = request.form.get('content')
        date = request.form.get('date_created')
        
        conn.execute(
            'INSERT INTO diary(title, content, date_created) VALUES (?, ?, ?)',
            (title, content, date)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('home')) 

    conn = get_db_connection()
    entries = conn.execute('SELECT * FROM diary ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('home.html', entries=entries)


    

if __name__=='__main__':
    app.run(debug=True)
    