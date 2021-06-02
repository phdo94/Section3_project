import os
import csv
from flask import Blueprint, render_template, request
from flask_app.utils import main_funcs


bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/upload')
def upload_index():
    
    msg_code = request.args.get('msg_code', None)
    
    alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None

    if alert_msg is None:
        return render_template('student.html', alert_msg=alert_msg)
    
    else:
        student_list = []
        
        CSV_FILEPATH = os.path.join(os.getcwd(), 'test_project.csv') 
        
        with open(CSV_FILEPATH, newline='') as csvfile:
            infile = csv.DictReader(csvfile)
        
            for data in infile:
                student_list.append(data)
        
        return render_template('student.html', alert_msg=alert_msg, student_list=student_list)

@bp.route('/predict', methods=["GET", "POST"])
def compare_index():
    
    users = {'id': 1, 'username':'test'}
    prediction = {
             "result" : "???",
             "compare_text" : "????"
         }

    if request.method == "POST":
        # POST 일 경우에 필요한 코드를 작성해 주세요
        pass

    return render_template('predict_result.html', users=users, prediction=prediction)