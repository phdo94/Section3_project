from flask_app import db

class School(db.Model):
    __tablename__ = 'school'

    id = db.Column(db.Integer(), primary_key=True)
    school_name = db.Column(db.String(64), nullable=False)
    settting = db.Column(db.String(64), nullable=False)
    student_id = db.Column(db.Integer(), db.ForeignKey('student.id'))
    
    def __repr__(self):
        return f"School {self.id}"