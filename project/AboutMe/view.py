from flask import Blueprint, render_template

aboutBP = Blueprint('aboutBP', __name__)

@aboutBP.route('/aboutme')
def aboutme():
    return render_template('about.html')