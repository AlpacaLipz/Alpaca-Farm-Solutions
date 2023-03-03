from flask_app import app
from flask import render_template, request, redirect
from flask_app.template_model import Dojo


@app.route('/')
def index():
    return render_template('create.html')