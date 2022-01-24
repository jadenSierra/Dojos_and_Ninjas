from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def home():
    return redirect('/dojos')


@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("home.html", dojos = dojos)

@app.route('/dojos/create', methods = ['POST'])
def dojos_create():
    data = {
        'dname' : request.form['dname']
    }
    Dojo.create(data)
    return redirect("/")

@app.route('/dojos/show/<int:id>')
def dojos_show(id):
    data = {
        'id' : id
    }
    dojo = Dojo.get_ninjas_for_dojo(data)
    print(dojo.ninjas[0].first_name)
    return render_template("show.html", dojo = dojo)