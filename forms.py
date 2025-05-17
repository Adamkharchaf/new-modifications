from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,DateField,SubmitField,IntegerField
from wtforms.validators import DataRequired,Email




class StudentForm(FlaskForm):
    fullname = StringField(' fullname',validators=[DataRequired()])
    tel=StringField(' tel number',validators=[DataRequired()])
    email=EmailField(' Email',validators=[DataRequired(),Email()])
    joining_date=DateField(' join Date',validators=[DataRequired()])
    btn_submit=SubmitField('Add Student')


class TeacherForm(FlaskForm):
    fullname = StringField('Teacher fullname', validators=[DataRequired()])
    tel=StringField(' Teacher phone number',validators=[DataRequired()])
    email=EmailField(' Teacher Email',validators=[DataRequired(),Email()])
    
    btn_submit=SubmitField('Add Teacher')
    experience= IntegerField('Teacher experience years', validators=[DataRequired()])
    subject= StringField('Subject', validators=[DataRequired()])
