from flask import Flask,render_template,url_for,redirect,Response,session,request
import random

app=Flask(__name__)

fortunes = [
    "Yes, but only if you believe.",
    "The stars are unclear right now.",
    "Absolutely not.",
    "Without a doubt.",
    "Ask again after a nap.",
    "The universe says maybe.",
    "Flask cannot decide your fate.",
    "It is certain.",
    "Doubt it.",
    "Your destiny awaits... just not today."
]


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit',methods=['POST'])
def submit():
    if request.method=='POST':
        question=request.form.get('question')
        answer=random.choice(fortunes)
        return render_template('ans.html',question=question,answer=answer)
    
    
    
    
if __name__=='__main__':
    app.run(debug=True)