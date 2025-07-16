from flask import Flask, request, session, Response, redirect, render_template, url_for


app=Flask(__name__)
app.secret_key = "key123"




@app.route("/", methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get('username')
        password=request.form.get('password')
        session['user']=username
        if username=='shamaiem' and password=='shamaiem':
            return redirect(url_for("welcome"))
        else:
            return Response("Wrong credentials!")
        
    return '''
    <form method="POST">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
'''
@app.route("/welcome")
def welcome():
    if 'user' in session:
         return f'''
            <h2>Hello, {session['user']}!</h2>
            <form action="/logout" method="get">
                <button type="submit">Logout</button>
            </form>
        '''
        
        
    else:
        return redirect(url_for(login))

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('login'))














if __name__=="__main__":
    app.run(debug=True)
