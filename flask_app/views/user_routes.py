import os
from flask import Blueprint, request, redirect, url_for, Response, render_template
from flask_app.services import embedding_api
from flask_app.models import student_model, school_model
from werkzeug.utils import secure_filename

bp = Blueprint('upload', __name__)

@bp.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['file']
    # 저장할 경로 + 파일명
    f.save(secure_filename(f.filename))
    return redirect(url_for('main.upload_index', msg_code=0), code=200)