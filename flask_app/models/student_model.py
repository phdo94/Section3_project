from flask_app import db

class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer(), primary_key=True)
    class_name = db.Column(db.String(64), nullable=False)
    teacing = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.String(32), nullable=False)
    lunch = db.Column(db.String(32), nullable=False)
    pretest = db.Column(db.Integer(), nullable=False)
    posttest = db.Column(db.PickleType)
    school = db.relationship('Student', backref='students', cascade="all,delete")

    def __init__(self, class_name, teaching, gender, lunch, pretest, posttest):
        self.class_name = class_name
        self.teacing = teaching
        self.gender = gender
        self.lunch = lunch
        self.pretest = pretest
        self.posttest = posttest
    
    def __repr__(self):
        return f"Student {self.id}"