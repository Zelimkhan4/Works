from flask import Flask, render_template
from data.db_session import create_session, global_init
from data.marsian import User
from data.jobs import Jobs
from config import db_name


app = Flask(__name__)
app.config['SECRET_KEY'] = "yandexlyceum"


if __name__ == "__main__":
    name = input().strip()
    global_init(db_name)
    app.run()
