from flask import Blueprint, render_template

homeBP = Blueprint('homeBP', __name__)

@homeBP.route('/')
def index():
    return render_template('index.html')