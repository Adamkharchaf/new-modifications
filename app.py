from flask import Flask, render_template,request,redirect,url_for
from forms import StudentForm,TeacherForm
from peewee import *
from datetime import datetime
# create flask app
app = Flask(__name__)
app.secret_key = "code secret"

#create database
db = SqliteDatabase("myschool.db")

class Student(db.Model):
    fullname= CharField()
    tel= CharField()
    email= CharField(unique=True)
    joining_date= DateTimeField(default=datetime.now, formats='%Y-%m-%d %H-%M-%S')

    class Meta : 
        database = db


class Teacher(db.Model):
    fullname= CharField()
    tel=CharField()
    email= CharField(unique=True)
    experience= IntegerField()
    subject= CharField
    joining_date= DateTimeField(default=datetime.now, formats='%Y-%m-%d %H-%M-%S')

    class Meta :
        database = db






def initialize_database():
    db.connect()
    db.create_tables([Student,Teacher])
    db.close()

with app.app_context():
    initialize_database()




# creating the first route for index page
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


# creating the student route
@app.route("/student", methods=['GET', 'POST'])
def student_list():
    return render_template('student.html')


@app.route("/student/new")
def add_student():
    #create
    form = StudentForm()
    return render_template('student_new.html',form=form)



#creating the teacher route
@app.route("/teachers")
def teachers_list():
    return render_template('teacher.html')

@app.route("/teacher/new",methods=['POST','GET'])
def add_teacher():
    form = TeacherForm()
    if request.method =='POST'and form.validate_on_submit():
       #2)insert new teacher into database
        
        Teacher.create(
           fullname = form.fullname.data,
           tel = form.tel.data,
           email = form.email.data,
           experience = form.experience.data,
           subject = form.subject.data
        )

        return redirect(url_for('teachers_list'))

    return render_template('teacher_new.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)