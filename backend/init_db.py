# backend/init_db.py
from app import app, db
from models import User

def create_admin():
    with app.app_context():
        noc = User.query.filter_by(username='noc').first()
        if noc is None:
            noc = User(username='noc')
            admin.set_password('Kolobok201@')  # Задайте безопасный пароль
            admin.is_admin = True
            db.session.add(admin)
            db.session.commit()
            print("Admin user created successfully.")

if __name__ == '__main__':
    create_admin()
