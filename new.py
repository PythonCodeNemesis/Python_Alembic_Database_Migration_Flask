from app import app

def add_user():
    with app.app_context():
        user = User(username='Brii', email='alice@example.com', age=22)
        db.session.add(user)
        db.session.commit()

add_user()
 
