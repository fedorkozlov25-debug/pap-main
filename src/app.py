from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import mysql.connector

app = Flask(__name__)
app.secret_key = "K7vN2_xQ9mT4pL8zW1cR6yH3jF0sD5aG-uE9bV2nM7kP4qX8tC1wZ6rY3hJ0fS5d"

def connect():
    cnx = mysql.connector.connect(
        host="185.114.247.43",
        port=3306,
        user="sch688_vvedenie",
        password="Qwerty123")
    return cnx

def close_connect(cnx):
    if cnx.is_connected():
        cnx.close()

@app.route('/user_register', methods=['POST'])
def user_register():
    req = request.get_json()
    password = req.get("password")
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
    cur = connect().cursor()
    cur.execute("""INSERT INTO 'users'(
                column1,column2,column3) 
                VALUES (value1,value2,value3,...)""")


@app.route("/")
def registration():
    return render_template('registration.html')

@app.route("/login")
def login():
    return render_template('login.html')

app.run()

