from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,DateField,SubmitField
from wtforms.validators import DataRequired,Email




class StudentForm(FlaskForm):
    fullname = StringField(' fullname',validators=[DataRequired()])
    tel=StringField(' tel number',validators=[DataRequired()])
    email=EmailField(' Email',validators=[DataRequired(),Email()])
    joining_date=DateField(' join Date',validators=[DataRequired()])
    btn_submit=SubmitField('Add Student')