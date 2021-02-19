from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biler.sqlite3'

db = SQLAlchemy(app)


class Biler(db.Model):
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
