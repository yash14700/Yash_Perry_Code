from __future__ import print_function
from flask import *
from flask_mysqldb import MySQL
import requests
import json
from helper import *
# from lecture_questions import *
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import yaml
import logging

#Set up
app=Flask(__name__)
UPLOAD_FOLDER = os.path.abspath(os.getcwd()) + '/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = yaml.load(open("db.yaml"))

#Logging
logging.basicConfig(level=logging.DEBUG)

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


############## Upload files API ################################


############# Upload video API ################################
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
                               
@app.route('/api/uploadvideo', methods=['GET', 'POST'])
def uploadvideo():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            app.logger.info("%s", os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # f=open("temp.txt", "a+")
            # f.write("%s", os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload Video File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

# @app.route('/', methods=['GET', 'POST'])
# def create_quiz:
#     cur = mysql.connection.cursor()
#     #raw_questions = #some fuction to get thomas's json
#     quiz_json = edit_json(raw_questions)
#
#     #Create new quiz
#     cur.execute("select * from quiz order by quiz_id desc limit 1")
#     new_id = cur.fetchall()[0][0] + 1
#     cur.execute("insert into quiz(quiz_id) values(%s)", (new_id, ))
#     mysql.connection.commit()
#
#     for question in quiz_json:
#         answers = question['question']['answers']
#         #if answers dont exist
#         if answers == []:
#             continue
#         #if answers exist, find answer
#         ans_text = "-1"
#         for i in range(len(answers)):
#             if answers[i]["answer_weight"] == 1:
#                 ans_text = answers[i]["answer_text"]
#                 break;




# @app.route('/quiz/<quiz_id>', methods=['GET'])
# def display quiz:

#Run
if __name__ == "__main__":
    app.debug = True
    app.run()
