from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)

from user import User

@app.route('/')
def home():
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def create():
    User.create(request.form)
    return redirect("/view")

@app.route('/view')
def view():
    users = User.read()
    return render_template("view.html", users = users)


if __name__=="__main__": 
    app.run(debug=True) 