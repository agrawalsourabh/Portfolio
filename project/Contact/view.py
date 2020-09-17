from flask import Blueprint, render_template

contactBP = Blueprint('contactBP', __name__)

@contactBP.route('/contact')
def contact():
    return render_template('contact.html')