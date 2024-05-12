from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])
#hostname = 
#username = 
#password = 
#database_name = 
@app.route("/faculty", methods = ["GET", "POST"])
def index():
    '''data = {
  {
    'faculty': 'undecided',
    'student': 'Reinhardt von Lohengramm',
    'major': 'Politics',
    'status': ['in_progress'],
    'updated': '10-01-3600 09:30 AM',
    'id': '01',
  },
  {
    'faculty': 'undecided',
    'student': 'Qui-Gon-Jin',
    'major': 'Jedi Master',
    'status': ['complete'],
    'updated': '10-01-0000 09:30 AM',
    'id': '02',
  },
}'''
    #data = {"index1:": "string1"}
    data = [
  {
    "faculty": 'undecided',
    "student": 'Reinhardt von Lohengramm',
    "major": 'Politics',
    "status": ['in_progress'],
    "updated": '10-01-3600 09:30 AM',
    "id": '01',
  },
  {
    "faculty": 'undecided',
    "student": 'Qui-Gon-Jin',
    "major": 'Jedi Master',
    "status": ['complete'],
    "updated": '10-01-0000 09:30 AM',
    "id": '02',
  },
];
    return jsonify(data)

if __name__== "__main__":
    app.run(debug=True)