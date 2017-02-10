from app import db

class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    description = db.Column(db.String(120))
    uid = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return '<Idea %r>' % (self.title)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    ideas = db.relationship('Idea', backref='idea', lazy='dynamic')

    def __repr__(self):
        return '<Category %r>' % (self.name)
