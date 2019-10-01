from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=20), unique=True)
    gold = db.Column(db.Integer())
    attack_strength = db.Column(db.Integer())
    hit_points = db.Column(db.Integer())
    luck = db.Column(db.Integer())
    score = db.Column(db.Integer())

    def __repr__(self):
        return '<Player {}>'.format(self.id)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "gold": self.gold,
            "attack_strength": self.attack_strength,
            "hit_points": self.hit_points,
            "luck": self.luck,
            "score": self.score
        }
