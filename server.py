from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'commit often'

@app.route('/counter')
def counter():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else: 
        session['visits'] = 1
    return "{}".format(session.get('visits'))


@app.route('/')
def view_counter():
    return render_template("index.html", session=session)




#def contact():
    if request.method == 'POST':
        if request.form['add'] == session['counter'] +2:
            pass
        elif request.form['reset'] == session['counter'] - session['counter'] +1:
            pass

        elif request.method == 'GET':
            return render_template('contact.html', form=form)


if __name__=="__main__":
    app.run(debug=True)