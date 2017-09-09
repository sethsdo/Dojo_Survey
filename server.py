from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

dev = True

@app.route('/')
def my_portfolio():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def create_info():
    print "Got user info"
    print request.form['name']
    print request.form['location']
    print request.form['language'] 
    print request.form['comment']
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/about')

@app.route('/about')
def show_user():
    print "Got user info"
    print session['name']
    print session['location']
    print session['language'] 
    print session['comment']
    return render_template('about.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])

@app.route('/back', methods=['GET'])
def back():
    return render_template('index.html')

app.run(debug=dev)