from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas/new')
def ninjas_new():
    dojos = Dojo.get_all()
    return render_template("ninja.html", dojos = dojos)

@app.route("/ninjas/create", methods=["POST"])
def ninja_create():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    Ninja.create(data)
    return redirect('/dojos')