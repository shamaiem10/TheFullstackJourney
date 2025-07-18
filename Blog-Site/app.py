from flask import Flask, request, render_template

app = Flask(__name__)

# Use a list to store posts
content = []

@app.route('/')
def home():
    return render_template('home.html', contentPages=content)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        title = request.form.get('title')
        post_content = request.form.get('content')
        # Save each post as a dictionary
        content.append({'title': title, 'content': post_content})
        return render_template('home.html', contentPages=content)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
