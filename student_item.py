from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123456@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"
app.config["SQLALCHEMY_ECHO"] = True
class Student(db.Model):
    __tablename__='student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


if __name__ == '__main__':

    db.create_all()

    # student = Student(1,1,1,1)
    s = Student.query.filter(Student.name=='1').one()
    s.name='1111'
    db.session.commit()
    # s = Student.query.all()

    # print(s)

