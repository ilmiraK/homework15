import sqlite3


from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/<animal_id>')
def page_by_id(animal_id):
    with sqlite3.connect("animal.db") as connection:
        cursor = connection.cursor()
        query = f"SELECT * FROM animal WHERE index_animal = {animal_id};"
        print(query)
        cursor.execute(query)
        result = cursor.fetchone()
        return jsonify(result)


app.run()
