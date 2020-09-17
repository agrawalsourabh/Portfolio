from flask import Blueprint, render_template

workBP = Blueprint('workBP', __name__)

@workBP.route('/works')
def works():
    return render_template('Works.html')