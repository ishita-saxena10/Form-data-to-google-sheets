from os import access
from flask import Flask, Response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import val


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:{0}@localhost:5432/Atlan".format(val)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)



class Form(db.Model):
    user_id = db.Column(db.Integer,nullable=False)
    id = db.Column(db.Integer,primary_key=True)
    form_category = db.Column(db.String(100),nullable=False)
    question_no = db.Column(db.Integer,nullable=False)
    answer_no = db.Column(db.Integer,nullable=False)
    user_name = db.Column(db.String(100),nullable=False)
    phone_number = db.Column(db.String(100))

class FormResponse(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    form_id = db.Column(db.Integer,nullable=False)
    questions = db.Column(db.String(100),nullable=False)
    answers = db.Column(db.String(100),nullable=False)




