from flask import Flask, jsonify, abort, request
import mysql.connector as mysql
app = Flask(__name__)

#FLASK_APP="python_handin_template/flask/flask_week8.py"

db = mysql.connect(
    host = "db",
    user = "root",
    passwd = "root",
    db = "db"
)


@app.route('/api/laptops/all', methods=['GET'])
def get_laptops():
    cur = db.cursor()
    query = 'SELECT * from week8;'
    cur.execute(query)
    res = cur.fetchall()
    return jsonify(res)

@app.route('/api/laptops', methods=['POST'])
def post_laptop():
    if not request.json or not 'name' in request.json or not 'price' in request.json:
        abort(400)

    laptop = {
        'name': request.json['name'],
        'price': request.json['price']
    }

    cur = db.cursor()
    query = 'INSERT INTO week8 (name, price) VALUES (%s, %s);'
    cur.execute(query, (request.json['name'], request.json['price'],))
    db.commit()

    return jsonify(laptop), 201