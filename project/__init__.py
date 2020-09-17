from flask import Flask

app = Flask(__name__)


from project.Home.view import homeBP
app.register_blueprint(homeBP)

from project.Works.view import workBP
app.register_blueprint(workBP)

from project.AboutMe.view import  aboutBP
app.register_blueprint(aboutBP)

from project.Contact.view import contactBP
app.register_blueprint(contactBP)