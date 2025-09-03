from app import app, db
from flask import redirect, render_template, url_for, request #renderizar arquivo html
from app.forms import ContatoForm
from app.models import Contato

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/contato/", methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for("homepage"))
    return render_template("contato.html", form = form)

