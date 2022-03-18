from flask import Flask

n = open("C:\Users\Aleli\OneDrive - Estudiantes ITCR\S I 2021\Taller I\Progras semanales\week03.py")
app = Flask(__name__)

@app.route('/') #@app.route('') to define route
def home():
    return n