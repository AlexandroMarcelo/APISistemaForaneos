from flask import Flask, jsonify,request,make_response,url_for,redirect
from flask_api import FlaskAPI, status, exceptions
from json import dumps
from requests import post

import GradesAPI

apiGrades = GradesAPI.GradesAPI()

app = Flask(__name__)
app.secret_key='12345'

@app.route('/')
def root():
    return "<h1>Hello, Im the API of the ITESM Students Exchange System.</h1>"

@app.route('/user_grades/<string:studentID>', methods=['GET'])
def user_grades(studentID):
    #query = {'user': apiGrades.get_user_grades('A01021383@itesm.mx', 1)}
    query = {'user': apiGrades.get_user_grades(studentID, 1)}
    return jsonify(query)

@app.route('/get_user_password/<string:studentID>', methods=['GET'])
def get_user_password(studentID):
    password_user = apiGrades.get_password_user(studentID)
    if password_user == False:
        return jsonify({'password':'False'})
    return jsonify({'password':password_user.decode('UTF-8')})
    
@app.route('/teacher_name/<string:email>', methods=['GET'])
def teacher_name(email):
    teacher_name = apiGrades.get_teacher_name(email)
    return jsonify({'name':teacher_name})

@app.route('/student_name/<string:email>', methods=['GET'])
def student_name(email):
    student_name = apiGrades.get_name_student(email)
    return jsonify({'name':student_name})

@app.route('/get_user_grades/<string:email>/<string:current_week>', methods=['GET'])
def get_user_grades(email, current_week):
    current_week = int(current_week)
    user_grades = apiGrades.get_user_grades(email, current_week)
    return jsonify(user_grades)
    
@app.route('/get_total_weeks', methods=['GET'])
def get_total_weeks():
    total_weeks = apiGrades.get_total_weeks()
    return jsonify({'total_weeks':total_weeks})
    
@app.route('/get_students_grades/<string:selected_class>/<string:current_week>', methods=['GET'])
def get_students_grades(selected_class, current_week):
    current_week = int(current_week)
    students_grades = apiGrades.get_students_grades(selected_class, current_week)
    return jsonify(students_grades)

@app.route('/get_total_weeks_class/<string:class_name>', methods=['GET'])
def get_total_weeks_class(class_name):
    total_weeks_class = apiGrades.get_total_weeks_class(class_name)
    return jsonify({'total_weeks_class':total_weeks_class})

@app.route('/get_classes_teacher/<string:mail>', methods=['GET'])
def get_classes_teacher(mail):
    classes_teacher = apiGrades.get_classes_teacher(mail)
    json_classes_teacher = []
    for classs in classes_teacher:
        json_classes_teacher.append({'class_name':classs})
    return jsonify(json_classes_teacher)

#@app.route('/insert_grades/<string:class>/<string:week>/<string:studentID>/<string:teamWork>/<string:communication>/', methods=['GET'])
@app.route('/insert_grades', methods=['POST'])
#def insert_grades(studentID, academic, teamWork, communication):
def insert_grades():
    if request.method == 'POST':
        print(request.json)
        insert_grades = apiGrades.insert_grades(request.json)
        return str(insert_grades)
    else:
        return "0"

@app.route('/update_grades', methods=['POST'])
def update_grades():
    if request.method == 'POST':
        print(request.json)
        insert_grades = apiGrades.update_grades(request.json)
        print(insert_grades)
        print(str(insert_grades))
        return str(insert_grades)
    else:
        return "ERROR"

if __name__ == "__main__":
    app.run(debug=True)