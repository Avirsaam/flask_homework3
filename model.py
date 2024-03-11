from flask_sqlalchemy import SQLAlchemy


# ○ Имя пользователя (обязательное поле)
# ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# 📌 После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
# 📌 Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
# базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
# об ошибке.

db = SQLAlchemy()

class User(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)    
    surname = db.Column(db.String(80), nullable=False) 
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return f'User({self.name}, {self.email})'