from app import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100), index = True, unique=True)
    password = db.Column(db.String(140), nullable=False)


    def __repr__ (self):
        return"<User %r>" %(self.email)

class Events(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(1000),nullable=False)
    creater = db.Column(db.Integer, db.ForeignKey('user.id'))
