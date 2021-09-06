from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'commit often'

def counter():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else: 
        session['visits'] = 1

@app.route('/add')
def add():
    counter()
    return redirect('/')

@app.route('/')
def view_counter():
    counter()
    return render_template("index.html", session=session)

@app.route('/destroy_session')
def clear_counter():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)