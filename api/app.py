from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
import create_db

import sqlite3

app = Flask(__name__)
CORS(app)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Python Tech Test API"
    }
)
app.register_blueprint(swaggerui_blueprint)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# TODO - you will need to implement the other endpoints
# GET /api/person/{id} - get person with given id
# POST /api/people - create 1 person
# PUT /api/person/{id} - Update a person with the given id
# DELETE /api/person/{id} - Delete a person with a given id
@app.route("/api/people")
def getall_people():
    conn = sqlite3.connect('test.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_people = cur.execute('SELECT * FROM Person;').fetchall()

    return jsonify(all_people)

@app.route("/api/person/{id}")
def getdetails_person(id ):
    conn = sqlite3.connect('test.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    person_details = cur.execute('SELECT * FROM Person where id = %s;', id).fetchone()

    return jsonify(person_details)

@app.route("/api/person/{id}")

def post_person(id,person):
  conn = sqlite3.connect('test.db')
  conn.row_factory = dict_factory
  cur = conn.cursor()
  fname = person.firstName
  lname = person.lastName
  authorised = person.authorised
  enabled = person.enabled
  data = (fname, lname, authorised, enabled)

  cursor.execute(
    "insert into person(id,firstName, lastName, authorised, enabled) select max(id) ,%s,%s,%s,%s from person",data
)
  connection.commit()

  return true

@app.route("/api/person/{person_id}")

def put_person(id,person):
    conn = sqlite3.connect('test.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    fname = person.firstName
    lname = person.lastName
    authorised = person.authorised
    enabled = person.enabled
    data = (fname,lname,authorised,enabled,person_id )
    cursor.execute(
      "UPDATE person SET firstName=%s, lastName=%s, authorised=%s, enabled=%s WHERE id = %s",
      data)
    connection.commit()

    return true

@app.route("/api/person/{id}")
def delete_person(id ):
    conn = sqlite3.connect('test.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    person_details = cur.execute('DELETE FROM Person where id = %s;', id)



if __name__ == '__main__':
    app.run()
