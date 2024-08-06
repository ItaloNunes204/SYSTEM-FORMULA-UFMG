import os
from flask import Flask, render_template, redirect, request, session, flash
from flask_session import Session
from classes import *

caminho_templates = os.path.join(os.getcwd(), "templates")
caminho_static = os.path.join(os.getcwd(), "static")

app = Flask(__name__, template_folder=caminho_templates, static_folder=caminho_static)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = "teste_palavra_chave"
Session(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    if request.method == "POST":
        matricula = request.form.get("matricula")
        senha = request.form.get("senha")
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
