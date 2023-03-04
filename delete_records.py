from app import app, User, db

def add_user():
    with app.app_context():
        num_rows_deleted = db.session.query(User).delete()
    db.session.commit()

add_user()