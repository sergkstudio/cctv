# backend/init_db.py
from backend.app_old import app, db
from backend.models_old import User

def create_admin():
    with app.app_context():
        admin = User.query.filter_by(username='admin').first()
        if admin is None:
            admin = User(username='admin')
            admin.set_password('Kolobok201@')  # Задайте безопасный пароль
            admin.is_admin = True
            db.session.add(admin)
            db.session.commit()
            print("Admin user created successfully.")

if __name__ == '__main__':
    create_admin()
