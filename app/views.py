from app import app
from flask import render_template
from .models import User, Events


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html',title ='My Main Page')