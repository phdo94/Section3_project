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

    return render_template('student.html', alert_msg=alert_msg)