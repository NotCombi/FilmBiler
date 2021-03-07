from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biler.sqlite3'

db = SQLAlchemy(app)


class biler(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    primær = db.Column('primær', db.String(50))
    sekundær = db.Column('sekundær', db.String(50))
    merke = db.Column('merke', db.String(100))
    modell = db.Column('modell', db.String(100))
    bilde = db.Column('bilde', db.String(255))
    film = db.Column('film', db.String(100))
    filmår = db.Column('filmår', db.Integer)


def __init__(self, primær, sekundær, merke, modell, bilde, film, filmår):
    self.primær = primær
    self.sekundær = sekundær
    self.merke = merke
    self.modell = modell
    self.bilde = bilde
    self.film = film
    self.filmår = filmår


@app.route('/')
def index():
    biler = db.engine.execute(
        'SELECT * FROM biler ORDER BY filmår DESC LIMIT 4')
    return render_template('index.html', biler=biler)


@app.route('/liste/<sorter>')
def liste(sorter):
    biler = db.engine.execute(
        f'SELECT * FROM biler ORDER BY {sorter} ASC')
    return render_template('liste.html', biler=biler)


@app.route('/liste/enkel')
def enkel():
    return render_template('enkel.html', biler=biler)


@app.route('/om')
def om():
    return render_template('om.html')


app.run(debug=True)
