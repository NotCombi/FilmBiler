from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biler.sqlite3'

db = SQLAlchemy(app)


class Biler(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    primaer = db.Column('primaer', db.String(50))
    sekundaer = db.Column('sekundaer', db.String(50))
    merke = db.Column('merke', db.String(100))
    modell = db.Column('modell', db.String(100))
    bilde = db.Column('bilde', db.String(255))
    film = db.Column('film', db.String(100))
    filmaar = db.Column('filmaar', db.Integer)


def __init__(self, primaer, sekundaer, merke, modell, bilde, film, filmaar):
    self.primaer = primaer
    self.sekundaer = sekundaer
    self.merke = merke
    self.modell = modell
    self.bilde = bilde
    self.film = film
    self.filmaar = filmaar
