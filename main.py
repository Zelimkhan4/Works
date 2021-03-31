from flask import Flask, render_template, request, redirect
from data.db_session import create_session, global_init
from data.marsian import User
from data.jobs import Jobs
from config import db_name
from forms.RegistrationForm import RegistrationForm


app = Flask(__name__)
app.config['SECRET_KEY'] = "yandexlyceum"


@app.route('/')
def index():
    sess = create_session()
    jobs = sess.query(Jobs).all()
    return render_template('works.html', title="Работы", jobs=jobs)


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        sess = create_session()
        if form.password.data != form.passwordAgain.data:
            return render_template('register.html', form=form, message='Пароли не совпадают')
        user = User(**form.get_opt())
        user.set_password(form.password.data)
        sess.add(user)
        sess.commit()
        return redirect('/')
    return render_template('register.html', form=form)

if __name__ == "__main__":
    global_init(db_name)
    app.run()
