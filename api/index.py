from flask import Flask, session
from flask import *
from flask_mysqldb import MySQL
import requests
import json
from helper import *

#Set up
app=Flask(__name__)
db = yaml.load(open("db.yaml"))

#db config
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

#typeform api
endpoint="https://api.typeform.com/"
api_token="8WUcqd3P8rKLrhNKkCwVN6c6oNa7wyPw9PkHfjXkrs7S"
headers = {"Authorization": "Bearer 8WUcqd3P8rKLrhNKkCwVN6c6oNa7wyPw9PkHfjXkrs7S"}

@app.route('/', methods=['GET', 'POST'])
def create_quiz:
    cur = mysql.connection.cursor()
    #raw_questions = #some fuction to get thomas's json
    quiz_json = edit_json(raw_questions)

    #Create new quiz
    cur.execute("select * from quiz order by quiz_id desc limit 1")
    new_id = cur.fetchall()[0][0] + 1
    cur.execute("insert into quiz(quiz_id) values(%s)", (new_id, ))
    mysql.connection.commit()

    for question in quiz_json:
        answers = question['question']['answers']
        #if answers dont exist
        if answers == []:
            continue
        #if answers exist, find answer
        ans_text = "-1"
        for i in range(len(answers)):
            if answers[i]["answer_weight"] == 1:
                ans_text = answers[i]["answer_text"]
                break;

        


# @app.route('/quiz/<quiz_id>', methods=['GET'])
# def display quiz:

#Run
if __name__ == "__main__":
    app.debug = False
    app.run()
