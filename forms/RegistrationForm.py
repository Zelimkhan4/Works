from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    login = StringField('login/email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordAgain = PasswordField('Password again', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField("Register")


    def get_opt(self):
        data = {
            'email': self.login.data, 
            "surname": self.surname.data,
            'name': self.name.data,
            "age": self.age.data,
            'position': self.position.data,
            'speciality': self.speciality.data,
            "address": self.address.data
        }
        return data