from app import db


class Recruit(db.Model):
    __tablename__ = "recruit"

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    num = db.Column(db.Integer, default=0)
    time = db.Column(db.DateTime)
    
    user = db.relationship('User',backref='recruit')

    def __init__(self,user_id,num,time):
        self.user_id = user_id
        self.num = num
        self.time = time

    def __repr__(self):
        return "<Recruit %r>" % self.user_id

class UserStat(db.Model):
    __tablename__ = "user_stat"

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True,nullable=False)
    rated_num = db.Column(db.Integer)
    buy_num = db.Column(db.Integer)

    def __init__(self,user_id,rated_num,buy_num):
        self.user_id=user_id
        self.rated_num=rated_num
        self.buy_num=buy_num

    def __repr__(self):
        return "<UserStat %r>" % self.user_id


class Sim(db.Model):
    __tablename__ = "sim"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    player_one = db.Column(db.Integer, db.ForeignKey('player_base.id'), nullable=False)
    player_two = db.Column(db.Integer, db.ForeignKey('player_base.id'), nullable=False)
    sim = db.Column(db.FLOAT)

    def __init__(self,player_one,player_two,sim):
        self.player_one=player_one
        self.player_two=player_two
        self.sim=sim

    def __repr__(self):
        return "<Sim %r, %r>" % (self.player_one,self.player_two)

class PlayerStat(db.Model):
    __tablename__ = "player_stat"

    player_id = db.Column(db.Integer, db.ForeignKey('player_base.id'), primary_key=True,nullable=False)
    mode = db.Column(db.Integer)

    def __init__(self,player_id,mode):
        self.player_id=player_id
        self.mode = mode

    def __repr__(self):
        return "<PlayerStat %r>" % self.player_id
