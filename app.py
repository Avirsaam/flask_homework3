from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from flask_wtf.csrf import CSRFProtect
from datetime import datetime
import secrets
from werkzeug.security import generate_password_hash

from forms import RegistrationForm
from model import db, User

# Задание №8
# 📌 Создать форму для регистрации пользователей на сайте.
# 📌 Форма должна содержать поля "Имя", "Фамилия", "Email",
# "Пароль" и кнопку "Зарегистрироваться".
# 📌 При отправке формы данные должны сохраняться в базе
# данных, а пароль должен быть зашифрован.

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/mydatabase.db'
app.config['SECRET_KEY'] = secrets.token_hex()
app.secret_key = secrets.token_hex()

db.init_app(app)
csrf = CSRFProtect(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')
    
@app.cli.command("add_user")
def add_user():    
    user = User(name='name', surname='surname', email='test@test.com', password='test', created=datetime.utcnow())
    db.session.add(user)
    db.session.commit()
    print('records added')    

@app.route('/')
def index():
    return redirect(url_for('register'))

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user = User.query.filter(User.email==form.email.data).first()      
        if user:
            flash('Пользователь с таким адресом уже существует!', 'danger')
            return redirect(url_for('register'))
        
        hashpass = generate_password_hash(form.password.data, method='sha256')
        
        db.session.add(User(name=form.name.data,
                            surname=form.surname.data,
                            email=form.email.data,
                            password=hashpass,
                            created=datetime.utcnow()))
        db.session.commit()
        return 'Database record created!'
        
    return render_template('register.html', form=form)



