from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


previous_messages = {}

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')

    valid_users = {
        'Shamaiem': '123',
        'Maryam': '456',
        'Zainab': '789'
    }

    if username in valid_users and password == valid_users[username]:
        return render_template('dashboard.html', user=username, msgDic=previous_messages)
    else:
        return 'You are not allowed here!'


@app.route('/msgSubmit', methods=['POST'])
def msgSubmit():
    userName = request.form.get('name')
    userMessage = request.form.get('message')

   
    previous_messages[userName] = userMessage

    return render_template('dashboard.html', msgDic=previous_messages)


if __name__ == '__main__':
    app.run(debug=True)
